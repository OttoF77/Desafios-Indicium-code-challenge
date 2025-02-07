# App_data Project

* Objective: The App_data project was based on the challenge proposed by the company Incidium and is a part of selection process for training in data engeniring.

* Development steps:

    1. Environment preparation:
        * Creation of the virtual environment through venv package;
        * Docker instalation;
        * Airflow instalation;
        * Meltano Instalation;
        * cloning the github repository.
        * Commit changes;
        Note: Due to the number of problems during the installation and preparation of Meltano, the folders generated during the testing phase following the official documentation were reused for extraction and loading of the challenge project.
    2. DAGs preparation;
        * Creating a dag to extract the csv file and load the log file;
        * Creating a dag to extract the postgreSQL file and load the log file;

    3. Sources:
        * Github:
            * https://hub.meltano.com/
            * github.com/emillysant/airflow_meltano/tree/main
        * Meltano: https://docs.meltano.com/
        * Airflow: https://airflow.apache.org/docs/apache-airflow/stable/start.html
        * Docker: https://docs.docker.com/get-docker/
        * Gemini: gemini.google.com
        * Youtube
        * Python.org: https://www.python.org/doc/
        * PostgreSQL: https://www.postgresql.

    Note: the current version is not complete, it is still missing the correct configuration of the tap-postgres extractor and the implementation of the rest of the DAGs. This challenge has been very exciting, due to the initial contact with many technologies that I did not know yet, such as: Meltano, Docker and Airflow.

