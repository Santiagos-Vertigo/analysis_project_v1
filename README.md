analysis_project_v1/
│
├── analysis-env/                 # Python virtual environment (DO NOT COMMIT)
│
├── data/
│   ├── raw/                      # Immutable source data (DO NOT MODIFY)
│   │   └── vega-data/
│   │       ├── airports.csv
│   │       ├── birdstrikes.csv
│   │       ├── annual-precip.json
│   │       └── ...
│   │
│   └── processed/                # Derived / cleaned outputs
│       └── analysis_v1/
│           ├── airports_clean.csv
│           └── summary_stats.csv
│
├── src/
│   ├── __init__.py
│   │
│   ├── main.py                   # ENTRY POINT (python -m src.main)
│   │
│   ├── io/                       # Data input/output layer
│   │   ├── __init__.py
│   │   ├── read_data.py          # load_airports(), load_csv(), etc.
│   │   └── write_data.py         # save_csv(), export_stats(), etc.
│   │
│   ├── analysis/                 # Analysis logic (pure functions)
│   │   ├── __init__.py
│   │   ├── schema.py             # print_schema()
│   │   ├── stats.py              # print_basic_stats()
│   │   └── missing.py            # print_missing_values()
│   │
│   ├── visualization/            # Optional plotting (still .py)
│   │   ├── __init__.py
│   │   └── plots.py              # matplotlib / seaborn functions
│   │
│   └── utils/                    # Shared helpers
│       ├── __init__.py
│       └── paths.py              # Centralized file paths
│
├── tests/                        # Unit tests (future)
│   ├── __init__.py
│   ├── test_read_data.py
│   └── test_stats.py
│
├── .gitignore
├── README.md
└── requirements.txt
