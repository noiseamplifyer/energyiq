import pandas as pd


def check_missing_values(df):

    return int(
        df.isna().sum().sum()
    )


def check_duplicate_timestamps(df):

    return int(
        df["timestamp"].duplicated().sum()
    )


def check_timestamp_order(df):

    return bool(
        df["timestamp"].is_monotonic_increasing
    )


def check_negative_values(df, columns):

    result = {}

    for column in columns:

        count = (
            df[column] < 0
        ).sum()

        result[column] = int(count)

    return result


def run_quality_checks(df, numeric_columns):

    result = {
        "total_rows": len(df),

        "missing_values":
            check_missing_values(df),

        "duplicate_timestamps":
            check_duplicate_timestamps(df),

        "timestamps_sorted":
            check_timestamp_order(df),

        "negative_values":
            check_negative_values(
                df,
                numeric_columns
            )
    }

    return result