# analysis_project_v1

analysis_project_v1/
├── analysis-env/                  # Python virtual environment (IGNORED)
│
├── analysis_v1/                   # Analysis iteration v1
│   ├── notebooks/
│   │   └── 01_exploration.ipynb
│   │
│   └── scripts/
│       └── (future: clean_data.py, utils.py, etc.)
│
├── data/                          # Shared data layer
│   ├── raw/                       # Immutable source data (IGNORED)
│   │   └── vega-data/
│   │       ├── airports.csv
│   │       ├── flights-*.csv
│   │       └── ...
│   │
│   └── processed/                 # Derived outputs (IGNORED)
│       └── analysis_v1/
│           └── (generated files)
│
├── .gitignore                     # Git ignore rules (TRACKED)
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies (TRACKED)
