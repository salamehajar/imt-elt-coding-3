"""
TP3 — Unit tests for src/gold.py
=====================================

These tests verify that Gold aggregations are correctly built and loaded,
without needing a real database connection.
"""


from unittest.mock import patch

from src.gold import (
    create_daily_revenue,
    create_product_performance,
    create_customer_ltv
)

class TestCreateDailyRevenue:
    """Tests for create_daily_revenue()."""

    @patch("src.gold._create_gold_table")
    @patch("src.gold.pd.read_sql")
    def test_creates_and_loads(self, mock_read_sql, sample_gold_df):
        # On utilise la fixture sample_gold_df
        mock_read_sql.return_value = sample_gold_df

        create_daily_revenue()

        mock_read_sql.assert_called_once()


class TestCreateProductPerformance:
    """Tests for create_product_performance()."""

    @patch("src.gold._create_gold_table")
    @patch("src.gold.pd.read_sql")
    def test_creates_and_loads(self, mock_read_sql, sample_gold_df):
        mock_read_sql.return_value = sample_gold_df

        create_product_performance()

        mock_read_sql.assert_called_once()


class TestCreateCustomerLTV:
    """Tests for create_customer_ltv()."""

    @patch("src.gold._create_gold_table")
    @patch("src.gold.pd.read_sql")
    def test_creates_and_loads(self, mock_read_sql, sample_gold_df):
        mock_read_sql.return_value = sample_gold_df

        create_customer_ltv()

        mock_read_sql.assert_called_once()
