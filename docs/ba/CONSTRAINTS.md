# Constraints – Retail Revenue Insights Platform

This document outlines the constraints impacting the design, development, and delivery of the analytics solution.

---

## 1. Technical Constraints
- Azure SQL is used as the only cloud database; no additional cloud tools are available in scope.
- ETL automation relies on Windows Task Scheduler, limiting cross-platform deployment (Windows-only).
- Python ARIMA forecasting is limited by the historical range and quality of the dataset.
- Power BI forecasting is subject to its built-in algorithm and has limited customisation.

---

## 2. Data Constraints
- Dataset is static and based on historical superstore data; real-time updates are not supported.
- No access to external datasets such as CRM, ERP, or customer lifetime value calculations.
- Missing cost-of-goods fields limit ability to calculate detailed gross margin metrics.
- Hierarchies (Region → State → City) must match the dataset’s structure; cannot invent missing data.

---

## 3. Business Constraints
- Project scope excludes creation of mobile-optimised dashboards.
- No integration with marketing automation or supply chain systems.
- Forecasting expectation is directional accuracy—not guaranteed precision.

---

## 4. Operational Constraints
- Automation schedule depends on the local machine being powered on.
- Power BI Service refresh limits may apply depending on workspace type.
- Azure SQL free-tier capacity limits may affect performance on very large datasets.

---

## 5. Time Constraints
- This project is delivered under a self-imposed timeline as part of a portfolio.
- Some advanced analytics features (clustering, churn prediction) are intentionally out of scope.