import pandas as pd

def spend_data_validation(df):
    required_columns = ["cloud","year_month","spend"]
    # Check for missing columns, report if any
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"The following columns are missing in spend data: {missing_columns}")

    # Change to desired data types, clean, and re-index
    df_copy = df.copy()
    df_copy["year_month"] = pd.to_datetime(df_copy["year_month"], format="%Y-%m", errors="coerce") # coerce will convert invalid data to NaN or NaT without raising errors!
    df_copy["spend"] = pd.to_numeric(df_copy["spend"], errors = "coerce")
    df_copy = df_copy.dropna(subset=["cloud","year_month","spend"]) # drop rows with missing (previously invalid or missing) data
    df_copy = df_copy.sort_values(["cloud", "year_month"]).reset_index(drop=True) # uses cloud and year_month as indexes & getting rid of old numbering of rows

    return df_copy


def commitment_data_validation(df):
    required_columns = ["cloud", "period_start", "period_end", "commitment"]
    # Check for missing columns, report if any
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"The following columns are missing in commitment data: {missing_columns}")

    # Change to desired data types, clean, and re-index
    df_copy = df.copy()
    df_copy["period_start"] = pd.to_datetime(df_copy["period_start"], format="%Y-%m", errors="coerce") 
    df_copy["period_end"] = pd.to_datetime(df_copy["period_end"], format="%Y-%m", errors="coerce") 
    df_copy["commitment"] = pd.to_numeric(df_copy["commitment"], errors = "coerce")
    df_copy = df_copy.dropna(subset=["cloud", "period_start", "period_end", "commitment"]) 
    df_copy = df_copy.sort_values(["cloud", "period_start"]).reset_index(drop=True) 

    return df_copy
