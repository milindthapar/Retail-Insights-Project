# Risks – Retail Revenue Insights Platform

This document outlines the key risks associated with the design, deployment, and maintenance of the analytics solution, along with their potential impact.

---

## 1. Data Risks

### R1 — Inconsistent Source Files  
If incoming CSV structure changes (column names, order, missing fields), the ETL pipeline may fail.

**Impact:** High  
**Mitigation:** Add schema validation and error logging.

---

### R2 — Data Quality Issues  
Missing or incorrect dates, negative sales, or invalid categories may lead to poor insights.

**Impact:** Medium  
**Mitigation:** Strengthen validation during cleaning; notify stakeholders.

---

### R3 — Forecasting Inaccuracy  
Forecasts depend fully on past data; sudden market changes may reduce accuracy.

**Impact:** Medium  
**Mitigation:** Use forecasts as directional guidance, not precise predictions.

---

## 2. Technical Risks

### R4 — Azure SQL Downtime  
Any outage or network issue may stop ETL uploads or break the Power BI connection.

**Impact:** High  
**Mitigation:** Retry logic, scheduled checks, alert logs.

---

### R5 — Automation Failure  
Task Scheduler requires the machine to be ON; script failures may go unnoticed.

**Impact:** Medium  
**Mitigation:** Enable logging, review `etl_log.txt`, consider email alerts.

---

### R6 — Power BI Refresh Limitations  
Power BI Service refresh may fail due to capacity or credential issues.

**Impact:** Medium  
**Mitigation:** Maintain credentials, monitor refresh history.

---

## 3. Business Risks

### R7 — Misinterpretation of Insights  
Stakeholders may misread visuals if not trained properly.

**Impact:** Medium  
**Mitigation:** Create a short “How to Use the Dashboard” guide.

---

### R8 — Over-reliance on Single Dataset  
Business decisions based solely on the Superstore dataset may be limited.

**Impact:** Low  
**Mitigation:** Clarify that this is a portfolio project using sample data.

---

## 4. Security Risks

### R9 — Credential Exposure  
Storing database passwords incorrectly may expose sensitive information.

**Impact:** High  
**Mitigation:** Use environment variables; never commit credentials.

---

### R10 — Unrestricted Power BI Access  
If reports are not permissioned correctly, financial data may be exposed internally.

**Impact:** Medium  
**Mitigation:** Apply workspace-level access control.

---

## 5. Operational Risks

### R11 — Manual Dependency  
If automation fails, manual refresh may be required.

**Impact:** Medium  
**Mitigation:** Add fallback manual refresh instructions.

---

### R12 — Lack of Version Control on Data  
Source files may change without version history.

**Impact:** Low  
**Mitigation:** Maintain a `/data/archive/` folder for historical versions.