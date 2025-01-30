import pandas as pd
import numpy as np


df = pd.read_csv(r"E:\\Yoobee\\MSE803-DA\Week 8\\House_Data.csv")


print("the first 5 rows of the dataframe:")
print(df.head())

print("Original Columns:", df.columns.tolist())


def clean_missing_values(df):
    # drop columns with more than 50% missing values
    threshold = len(df) * 0.5
    df_cleaned = df.dropna(thresh=threshold, axis=1)

    numeric_cols = df_cleaned.select_dtypes(include=np.number).columns
    categorical_cols = df_cleaned.select_dtypes(exclude=np.number).columns

    for col in numeric_cols:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())

    for col in categorical_cols:
        if df_cleaned[col].isnull().sum() > 0:
            mode_value = df_cleaned[col].mode()[0]
            df_cleaned[col] = df_cleaned[col].fillna(mode_value)

    return df_cleaned


def clean_outliers(df, threshold=3):
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        method = "iqr" if df[col].skew() > 1 else "zscore"

        print(f"Processing {col}..using {method} method.")
        if method == "iqr":
            # IQR
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower) & (df[col] <= upper)]
        elif method == "zscore":
            # Z-Score
            z_scores = (df[col] - df[col].mean()) / df[col].std()
            df = df[abs(z_scores) < threshold]

    return df


df_clean = df.copy()
df_cleaned = clean_missing_values(df_clean)
df = df_cleaned.drop_duplicates()  # remove duplicates
df = clean_outliers(df_cleaned)  # remove outliers

# save the cleaned data to a new csv file
df.to_csv(r"E:\\Yoobee\\MSE803-DA\Week 8\\House_Data_Clean.csv", index=False)
