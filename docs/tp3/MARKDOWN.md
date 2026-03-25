## 🧪 TP 3 — Unit Testing, Logging & Data Quality

In this phase, we secured the data transformations and made the pipeline observable.

### Key Achievements
* **Unit Testing:** Implemented `pytest` to test extraction and transformation functions in isolation.
* **Mocking:** Utilized `unittest.mock` and fixtures to simulate PostgreSQL database data without requiring a live connection.
* **Structured Logging:** Replaced standard `print()` statements with a JSON-formatted logger (`src/logger.py`), enabling better traceability in production environments.
* **Error Handling:** Implemented `try/except` blocks to ensure that a single faulty row or connection issue does not crash the entire pipeline.

### Test Coverage Report

We aimed for optimal code coverage, particularly focusing on the critical data transformation functions (Silver layer). 

<img src=".\test_coverage.jpg" alt="Coverage test results" width="75%" />

**Analysis of Results:**
* **Target Reached:** We successfully exceeded the >=80% coverage target for the core business logic in `src/transform.py`, achieving **82%**. This ensures that edge cases, NULL values, and PII removal are thoroughly validated.
* `src/logger.py` is nearly fully covered at **94%**.
* The overall pipeline coverage stands at **61%**. Future improvements would include adding integration tests for the `monitoring.py` and `database.py` modules to raise the global coverage score.