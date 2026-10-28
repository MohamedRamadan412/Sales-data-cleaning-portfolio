from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
SQL_DIR = BASE_DIR / "sql"

RAW_FILE = DATA_DIR / "sales_raw.csv"
CLEAN_FILE = OUTPUT_DIR / "sales_clean.csv"
DB_FILE = OUTPUT_DIR / "sales.db"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1) Read source data
    df = pd.read_csv(RAW_FILE)
    original_rows = len(df)

    # 2) Clean text fields and convert types
    df["customer_name"] = df["customer_name"].astype(str).str.strip()
    df["city"] = df["city"].astype(str).str.strip()
    df["product"] = df["product"].astype(str).str.strip()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # 3) Remove duplicate orders and invalid records
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    df = df.dropna(subset=["order_id", "order_date", "customer_name", "product",
                           "quantity", "unit_price", "city"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]

    # 4) Add calculated revenue field
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

    # 5) Save cleaned CSV
    df.to_csv(CLEAN_FILE, index=False, encoding="utf-8-sig")

    # 6) Load data into SQLite database
    with sqlite3.connect(DB_FILE) as conn:
        df.to_sql("sales", conn, if_exists="replace", index=False)

    print("Pipeline completed successfully.")
    print(f"Original rows: {original_rows}")
    print(f"Clean rows: {len(df)}")
    print(f"Rows removed: {original_rows - len(df)}")
    print(f"Total revenue: {df['revenue'].sum():,.2f}")
    print(f"Clean CSV: {CLEAN_FILE}")
    print(f"SQLite database: {DB_FILE}")


if __name__ == "__main__":
    main()
