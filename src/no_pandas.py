import csv
from collections import defaultdict
from math import sqrt

DATA_PATH = "data/raw/vega-data/airports.csv"
NUMERIC_THRESHOLD = 0.95  # ≥95% numeric → treat column as numeric
MISSING_TOKENS = {"", "na", "n/a", "none", "null"}


# -----------------------------
# DATA LOADING (ARRAY OF DICTS)
# -----------------------------
def load_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# -----------------------------
# SCHEMA EXPLORATION
# -----------------------------
def print_schema(rows):
    if not rows:
        return

    columns = list(rows[0].keys())
    types = {}

    for col in columns:
        for row in rows:
            val = row[col].strip()
            if val != "":
                types[col] = infer_type(val)
                break
        else:
            types[col] = "unknown"

    print("=== COLUMNS ===")
    print(columns)

    print("\n=== DATA TYPES (INFERRED) ===")
    for col in columns:
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


# -----------------------------
# MISSING VALUES
# -----------------------------

def is_missing(val):
    return val.strip().lower() in MISSING_TOKENS

def print_missing_values(rows):
    missing = defaultdict(int)

    for row in rows:
        for col, val in row.items():
            if is_missing(val):
                missing[col] += 1

    print("\n=== MISSING VALUES ===")
    for col, count in sorted(missing.items(), key=lambda x: x[1], reverse=True):
        print(f"{col}: {count}")


# -----------------------------
# BASIC STATS (NUMERIC ONLY)
# -----------------------------
def print_basic_stats(rows):
    column_values = defaultdict(list)
    non_missing_counts = defaultdict(int)

    # First pass: collect numeric candidates
    for row in rows:
        for col, val in row.items():
            val = val.strip()
            if val == "":
                continue

            non_missing_counts[col] += 1
            try:
                column_values[col].append(float(val))
            except ValueError:
                pass

    print("\n=== DESCRIPTIVE STATS ===")

    for col in sorted(column_values.keys()):
        numeric_count = len(column_values[col])
        total_count = non_missing_counts[col]

        # Apply numeric threshold rule
        if total_count == 0:
            continue

        if numeric_count / total_count < NUMERIC_THRESHOLD:
            continue

        values = column_values[col]

        count = len(values)
        mean = sum(values) / count
        min_v = min(values)
        max_v = max(values)
        std = sqrt(sum((x - mean) ** 2 for x in values) / count)

        print(f"\n{col}")
        print(f"  count: {count}")
        print(f"  mean : {mean:.4f}")
        print(f"  std  : {std:.4f}")
        print(f"  min  : {min_v}")
        print(f"  max  : {max_v}")


# -----------------------------
# ENTRY POINT (ORCHESTRATION)
# -----------------------------
def main():
    rows = load_csv(DATA_PATH)
    print_schema(rows)
    print_basic_stats(rows)
    print_missing_values(rows)


if __name__ == "__main__":
    main()
