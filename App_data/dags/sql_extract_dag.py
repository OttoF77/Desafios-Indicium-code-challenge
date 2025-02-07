from airflow import DAG  # required to implement the airflow workflow
from airflow.operators.bash import (
    BashOperator,
)  # to implement shell commands as airflow tasks
from datetime import (
    datetime,
    timedelta,
)  # for manipulating date, time and calculating time intervals

# Defines default arguments for DAG tasks
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Setting the default DAG for data extraction
with DAG(
    dag_id="sql_extract_dag",
    default_args=default_args,
    description="PostgreSQL data extraction DAG",
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=["meltano", "postgres"],
) as dag:
    postgres_extract = BashOperator(
        task_id="postgres_extract_task",
        bash_command="meltano run tap-postgres target-jsonl",
    )

    postgres_extract  # Running the task
