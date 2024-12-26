from Addresses.Repository.AddressRepo import get_write_db_connection

file_path = 'Addresses/Repository/input_data.csv'

def loadAddressData():
    with get_write_db_connection() as connection:
        drop_table(connection)
        load_data_from_csv(connection)
        print("Address data loaded")


def drop_table(connection):
    connection.execute(f"""
    DROP TABLE IF EXISTS addresses
    """)


def load_data_from_csv(connection):
    connection.execute(f"""
    CREATE TABLE addresses AS 
    SELECT * FROM read_csv_auto('{file_path}')
    """)
