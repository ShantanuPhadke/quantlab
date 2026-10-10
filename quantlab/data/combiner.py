def combine_dataframes(df1, df2, on_column):
    return df1.merge(df2, on=on_column, how="outer")
