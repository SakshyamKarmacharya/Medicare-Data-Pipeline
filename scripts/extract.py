import pandas as pd

def extract_data():
    # Full absolute path inside the container
    input_path = "/opt/airflow/data/Medicare_2019.csv"
    output_path = "/opt/airflow/data/extracted.csv"

    df = pd.read_csv(input_path, dtype=str)
    df.to_csv(output_path, index=False)
    print(f"Extracted {len(df)} rows.")
