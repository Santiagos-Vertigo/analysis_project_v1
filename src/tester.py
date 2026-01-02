import csv
from collections import defaultdict
from math import sqrt

DATA_PATH = "data/raw/vega-data/airports.csv"
NUMERIC_THRESHOLD = 0.95  # ≥95% numeric → treat column as numeric
MISSING_TOKENS = {"", "na", "n/a", "none", "null"}

# Data Loading
def load_csv(path):
    rows = []
    with open(path, newline= "", encoding="utf-8") as f:
        reader  = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

# Schema Exploration
def print_schema(rows):
    if not rows:
        return
    
    colums = list(rows[0].keys())
    types = {}

    for col in colums:
        for row in rows:
            val = row[col].strip()
            if val != "":
                types[col] = infer_type(val)
                break
        else:
            types[col] = "unknown"
            
    print("=== Colums ===")
    print(colums)

    print("\n=== Data Types (Infered) ===")
    for col in colums:
        print(f"{col}: {types[col]}")

def infer_type(value):
    try:
        int(value)
        return "int"
    except ValueError:
        try:
            float(value)
            return "float"
        except ValueError:
            return "string"




# Missing Values
def is_missing(val):
    return val.strip().lower() in MISSING_TOKENS

def print_missing_values(rows):
    missing = defaultdict(int)

    for row in rows:
        for col, val in row.items():
            if is_missing(val):
                missing[col] += 1

    print("\n=== Is Missing Values ===")
    for col, count in sorted(missing.items, key=lambda x: x[1], reverse=True):
        print(f"{col}: {count}")

# Basic Stats
def print_basic_stats(rows):
    column_values = defaultdict(int)
    non_missing_counts = defaultdict(int)

    # first pass for numeric candidates
    for row in rows:
        for col, val in row.items():
            val = val.strip()
            if val == "":
                continue

            non_missing_counts += 1
            try:
                column_values[col].append(float(val))
            except ValueError:
                pass

    print("\n=== Descriptive Stats ===")

    for col in sorted(column_values.keys()):
        numeric_count = len(column_values[col])
        total_count = non_missing_counts[col]

        if total_count == 0:
            continue

        if numeric_count / total_count < NUMERIC_THRESHOLD:
            continue

        values = column_values[col]

        count = len(values)
        mean = sum(values) / count
        min_v = min(values)
        max_v = max(values)
        std = sqrt(sum((x - mean) ** 2 for x in values) /  count)

        print(f"\n{col}")
        print(f" count: {count}")
        print(f" mean: {mean}")
        print(f" std: {std}")
        print(f" min: {min_v}")   
        print(f" max: {max_v}")



# Entry Point (Orchestration)
def main():
    rows = load_csv(DATA_PATH)
    print_schema(rows)
    print_basic_stats(rows)
    print_missing_values(rows)


if __name__ == "__main__":
    main()
