# Cleaned Datasets Directory

This directory stores the cleaned, standardized, and validated datasets exported from the data cleaning pipeline notebooks:

* `03_data_cleaning_transactions.ipynb` -> `transactions_cleaned.csv`
* `04_data_cleaning_customers.ipynb` -> `customers_cleaned.csv`
* `05_data_cleaning_products.ipynb` -> `products_cleaned.csv`

---

## Guidelines for Cleaned Data:

1. **Never overwrite raw data**: All transformations must read from `data/raw/` and output strictly into `data/cleaned/`.
2. **Standard naming convention**: Keep cleaned filenames consistent (e.g., `<entity>_cleaned.csv`).
3. **Validation before downstream use**: Ensure datasets pass all checks in `notebooks/06_data_validation.ipynb` before proceeding to SQL loading, EDA, or Power BI.
4. **Encoding & Formatting**:
   - Format: CSV (UTF-8)
   - Date formats: Standardized ISO format (`YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`)
   - Null handling: Explicit representations consistent across all cleaned tables.
