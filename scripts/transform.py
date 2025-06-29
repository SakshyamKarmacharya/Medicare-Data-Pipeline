import pandas as pd

def transform_data():
    df = pd.read_csv("data/extracted.csv")
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df = df.dropna(subset=['provider_id', 'total_discharges'])
    df.to_csv("data/transformed.csv", index=False)
