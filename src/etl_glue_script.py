import sys
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Load from Glue catalog table
source_df = glueContext.create_dynamic_frame.from_catalog(
    database="zs-pharma-db", table_name="raw"
).toDF()

# Data Cleaning
cleaned_df = source_df.dropna(subset=["sale_datetime", "quantity", "revenue"]) \
                      .filter(F.col("quantity") > 0)

# Add year and month columns
final_df = cleaned_df.withColumn("year", F.year("sale_datetime")) \
                     .withColumn("month", F.month("sale_datetime"))

# Write to S3 in Parquet format, partitioned by year/month
final_df.write.mode("overwrite") \
        .partitionBy("year", "month") \
        .parquet("s3://zs-pharma-etl/processed/sales_parquet/")

job.commit()

