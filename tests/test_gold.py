"""
TP3 — Unit tests for src/gold.py
=====================================

These tests verify that Gold aggregations are correctly built and loaded,
without needing a real database connection.
"""

import pytest
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

class TestGoldErrorHandling:
    """
    Tests for error handling (Step 3).

    Here we use side_effect=Exception(...) to simulate a database failure.
    Instead of returning fake data, mock_read will RAISE an exception.
    We then verify with pytest.raises() that the exception is propagated.
    """

    @patch("src.gold._create_gold_table")
    @patch("src.gold.pd.read_sql", side_effect=Exception("Failed to read from DB"))
    def test_create_daily_revenue_propagates_error(self, mock_read, mock_load):
        with pytest.raises(Exception, match="Failed to read from DB"):
            create_daily_revenue()

    @patch("src.gold._create_gold_table")
    @patch("src.gold.pd.read_sql", side_effect=Exception("Failed to read from DB"))
    def test_create_product_performance_propagates_error(self, mock_read, mock_load):
        with pytest.raises(Exception, match="Failed to read from DB"):
            create_product_performance()

    @patch("src.gold._create_gold_table")
    @patch("src.gold.pd.read_sql", side_effect=Exception("Failed to read from DB"))
    def test_create_customer_ltv_propagates_error(self, mock_read, mock_load):
        with pytest.raises(Exception, match="Failed to read from DB"):
            create_customer_ltv()

    

