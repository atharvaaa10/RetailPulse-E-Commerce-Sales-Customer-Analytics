"""Data cleaning pipeline templates for RetailPulse datasets.

This module provides reusable interfaces for standardizing and cleaning
raw transactions, customers, and products data.

NOTE: Do NOT automatically implement cleaning rules here.
Fill in each function as you complete the corresponding cleaning notebooks.
"""

import pandas as pd


def clean_transactions_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize raw transactions DataFrame.

    Investigation tasks:
    - Handle nulls and missing values in critical columns.
    - Remove or handle duplicate transactions.
    - Standardize date formatting across all rows.
    - Convert numerical data types appropriately.
    - Validate business bounds (Quantity > 0, Discount between 0 and 1, etc.).
    - Fix categorical variations in Payment_Method, Order_Status, etc.

    Args:
        df: Raw transactions DataFrame.

    Returns:
        Cleaned transactions DataFrame.
    """
    cleaned_df = df.copy()
    # TODO: Implement step-by-step cleaning operations based on Notebook 03 findings
    return cleaned_df


def clean_customers_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize raw customers DataFrame.

    Investigation tasks:
    - Deduplicate Customer_ID or records.
    - Standardize text casing and trimming for Name, City, State.
    - Normalize Gender and Customer_Segment categories.
    - Parse Registration_Date to datetime.
    - Validate Age range and handle anomalies/nulls.

    Args:
        df: Raw customers DataFrame.

    Returns:
        Cleaned customers DataFrame.
    """
    cleaned_df = df.copy()
    # TODO: Implement step-by-step cleaning operations based on Notebook 04 findings
    return cleaned_df


def clean_products_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize raw products DataFrame.

    Investigation tasks:
    - Deduplicate Product_ID or records.
    - Standardize Category, Subcategory, and Brand naming.
    - Verify Cost_Price and Listed_Price formatting and positivity.
    - Check for cost > listed price logical inconsistencies.
    - Handle missing ratings or invalid rating ranges.

    Args:
        df: Raw products DataFrame.

    Returns:
        Cleaned products DataFrame.
    """
    cleaned_df = df.copy()
    # TODO: Implement step-by-step cleaning operations based on Notebook 05 findings
    return cleaned_df
