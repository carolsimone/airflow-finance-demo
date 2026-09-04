# airflow-finance-demo

finance team's downstream Airflow for the migration demo. Reads core's `revenue_per_user`.

It joins the external `analytics_net` network and shares core's warehouse, so **start `airflow-core-demo` first** — it owns the warehouse and the network.

Full walkthrough (before → break → after): [airflow-core-demo](https://github.com/carolsimone/airflow-core-demo).
