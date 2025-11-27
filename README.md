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

---

## 4. Data Cleaning & Preparation (Python)

The raw dataset (`superstore_raw.csv`) contains retail order information including customer, product, sales, and profit fields. Cleaning was performed using Python to prepare a reliable analytics layer.

**Key cleaning steps:**

- Resolved encoding errors during CSV import  
- Removed duplicates and invalid rows  
- Converted `Order_Date` & `Ship_Date` to proper datetime types  
- Checked for negative or missing values  
- Standardised category names  
- Ensured schema alignment with Azure SQL  
- Exported cleaned file: `superstore_clean.csv`

All transformation logic lives in:  
`python/cleaning_superstore.ipynb`

---

## 5. Azure SQL Data Model

The cleaned dataset is loaded into Azure SQL as a single fact-style table: **`superstore_orders`**.

**Schema includes:**

- Order fields → `Order_ID`, `Order_Date`, `Ship_Date`, `Ship_Mode`  
- Customer fields → `Customer_ID`, `Customer_Name`, `Segment`  
- Geography → `Country`, `State`, `City`, `Region`  
- Product fields → `Product_ID`, `Category`, `Sub_Category`, `Product_Name`  
- Metrics → `Sales`, `Quantity`, `Discount`, `Profit`

SQL scripts used:

- `sql/create_superstore_table.sql` → creates the table  
- `sql/analysis_queries.sql` → business KPI queries (profit, discount impact, segment analysis)

Azure SQL acts as the **central data warehouse** for the project.

---

## 6. Automated ETL Pipeline (Python + Task Scheduler)

The ETL automation script (`automate_etl_refresh.py`) performs:

1. Loads the cleaned dataset  
2. Runs light validation  
3. Connects to Azure SQL using **ODBC Driver 18**  
4. Truncates the existing table  
5. Inserts fresh rows  
6. Logs every run (`etl_log.txt`)

This script is scheduled via **Windows Task Scheduler** to run nightly, ensuring the dashboard uses up-to-date data without manual intervention.

**Result:**  
Fully automated data pipeline → CSV → Python ETL → Azure SQL → Power BI refresh.

---

## 7. Power BI Dashboard (5 Pages)

The Power BI report (`RetailInsights.pbix`) connects directly to Azure SQL and provides a clean business-facing interface.

### **Page 1 – Executive Summary**
- Total Revenue, Total Profit, Profit Margin  
- Top 10 regions, segments, and categories  
- Quick profitability overview  

### **Page 2 – Sales & Profit Trends**
- Monthly revenue & profit chart  
- Seasonality patterns  
- Category/segment breakdown  

### **Page 3 – Customer Insights**
- RFM-style segmentation  
- Customer contribution to revenue  
- High-value vs at-risk customers  

### **Page 4 – Product & Discount Analysis**
- Discount vs Profit matrix  
- Category/Sub-category margin performance  
- Most/least profitable SKUs  

### **Page 5 – Forecasting & Modern Analytics**
- Power BI built-in forecast (3–6 months)  
- KPI cards (3-month vs 6-month comparison)  
- Python ARIMA forecast validation plot  

Screenshots will be added under:  
`outputs/dashboard_screenshots/`

---

## 8. Forecasting (Python ARIMA)

Forecasting was implemented using `statsmodels` ARIMA to validate the Power BI forecast.

**Steps:**

1. Aggregate monthly revenue  
2. Fit an ARIMA model (e.g. ARIMA(1,1,1))  
3. Forecast upcoming months  
4. Plot actual vs forecast values  
5. Compare with Power BI’s decomposition-based forecast  

The objective was **cross-validation** — ensuring consistency between two forecasting engines.

Outputs:  
`outputs/arima_forecast.png`

---

## 9. End-to-End Automation Flow

**Daily at 2 AM:**

1. Python ETL script refreshes **Azure SQL**  
2. Power BI Scheduled Refresh (in Service) retrieves fresh data  
3. Dashboard updates automatically  
4. Business stakeholders open the report anytime and see the latest metrics  

This mirrors industry-grade data refresh pipelines with **zero manual steps**.

---

## 10. How to Run This Project Locally

### **Clone the repo**
```bash
git clone https://github.com/<your-username>/Retail-Insights-Project.git

---

---

## 11. Business Analyst / Agile Documentation (To Be Added)

This project includes a dedicated BA layer, which will be added next:

- Epic & multiple user stories  
- Acceptance criteria (Gherkin format)  
- Requirements & assumptions  
- High-level BPMN process flow  
- Stakeholder analysis & KPIs  
- Risks, constraints, and recommendations  
- Sprint planning & Jira-style board mockup  

This simulates real-world Agile delivery in analytics.

---

## 12. About the Author

**Milind Thapar**  
Business Analyst / Data Analyst (Python, SQL, Azure, Power BI, Agile, Automation)

This project is part of a 10-project portfolio combining **business problem solving** with **modern analytics and engineering skills**.
