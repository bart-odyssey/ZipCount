import duckdb

def loadAddressData():
    # Specify the file path
    file_path = 'Adresses/Data/input_data.csv'

    # Database connection
    con = duckdb.connect("Adresses/Data/ZipCount.db")

    # Read the CSV and create a table
    con.execute(f"""
    DROP TABLE IF EXISTS addresses
    """)
    con.execute(f"""
    CREATE TABLE addresses AS 
    SELECT * FROM read_csv_auto('{file_path}')
    """)

    con.close()
    print("Data loaded")
