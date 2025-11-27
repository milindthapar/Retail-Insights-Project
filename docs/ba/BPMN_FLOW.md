# BPMN Process Flow – Retail Revenue Insights Platform

This document describes the high-level Business Process Model and Notation (BPMN) flow for the end-to-end Retail Revenue Insights pipeline.

The flow covers:  
- Data ingestion  
- Cleaning & validation  
- Cloud upload  
- Automated refresh  
- Dashboard consumption  

A visual BPMN diagram (`BPMN_FLOW.png`) will be added here once created.

---

## 1. High-Level BPMN Description

### **Start Event**
Process begins when a new CSV file (raw sales data) becomes available.

---

### **Task 1: Load Raw Data**
Python reads the raw CSV file and loads it into a pandas DataFrame.

---

### **Task 2: Data Cleaning & Validation**
- Remove duplicates  
- Fix encoding issues  
- Standardise schema  
- Parse date fields  
- Validate sales/discount values  

**Gateway:**  
If validation fails → log error → End.  
If validation passes → continue.

---

### **Task 3: Prepare Dataset**
Transform the cleaned dataset into the schema required by Azure SQL.

---

### **Task 4: Connect to Azure SQL**
Establish a secure connection using ODBC Driver 18.

---

### **Task 5: Upload to Azure SQL**
- Truncate table  
- Insert cleaned rows  
- Commit transaction  
- Log success/failure  

---

### **Intermediate Timer Event**
Nightly trigger via Task Scheduler (e.g., 2:00 AM).

---

### **Task 6: Power BI Refresh**
Power BI Service refreshes the dataset using Azure SQL.

---

### **Task 7: Dashboard Consumption**
Business users access the refreshed report:
- Sales Director (KPI overview)  
- Marketing Lead (segmentation)  
- Finance Manager (discount impact)  
- Regional Manager (geographic insights)  
- CEO (profitability drilldown)  

---

### **End Event**
Updated insights are available for decision-making.

---

## 2. BPMN Diagram Placeholder

The BPMN diagram will be added here:  
**`BPMN_FLOW.png`**

Example notation to be included:

- **Start Event** → circle  
- **Task** → rectangle  
- **Gateway** → diamond  
- **Intermediate Event (Timer)** → clock icon  
- **End Event** → bold circle  

A full diagram will be created using draw.io or Miro.