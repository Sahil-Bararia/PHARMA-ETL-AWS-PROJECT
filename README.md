# Pharma Sales Analytics Pipeline – AWS ETL Project

## 🚀 Project Overview
This project demonstrates a complete **ETL and analytics pipeline for pharmaceutical sales data** using AWS services. Built using the **Medallion Architecture (Bronze, Silver, Gold layers)**, it replicates real-world consulting use cases often encountered in healthcare and pharma analytics.

---
## 🚀 Short Summary
I built a Medallion-style ETL pipeline on AWS that ingested synthetic pharma sales transaction data into **S3 (Bronze)**, cleaned and partitioned it using an **AWS Glue PySpark job** and stored it as **Parquet (Silver)**, and then exposed curated, queryable data via **Athena (Gold)**. I optimized for analytics by partitioning by year/month and used Parquet for its columnar performance. I also implemented **windowed SQL (LEAD/LAG, ranking, cumulative sums)** in Athena to surface **trends and product-level month-over-month comparisons**. During the build I debugged Glue catalog name mismatches and fixed IAM permissions to ensure secure writes to S3.

---
## 🏗️ Architecture Layer

- **Bronze Layer**: Raw CSV files ingested into S3.
- **Silver Layer**: Cleaned, deduplicated Parquet files written to S3.
- **Gold Layer**: Aggregated and analytics-ready data queried with Athena.

---

## 🔧 AWS Services Used
- **S3** – Data lake storage for raw, processed, and final datasets
- **AWS Glue** – ETL jobs using PySpark (extract, transform, and load operations)
- **Athena** – SQL-based analytics on curated data
- **AWS IAM** – Role-based access and job permissions
- *(Optionally extensible to QuickSight or Redshift)*

---

## 📂 Data Layers (Medallion Style)
- `zs-pharma-etl/raw/` – CSV files as-is from source
- `zs-pharma-etl/processed/` – Cleaned Parquet format
- `zs-pharma-etl/analytics/` – Final transformed outputs

---

## 🔍 Sample Queries (Athena)
```sql
-- LAG example: Compare monthly sales with previous month
SELECT product, year, month, 
       sales, 
       LAG(sales) OVER (PARTITION BY product ORDER BY year, month) AS previous_sales
FROM analytics_table;

-- LEAD example: Forecast trend with next month sales
SELECT product, year, month, 
       sales, 
       LEAD(sales) OVER (PARTITION BY product ORDER BY year, month) AS next_sales
FROM analytics_table;

-- YOY Growth
SELECT product, year, SUM(sales) AS total_sales
FROM analytics_table
GROUP BY product, year;
```

---

## ✅ Features
- Handles large pharma datasets (sales, regions, SKUs)
- Converts CSV to columnar Parquet format
- Performance-optimized querying with Athena
- Modular and extensible for future ML/BI integration

---

## 📌 How to Run This Project
1. Upload sample `sales_data.csv` to S3 in the `raw/` folder
2. Create and run Glue Job (PySpark script)
3. Validate outputs in `processed/` and `analytics/` folders
4. Use Athena to run analytics queries on curated tables

---

## 🧠 Why Medallion Architecture?
The layered approach ensures:
- Data quality at every stage
- Simplified debugging
- Reusability across downstream systems (BI, ML)

---

## 👨‍💻 Author
**Sahil Bararia**  
Data Engineer | Power BI | Azure | AWS | Python

🔗 [LinkedIn](https://www.linkedin.com/in/sahil-bararia-a09772232/)  
🔗 [GitHub](https://github.com/Sahil-Bararia)

---

