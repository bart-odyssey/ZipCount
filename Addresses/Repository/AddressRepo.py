import duckdb

databaseConnectionString = "Addresses/Repository/ZipCount.db"

def get_read_db_connection() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(databaseConnectionString, read_only=True)

def get_write_db_connection()-> duckdb.DuckDBPyConnection:
    return duckdb.connect(databaseConnectionString)

def count_addresses_by_postal_code(postal_code: str):
    with get_read_db_connection() as connection:
        result = connection.execute("SELECT COUNT(*) FROM addresses WHERE PC = ?", (postal_code,)).fetchone()[0]
    return result