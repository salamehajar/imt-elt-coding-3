"""
TP3 — Shared pytest fixtures
=============================
Fixtures are fake DataFrames that mimic Bronze data.
They are automatically injected into tests by pytest when a test parameter
has the same name as a fixture function.

Example:
    # This fixture is defined here:
    @pytest.fixture
    def sample_products(): ...

    # Any test with "sample_products" as a parameter receives it automatically:
    def test_something(self, sample_products):
        # sample_products is the DataFrame returned by the fixture above
"""

import pytest
import pandas as pd


@pytest.fixture
def sample_products():
    """Fake products DataFrame mimicking Bronze data."""
    return pd.DataFrame({
        "product_id": [1, 2, 3],
        "display_name": ["Nike Air Max", "Adidas Ultraboost", "Jordan 1"],
        "brand": ["Nike", "Adidas", "Jordan"],
        "category": ["sneakers", "sneakers", "sneakers"],
        "price_usd": [149.99, 179.99, -10.00],  # one invalid price for testing
        "tags": ["running|casual", "running|boost", "retro|hype"],
        "is_active": [1, 1, 0],
        "is_hype_product": [0, 0, 1],
        "_internal_cost_usd": [50.0, 60.0, 70.0],
        "_supplier_id": ["SUP001", "SUP002", "SUP003"],
    })


@pytest.fixture
def sample_users():
    """Fake users DataFrame mimicking Bronze data."""

    return pd.DataFrame({
        "user_id": [1, 2],
        "email": [" Alice@Example.COM ", "bob@test.com"],
        "first_name": ["Alice", "Bob"],
        "last_name": ["Martin", "Smith"],
        "loyalty_tier": ["gold", None],
        "_hashed_password": ["abc123", "def456"],
        "_last_ip": ["1.2.3.4", "5.6.7.8"],
        "_device_fingerprint": ["fp1", "fp2"],
    })


@pytest.fixture
def sample_orders():
    """Fake orders DataFrame mimicking Bronze data."""

    return pd.DataFrame({
        "order_id": [1, 2, 3],
        "user_id": [1, 2, 1],
        "order_date": ["2026-02-10", "2026-02-11", "2026-02-12"],
        "status": ["delivered", "shipped", "invalid_status"],
        "total_usd": [149.99, 179.99, 50.0],
        "coupon_code": ["SAVE10", None, None],
        "_stripe_charge_id": ["ch_1", "ch_2", "ch_3"],
        "_fraud_score": [0.1, 0.2, 0.9],
    })


# We add this fixture to have a coverage higher than 80% for the file transform.py

@pytest.fixture
def sample_order_lines():
    """Fake order lines DataFrame mimicking Bronze data."""
    return pd.DataFrame({
        "order_id": [1, 1],
        "product_id": [10, 11],
        "quantity": [2, 0],
        "unit_price_usd": [50.0, 100.0],
        "line_total_usd": [100.0, 0.0]
    })

# We add this fixture to have a higher coverage for the file extract.py
@pytest.fixture
def sample_reviews():
    """Fake reviews DataFrame mimicking Bronze data."""
    return pd.DataFrame({
        "review_id": [1, 2],
        "user_id": [1, 2],
        "product_id": [10, 11],
        "rating": [5, 3],
        "comment": ["Great product", "not bad"],
        "review_date": ["2026-02-10", "2026-03-11"]
    })

@pytest.fixture
def sample_gold_df():
    """Fake DataFrame mimicking a SQL aggregation result for Gold tests."""
    return pd.DataFrame({
        "metric_name": ["Metric A", "Metric B"],
        "value": [100.0, 250.5],
        "count": [10, 25]
    })