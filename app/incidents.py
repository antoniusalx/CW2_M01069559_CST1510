import pandas as pd


def migrating_cyber_incidents(conn):
        data = pd.read_csv('DATA/cyber_incidents.csv')
        data.to_sql('cyber_incidents', conn, if_exists='replace', index=False)
        return data