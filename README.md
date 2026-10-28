# Sales Data Cleaning & Reporting Pipeline

A beginner-friendly portfolio project using Python, Pandas, CSV, SQLite, and SQL.

## What it does
1. Reads sample sales data from `data/sales_raw.csv`.
2. Trims whitespace and converts columns to the correct data types.
3. Removes duplicate order IDs and invalid records (such as zero or negative quantities).
4. Calculates revenue as `quantity × unit_price`.
5. Exports cleaned data to `output/sales_clean.csv`.
6. Loads the cleaned data into `output/sales.db` (SQLite).
7. Provides SQL queries for total revenue, revenue by product, revenue by city, and daily revenue.

## Requirements
- Python 3.10+
- pandas

## Run in VS Code
Open this folder in VS Code, then in the Terminal run:

```bash
python -m venv .venv
```

Activate the environment:

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:
```bat
.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependency and run:
```bash
python -m pip install -r requirements.txt
python pipeline.py
```

After it finishes, check the `output` folder.

## SQL queries
The database is SQLite, so you can run the queries in `sql/reports.sql` using a SQLite viewer or Python. The project intentionally uses SQLite to keep setup simple and avoid requiring a database server.

## Portfolio description
**Sales Data Cleaning & Reporting Pipeline | Python, Pandas, SQL, SQLite**

Built a small ETL pipeline to clean raw sales data, remove duplicate and invalid records, calculate revenue, load results into a database, and generate SQL reports by product, city, and date.

## Important
This is a demonstration project with synthetic sample data, not real client data. Adapt the cleaning rules to each client's requirements before using this workflow for paid work.
