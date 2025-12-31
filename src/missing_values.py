def print_missing_values(df):
    print("\n=== MISSING VALUES ===")
    print(df.isna().sum().sort_values(ascending=False))
