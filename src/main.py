from src.read_data import load_airports
from src.explore_schema import print_schema
from src.basic_stats import print_basic_stats
from src.missing_values import print_missing_values

DATA_PATH = "data/raw/vega-data/airports.csv"

def main():
    df = load_airports(DATA_PATH)
    print_schema(df)
    print_basic_stats(df)
    print_missing_values(df)

if __name__ == "__main__":
    main()
