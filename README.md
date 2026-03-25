# KICKZ EMPIRE — ELT Pipeline

ELT (Extract, Load, Transform) pipeline for the **KICKZ EMPIRE** e-commerce website, built as part of the IMT Data Engineering course.

## 🏗️ Architecture

```
S3 (CSV)  ──→  🥉 Bronze (raw)  ──→  🥈 Silver (clean)  ──→  🥇 Gold (analytics)
```

| Layer | Schema | Description |
|---|---|---|
| **Bronze** | `bronze_groupN` | Raw data — faithful copy of CSV files from S3 |
| **Silver** | `silver_groupN` | Cleaned data — internal columns removed, PII masked |
| **Gold** | `gold_groupN` | Aggregated data — ready for dashboards |

## 📁 Project Structure

```
├── docs/
│   ├── DATA_PRESENTATION.md    # KICKZ EMPIRE data presentation
│   └── tp1/
│       └── INSTRUCTIONS.md     # Step-by-step TP1 instructions
├── src/
│   ├── __init__.py
│   ├── database.py             # PostgreSQL connection (AWS RDS)
│   ├── extract.py              # Extract: S3 (CSV) → Bronze
│   ├── transform.py            # Transform: Bronze → Silver
│   └── gold.py                 # Gold: Silver → Gold (aggregations)
├── pipeline.py                 # ELT orchestrator
├── tests/                      # Tests (TP2)
├── .env.example                # Environment variables template
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

```bash
# 1. Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Configure with your credentials (DB + AWS)

# 2. Test the connection
python -m src.database

# 3. Run the pipeline (reads from S3 automatically)
python pipeline.py
```

## 📊 Datasets

| Dataset | Format | Source (S3) | Bronze Table |
|---|---|---|---|
| Product Catalog | CSV | `raw/catalog/products.csv` | `products` |
| Users | CSV | `raw/users/users.csv` | `users` |
| Orders | CSV | `raw/orders/orders.csv` | `orders` |
| Order Line Items | CSV | `raw/order_line_items/order_line_items.csv` | `order_line_items` |

## 📚 Documentation

- [Data Presentation](docs/DATA_PRESENTATION.md)
- [TP1 Instructions](docs/tp1/INSTRUCTIONS.md)
- [TP2 Instructions](docs/tp2/INSTRUCTIONS.md)
- [TP3 Instructions](docs/tp3/INSTRUCTIONS.md)
- [TP4 Instructions](docs/tp4/INSTRUCTIONS.md)

## ⚙️ Tech Stack

- **Python 3.10+** : Main language
- **pandas** : Data manipulation
- **boto3** : AWS S3 access
- **SQLAlchemy** : ORM / PostgreSQL connection
- **PostgreSQL** (AWS RDS) : Database
- **pytest** : Testing (TP2)

## 🧭 Business Context

KICKZ EMPIRE is an e-commerce platform that needs trustworthy analytics for operations and decision-making.
This ELT pipeline centralizes data from source files, standardizes quality in a layered warehouse model,
and exposes business-ready aggregates for dashboards (revenue, product performance, customer value).

## ▶️ Run Options

Run full pipeline:

```bash
python pipeline.py
```

Run a single step:

```bash
python pipeline.py --step extract
python pipeline.py --step transform
python pipeline.py --step gold
```

After execution, a monitoring report is generated in:

```text
pipeline_report.json
```

## 🧪 Testing

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

Run tests per module:

```bash
pytest tests/test_extract.py
pytest tests/test_transform.py
pytest tests/test_gold.py
```

## 👥 Team Members

- Khaoula AROUISSI
- Safaa MAHDIR
- Hajar SALAME

## 🛡️ Production Checklist

- [x] `.gitignore` includes `.env`, `__pycache__/`, `venv/`, `*.pyc`
- [x] `requirements.txt` uses pinned versions
- [x] README includes setup, run, test, and architecture sections
- [ ] Run formatter before release:

```bash
python -m black src pipeline.py
```

- [x] No hardcoded credentials should be committed
