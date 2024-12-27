from app.Addresses.Repository.AddressRepo import get_write_db_connection

file_path = 'Addresses/Repository/input_data.csv'


def load_address_data():
    with get_write_db_connection() as connection:
        drop_table(connection)
        load_data_from_csv(connection)
        create_index(connection)
        print("Address data loaded")


def drop_table(connection):
    connection.execute("""
    DROP TABLE IF EXISTS addresses
    """)


def load_data_from_csv(connection):
    connection.execute(f"""
    CREATE TABLE addresses AS 
    SELECT * FROM read_csv_auto('{file_path}')
    """)

def create_index(connection):
    connection.execute("""
       CREATE INDEX addresses_PC_index ON addresses (PC);
       """)

