# Acceptance Criteria – Retail Revenue Insights Platform  
Format: Gherkin (Given / When / Then)

This document specifies the acceptance criteria for the user stories defined in USER_STORIES.md.  
These criteria ensure clarity, testability, and alignment with business needs.

---

## 1. Executive Summary Metrics

### User Story Reference:
Sales Director – Executive Overview

### Acceptance Criteria:

**Scenario 1 – Display core KPIs**
- **Given** the dashboard is loaded  
- **When** the data is fetched from Azure SQL  
- **Then** I should see Total Revenue, Total Profit, and Profit Margin KPIs  
- **And** all numbers should update automatically after the ETL refresh.

**Scenario 2 – KPI accuracy validation**
- **Given** the KPIs are displayed  
- **When** I manually run the SQL validation queries  
- **Then** the KPI values should match the SQL results exactly.

---

## 2. Regional Performance Insights

### User Story Reference:
Regional Manager – Geographic Insights

### Acceptance Criteria:

**Scenario 1 – Regional comparison chart**
- **Given** the user selects a date range  
- **When** the dashboard loads  
- **Then** I should see revenue and profit by region/state.

**Scenario 2 – Drill-down capability**
- **Given** a region is clicked  
- **When** I drill down  
- **Then** the dashboard should show city-level breakdown.

---

## 3. Discount Impact Analysis

### User Story Reference:
Finance Manager – Discount Impact

### Acceptance Criteria:

**Scenario 1 – Discount vs Profit chart**
- **Given** discount and profit fields exist in the dataset  
- **When** the dashboard renders Page 4  
- **Then** I should see the relationship between discount level and profit.

**Scenario 2 – Identify loss-making items**
- **Given** the product list is displayed  
- **When** filters are applied  
- **Then** I should be able to identify products with negative or low profit margins.

---

## 4. Customer Segmentation (RFM)

### User Story Reference:
Marketing Lead – Customer Segmentation

### Acceptance Criteria:

**Scenario 1 – Segmentation logic**
- **Given** customer behavioural data is available  
- **When** segmentation logic is executed  
- **Then** customers should be categorised by Recency, Frequency, Monetary value.

**Scenario 2 – Segment-level filtering**
- **Given** segments exist  
- **When** I choose a segment in Power BI  
- **Then** the visualisations should update to show metrics for that segment.

---

## 5. Sales Forecasting

### User Story Reference:
Supply Chain Lead – Demand Forecasting

### Acceptance Criteria:

**Scenario 1 – Power BI forecasting**
- **Given** a line chart with date and revenue  
- **When** forecasting is applied  
- **Then** a future projection should appear for 3–6 months.

**Scenario 2 – ARIMA model validation**
- **Given** Python ARIMA forecasting is completed  
- **When** comparing ARIMA and Power BI results  
- **Then** trend direction should be consistent across both.

---

## 6. Automated Refresh

### User Story Reference:
BI Analyst – Automated Refresh

### Acceptance Criteria:

**Scenario 1 – ETL refresh success**
- **Given** Task Scheduler triggers the Python script  
- **When** the ETL job completes  
- **Then** Azure SQL table should contain the latest dataset.

**Scenario 2 – Power BI scheduled refresh**
- **Given** Power BI Service is configured  
- **When** the scheduled refresh runs  
- **Then** the dashboard should show the updated values without manual effort.

---

## 7. Product Profitability

### User Story Reference:
CEO – Product Profitability

### Acceptance Criteria:

**Scenario 1 – Profitability ranking**
- **Given** product-level data exists  
- **When** the dashboard loads  
- **Then** products should be ranked by profitability.

**Scenario 2 – Category drilldown**
- **Given** a category is selected  
- **When** the user drills down  
- **Then** sub-category and product-level profits should display.

---

## 8. Shipping Mode Analysis

### User Story Reference:
Customer Experience Manager – Shipping Behaviour

### Acceptance Criteria:

**Scenario 1 – Shipping cost vs delivery speed**
- **Given** shipping mode data exists  
- **When** the dashboard renders  
- **Then** I should see ship mode usage patterns and delivery trends.

**Scenario 2 – Customer impact view**
- **Given** the user selects a customer segment  
- **When** viewing shipping details  
- **Then** delivery speed and mode distribution should be updated accordingly.