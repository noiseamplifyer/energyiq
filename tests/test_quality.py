import pandas as pd
import numpy as np

from src.quality_checks import (
    check_missing_values,
    check_duplicate_timestamps,
    check_timestamp_order
)

def create_test_dataframe():

    return pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2026-01-01 10:00",
            "2026-01-01 10:01",
            "2026-01-01 10:02"
        ]),

        "power": [
            1.2,
            1.5,
            2.0
        ]
    })
    
def test_missing_values():

    df = create_test_dataframe()

    result = check_missing_values(df)

    assert result == 0
    

def test_duplicate_timestamps():

    df = create_test_dataframe()

    df.loc[2, "timestamp"] = df.loc[1, "timestamp"]

    result = check_duplicate_timestamps(df)

    assert result == 1
    
    
def test_timestamp_order():

    df = create_test_dataframe()

    result = check_timestamp_order(df)

    assert result is True
    
def test_timestamp_not_sorted():

    df = create_test_dataframe()

    df = df.iloc[::-1]

    result = check_timestamp_order(df)

    assert result is False