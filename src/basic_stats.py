def print_basic_stats(df):
    numeric_df = df.select_dtypes(include="number")
    print("\n=== DESCRIPTIVE STATS ===")
    print(numeric_df.describe())
