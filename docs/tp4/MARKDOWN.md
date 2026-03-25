## 🚀 TP 4 — CI/CD, Monitoring & Deployment

The final step was to automate test execution and monitor pipeline performance on every run.

### Key Achievements
* **Continuous Integration (CI):** Configured **GitHub Actions** (`.github/workflows/ci.yml`). On every `git push`, a virtual environment is spun up to verify code formatting (`flake8`) and run the test suite (`pytest`).
* **Monitoring:** Created a module (`src/monitoring.py`) to track execution time, step status, and the volume of rows processed at each stage of the pipeline.
* **Report Generation:** Automatically outputs a `pipeline_report.json` file at the end of each ELT run.

### Pipeline Execution Results

Here is an example of the generated report after a complete end-to-end run (Extract ➔ Transform ➔ Gold):

```json
{
  "pipeline_name": "KICKZ EMPIRE ELT",
  "run_id": "2026-03-25T14:37:47.063083+00:00",
  "steps": [
    {
      "step_name": "extract",
      "status": "success",
      "start_time": "2026-03-25T14:37:47.063094+00:00",
      "end_time": "2026-03-25T14:39:42.986599+00:00",
      "duration_seconds": 115.92,
      "rows_processed": 600155,
      "tables_created": [
        "products",
        "users",
        "orders",
        "order_line_items",
        "reviews",
        "clickstream"
      ],
      "errors": []
    },
    {
      "step_name": "transform",
      "status": "success",
      "start_time": "2026-03-25T14:39:42.986656+00:00",
      "end_time": "2026-03-25T14:39:55.927988+00:00",
      "duration_seconds": 12.94,
      "rows_processed": 53184,
      "tables_created": [
        "dim_products",
        "dim_users",
        "fct_orders",
        "fct_order_lines"
      ],
      "errors": []
    },
    {
      "step_name": "gold",
      "status": "success",
      "start_time": "2026-03-25T14:39:55.928017+00:00",
      "end_time": "2026-03-25T14:40:03.022234+00:00",
      "duration_seconds": 7.09,
      "rows_processed": 0,
      "tables_created": [],
      "errors": []
    }
  ]
}
```