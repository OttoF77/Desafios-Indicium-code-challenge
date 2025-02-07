from airflow import DAG  # required to implement the airflow workflow
from airflow.operators.bash import (
    BashOperator,
)  # to implement shell commands as airflow tasks
from datetime import (
    datetime,
    timedelta,
)  # for manipulating date, time and calculating time intervals

# Setting the default DAG for data extraction
with DAG(
    dag_id="csv_extract_dag",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["meltano", "csv"],
) as dag:  # Creating a new instance for extracting the csv file
    csv_extract = BashOperator(
        task_id="csv_extract_task",
        bash_command="meltano elt tap-csv target-json1",
    )

    csv_extract  # Running the task