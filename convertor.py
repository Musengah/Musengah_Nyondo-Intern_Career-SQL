import pandas as pd
from sqlalchemy import create_engine

postgresql_username = 'postgres'
postgresql_password = ''
postgresql_host = 'localhost'
postgresql_database = 'spotify_data'

database_url = f'postgresql+psycopg2://{postgresql_username}:{postgresql_password}@{postgresql_host}/{postgresql_database}'
engine = create_engine(database_url)

csv_file_path = 'spotify-data.csv'

try:
    df = pd.read_csv(csv_file_path)
    table_name = 'music'
    df.to_sql(table_name, engine, index=False, if_exists='replace')
except Exception as e:
    print(f"Error: {e}")

engine.dispose()
