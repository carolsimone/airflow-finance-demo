from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

DBT = "/opt/dbt-venv/bin/dbt"
PROJECT = "/opt/dbt/finance"
COMMON = f"--project-dir {PROJECT} --profiles-dir {PROJECT}"

# finance runs at 03:00 — one hour after core, "because core is usually done by
# then". finance's scheduler has NO edge to core's. It fires whether core's run
# finished, failed, or renamed a column finance reads. That guess is the bug.
with DAG(
    dag_id="finance_daily",
    start_date=datetime(2026, 1, 1),
    schedule="0 3 * * *",
    catchup=False,
    tags=["finance"],
) as dag:
    seed = BashOperator(task_id="dbt_seed", bash_command=f"{DBT} seed {COMMON}")
    run = BashOperator(task_id="dbt_run", bash_command=f"{DBT} run {COMMON}")
    test = BashOperator(task_id="dbt_test", bash_command=f"{DBT} test {COMMON}")
    seed >> run >> test
