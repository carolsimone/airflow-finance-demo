FROM apache/airflow:2.10.5-python3.12
# dbt in an isolated venv so its pins never fight Airflow's own dependency set.
# Defaults are the authoritative continuo-demo pins; the build-arg override is for
# environments whose pip mirror lacks the beta. Never relax the pin upward.
ARG DBT_CORE_VERSION=1.12.0b1
ARG DBT_POSTGRES_VERSION=1.10.0
USER root
RUN python -m venv /opt/dbt-venv \
 && /opt/dbt-venv/bin/pip install --no-cache-dir \
      "dbt-core==${DBT_CORE_VERSION}" "dbt-postgres==${DBT_POSTGRES_VERSION}" \
 && chown -R airflow: /opt/dbt-venv
USER airflow
