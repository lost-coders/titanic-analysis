import pandas as pd
from typing import List

def cleanup_data(df: pd.DataFrame, params: List[str]) -> pd.DataFrame:
    """
    Take DataFrame, cleanup it up to remove empty values, and
    convert columns such as Embarked (C, Q, S) to (0, 1, 2),
    then return existing mutated DataFrame.

    Parameters
    ----------
    df: DataFrame
        DataFrame to process and cleanup fields
    params: List[str]
        List of fields to convert to integer equivalents

    Returns
    ----------
    DataFrame

    """
    return df