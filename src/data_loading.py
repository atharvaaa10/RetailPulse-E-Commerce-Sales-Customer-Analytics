"""Data loading utilities for RetailPulse datasets.

This module provides helper functions to load raw and cleaned datasets
using relative paths and configurable loading options.
"""

from pathlib import Path
from typing import Optional
import pandas as pd

# Base relative paths
DATA_DIR = Path("data")
RAW_DATA_DIR = DATA_DIR / "raw"
CLEANED_DATA_DIR = DATA_DIR / "cleaned"


def load_raw_transactions(
    filepath: Optional[Path] = None, **kwargs
) -> pd.DataFrame:
    """Load the raw transactions dataset.

    Args:
        filepath: Optional custom Path to transactions.csv.
                  Defaults to data/raw/transactions.csv.
        **kwargs: Additional keyword arguments passed to pd.read_csv.

    Returns:
        pd.DataFrame containing raw transactions data.
    """
    path = filepath or (RAW_DATA_DIR / "transactions.csv")
    # TODO: Implement robust reading logic, custom parse_dates or chunking if desired
    return pd.read_csv(path, **kwargs)


def load_raw_customers(
    filepath: Optional[Path] = None, **kwargs
) -> pd.DataFrame:
    """Load the raw customers dataset.

    Args:
        filepath: Optional custom Path to customers.csv.
                  Defaults to data/raw/customers.csv.
        **kwargs: Additional keyword arguments passed to pd.read_csv.

    Returns:
        pd.DataFrame containing raw customers data.
    """
    path = filepath or (RAW_DATA_DIR / "customers.csv")
    # TODO: Implement robust reading logic
    return pd.read_csv(path, **kwargs)


def load_raw_products(
    filepath: Optional[Path] = None, **kwargs
) -> pd.DataFrame:
    """Load the raw products dataset.

    Args:
        filepath: Optional custom Path to products.csv.
                  Defaults to data/raw/products.csv.
        **kwargs: Additional keyword arguments passed to pd.read_csv.

    Returns:
        pd.DataFrame containing raw products data.
    """
    path = filepath or (RAW_DATA_DIR / "products.csv")
    # TODO: Implement robust reading logic
    return pd.read_csv(path, **kwargs)


def load_cleaned_data(dataset_name: str, **kwargs) -> pd.DataFrame:
    """Load a processed dataset from data/cleaned/.

    Args:
        dataset_name: Name of the dataset ('transactions', 'customers', or 'products').
        **kwargs: Additional keyword arguments passed to pd.read_csv.

    Returns:
        pd.DataFrame containing cleaned dataset.
    """
    filename = f"{dataset_name}_cleaned.csv"
    path = CLEANED_DATA_DIR / filename
    # TODO: Validate that the file exists and load clean dataset
    return pd.read_csv(path, **kwargs)
