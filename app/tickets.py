def migrating_it_tickets(conn):
        data = pd.read_csv('DATA/it_tickets.csv')
        data.to_sql('it_tickets', conn)