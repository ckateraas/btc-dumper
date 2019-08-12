def get_database_file(arguments):
    if arguments.database:
        database_file = arguments.database
    else:
        fd, database_file = tempfile.mkstemp()
        os.close(fd)
    return database_file

def initialize(database):
    cursor = database.cursor()

    cursor.execute(
        """
        DROP TABLE IF EXISTS balance
        """
    )

    cursor.execute(
        """
        CREATE TABLE balance (
                address TEXT PRIMARY KEY,
                amount BIGINT NOT NULL,
                height BIGINT NOT NULL
        )
        """
    )
    return cursor

def add_address(address, amount, height, cursor):
    cursor.execute("""
        INSERT OR IGNORE INTO balance (amount, height, address) VALUES (?, ?, ?)
    """, (0, 0, address))

    cursor.execute("""
        UPDATE balance SET
        amount = amount + ?,
        height = ?
        WHERE address = ?
    """, (amount, height, address))

def fetch_addresses_from_database(cursor, arguments):
    if arguments.sort is None:
        select_expression = 'SELECT * FROM balance'
    elif arguments.sort == 'ASC':
        select_expression = 'SELECT * FROM balance ORDER BY amount ASC'
    elif arguments.sort == 'DESC':
        select_expression = 'SELECT * FROM balance ORDER BY amount DESC'
    else:
        select_expression = 'SELECT * FROM balance'

    cursor.execute(select_expression)
