import pandas as pd
from typing import List

def cleanup_data(df: pd.DataFrame, to_remove: List[str]) -> pd.DataFrame:
    """
    Take DataFrame, cleanup it up to remove empty values, and
    remove unneeded fields then return existing mutated DataFrame.

    Parameters
    ----------
    df: DataFrame
        DataFrame to process and cleanup fields
    to_remove: List[str]
        List of fields to remove from the DataFrame

    Returns
    ----------
    DataFrame:
        Altered DataFrame after cleanup performed

    """
    return df

def convert_fields(df: pd.DataFrame, fields: List[str]) -> pd.DataFrame:
    """
    Return mutated DataFrame after converting columns
    such as Gender (M, F) to (0, 1).

    Parameters
    ----------
    df: DataFrame
        DataFrame to process and cleanup fields
    fields: List[str]
        List of field names to convert to numerical equivalents

    Returns
    ----------
    DataFrame:
        Altered DataFrame after conversion performed

    """
    return df

def clean_all(df: pd.DataFrame, to_remove: List[str], fields: List[str]) -> pd.DataFrame:
    """
    Take DataFrame, cleanup it up to remove empty values,
    remove unneeded fields, and convert columns such as 
    Gender (M, F) to (0, 1), then return existing mutated DataFrame.

    Parameters
    ----------
    df: DataFrame
        DataFrame to process and cleanup fields
    to_remove: List[str]
        List of fields to remove from the DataFrame
    fields: List[str]
        List of field names to convert to numerical equivalents

    Returns
    ----------
    DataFrame:
        Altered DataFrame after cleanup and conversion performed

    """
    return df