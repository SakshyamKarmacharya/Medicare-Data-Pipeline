Medicare Data Pipeline is a project that automates the extraction, transformation, and loading (ETL) of U.S. Medicare data. The pipeline reads raw healthcare data from a CSV file, processes and cleans it, and loads the structured data into a PostgreSQL database for storage and analysis.

The entire ETL process is orchestrated using Apache Airflow, allowing for scheduled and repeatable data workflows. To ensure consistent deployment across different environments, all components—including Airflow, PostgreSQL, and ETL scripts—are containerized using Docker.

This project is designed to simulate real-world healthcare data workflows and can be extended for use cases such as cost analysis, fraud detection, and health service optimization. It demonstrates core data engineering skills including pipeline automation, workflow management, database integration, and containerization.
