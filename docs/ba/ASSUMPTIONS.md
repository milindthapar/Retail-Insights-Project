# Assumptions – Retail Revenue Insights Platform

This document outlines assumptions made during planning and development of the analytics solution.

---

## 1. Data Assumptions
- The source CSV dataset is updated periodically and follows the same structure each time.
- Order dates are always valid and correctly reflect the transaction timeline.
- Discount and Profit values are already calculated correctly in the dataset.
- All required fields exist in the source data and no major redesign of schema is needed.

---

## 2. Technical Assumptions
- Azure SQL database remains online and accessible during ETL execution.
- ODBC Driver 18 for SQL Server is installed and working.
- Users have access to Power BI Desktop and Power BI Service.
- ETL script runs on a Windows machine with Task Scheduler available.

---

## 3. Business Assumptions
- Stakeholders are familiar with Power BI navigation and filtering.
- Business will provide timely updates if new fields or metrics need to be added.
- Forecasting accuracy expectations are reasonable (trends > exact values).
- Daily refresh frequency is sufficient for business operations.

---

## 4. Project Assumptions
- Scope remains limited to revenue, profit, discount, segmentation, and forecasting insights.
- No real-time data streaming is required.
- All BA and technical documentation will be stored and versioned in GitHub.