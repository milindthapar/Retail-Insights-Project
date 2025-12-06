import pandas as pd
import pyodbc
import logging

# -----------------------
# 1. CONFIGURATION
# -----------------------

# PATH TO YOUR RAW DATA (or use clean file if you prefer)
RAW_CSV_PATH = r"C:\Users\thapa\OneDrive\Desktop\Retail-Insights_Project\data\superstore_clean.csv"
# If this still gives issues, switch to superstore_clean.csv:
# RAW_CSV_PATH = r"C:\Users\thapa\OneDrive\Desktop\Retail-Insights_Project\data\superstore_clean.csv"

# LOG FILE PATH
LOG_FILE = r"C:\Users\thapa\OneDrive\Desktop\Retail-Insights_Project\automation\etl_log.txt"

# AZURE SQL DETAILS  >>>>>  FILL THESE  <<<<<
SERVER = ""   # e.g. retailinsightsserver.database.windows.net
DATABASE = ""                      # your DB name
USERNAME = ""               # the admin you created
PASSWORD = ""               # your password

TABLE_NAME = "superstore_orders"

# -----------------------
# 2. SETUP LOGGING
# -----------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("ETL job started...")
logging.info("ETL Job Started")

try:
    # -----------------------
    # 3. LOAD RAW DATA (WITH ENCODING FIX)
    # -----------------------
    logging.info(f"Loading CSV from: {RAW_CSV_PATH}")
    # Try a robust encoding that handles 0xa0 characters
    df = pd.read_csv(RAW_CSV_PATH, encoding="ISO-8859-1", on_bad_lines="skip")
    # If the above still fails, you can try:
    # df = pd.read_csv(RAW_CSV_PATH, encoding="cp1252", on_bad_lines="skip")

    logging.info(f"Raw Data Loaded: {df.shape[0]} rows.")

    # -----------------------
    # 4. BASIC CLEANING (MATCH WHAT YOU DID IN NOTEBOOK)
    # -----------------------
    # Drop duplicates
    df = df.drop_duplicates()

    # Parse dates
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], errors="coerce")

    # Remove rows with invalid dates
    df = df[df["Order_Date"].notnull()]

    logging.info(f"Data Cleaned: {df.shape[0]} rows remain after basic cleaning.")

    # IMPORTANT: ensure columns are in the same order as your SQL table
    expected_cols = [
        "Row_ID",
        "Order_ID",
        "Order_Date",
        "Ship_Date",
        "Ship_Mode",
        "Customer_ID",
        "Customer_Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Postal_Code",
        "Region",
        "Product_ID",
        "Category",
        "Sub_Category",
        "Product_Name",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    df = df[expected_cols]

    logging.info("Columns aligned to SQL table schema.")

    # -----------------------
    # 5. CONNECT TO AZURE SQL
    # -----------------------
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD}"
    )

    logging.info("Connecting to Azure SQL...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    logging.info("Connected to Azure SQL successfully.")

    # -----------------------
    # 6. CLEAR OLD DATA
    # -----------------------
    truncate_sql = f"TRUNCATE TABLE {TABLE_NAME};"
    cursor.execute(truncate_sql)
    conn.commit()
    logging.info(f"Old data truncated from table {TABLE_NAME}.")

    # -----------------------
    # 7. INSERT NEW DATA
    # -----------------------
    insert_sql = f"""
        INSERT INTO {TABLE_NAME} (
            Row_ID, Order_ID, Order_Date, Ship_Date, Ship_Mode,
            Customer_ID, Customer_Name, Segment, Country, City, State,
            Postal_Code, Region, Product_ID, Category, Sub_Category,
            Product_Name, Sales, Quantity, Discount, Profit
        )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """

    logging.info("Starting row insert into Azure SQL...")

    for _, row in df.iterrows():
        cursor.execute(insert_sql, tuple(row[col] for col in expected_cols))

    conn.commit()
    conn.close()

    logging.info("New data uploaded successfully.")
    print("ETL job finished successfully. Check etl_log.txt for details.")

except Exception as e:
    logging.error(f"ETL Job FAILED: {str(e)}")
    print("ETL job FAILED. Check etl_log.txt for error details.")

finally:
    logging.info("ETL Job Finished.\n")
