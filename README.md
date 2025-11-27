# Retail Revenue Insights – End-to-End Analytics (Python • Azure SQL • Power BI • Automation)

This project is an **end-to-end retail analytics solution** built to showcase both:

- **Business Analyst skills** (requirements, KPIs, insights, storytelling), and  
- **Data Analytics / Engineering skills** (Python, SQL, Azure, Power BI, automation).

It simulates how a retailer would understand **revenue, profit, discounts, and customer behaviour** and then automate reporting for decision-makers.

---

## 1. Business Problem

A mid-size retail business wants to answer:

1. How are **revenue and profit** trending over time?
2. Which **customer segments, regions and product categories** drive the most value?
3. Are **discounts** improving sales or killing profit?
4. Which customers should be targeted for **retention and cross-sell**?
5. What does the **next few months of revenue** look like?
6. Can all of this update **automatically**, without manual Excel/CSV work?

This project delivers a solution that does exactly that, using a cloud data model and automated refresh.

---

## 2. Tech Stack & Architecture

**Tech used:**

- **Python** – data cleaning, transformation, ARIMA forecasting, ETL script  
- **Azure SQL Database** – cloud data storage (`superstore_orders` table)  
- **PyODBC + ODBC Driver 18** – secure connection from Python to Azure SQL  
- **Power BI Desktop + Power BI Service** – data modelling and dashboards  
- **Windows Task Scheduler** – nightly automated ETL refresh  
- *(BA/Agile tools like Jira / Confluence style docs are added separately as BA documentation.)*

**High-level pipeline:**

1. Raw retail data → `data/superstore_raw.csv`  
2. Python cleaning notebook → `data/superstore_clean.csv`  
3. Python ETL script → uploads cleaned data to **Azure SQL**  
4. Power BI connects to **Azure SQL** (`superstore_orders` table)  
5. Power BI report (5-page dashboard) used by business stakeholders  
6. Windows Task Scheduler runs ETL nightly → **automated refresh**

---

## 3. Repository Structure

```text
Retail-Insights-Project/
│
├── data/
│   ├── superstore_raw.csv          # Original dataset
│   ├── superstore_clean.csv        # Cleaned dataset used for modelling
│
├── python/
│   ├── cleaning_superstore.ipynb   # Data cleaning & preparation
│   ├── arima_revenue_forecast.ipynb# ARIMA validation of revenue forecast
│
├── sql/
│   ├── create_superstore_table.sql # DDL for Azure SQL table
│   ├── analysis_queries.sql        # Business analysis queries (profit, RFM, etc.)
│
├── powerbi/
│   ├── RetailInsights.pbix         # Power BI report (5-page dashboard)
│
├── automation/
│   ├── automate_etl_refresh.py     # Python ETL script (CSV → Azure SQL)
│   ├── etl_log.txt                 # Log file for ETL runs (example)
│
├── outputs/
│   ├── arima_forecast.png          # Plot: historical vs ARIMA forecast
│   ├── dashboard_screenshots/      # Exported images of each report page
│
└── README.md
