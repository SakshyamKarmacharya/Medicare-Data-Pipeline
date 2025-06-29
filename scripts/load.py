import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def load_data():
    df = pd.read_csv("data/transformed.csv")
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/healthcare')
    df.to_sql('claims_data', engine, if_exists='replace', index=False)
