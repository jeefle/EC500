import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_airports(conn, airports):
    sql = ''' INSERT INTO airports(name, code)
              VALUES(?, ?, ?) '''

    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_data(conn, data):
    sql = ''' INSERT INTO tasks(code, lat, lon, city, state, country, woeid, tz, phone, email, url, runway_length,
                                elev, icao, direct_flights, carriers)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "/Users/jleong/Desktop/EC500/airports.db"
 
    sql_create_airports_table = """ CREATE TABLE IF NOT EXISTS airports (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        code text NOT NULL
                                    ); """
 
    sql_create_data_table = """CREATE TABLE IF NOT EXISTS data (
                                    id integer PRIMARY KEY,
                                    code text NOT NULL,
                                    lat text NOT NULL,
                                    lon text NOT NULL,
                                    city text NOT NULL,
                                    state text NOT NULL,
                                    country text NOT NULL,
                                    woeid text NOT NULL,
                                    tz text NOT NULL,
                                    phone text,
                                    email text,
                                    url text,
                                    runway_length text NOT NULL,
                                    elev text NOT NULL,
                                    icao text NOT NULL,
                                    direct_flights text NOT NULL,
                                    carriers text NOT NULL,
                                    FOREIGN KEY (code) REFERENCES airports (id)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_airports_table)
        # create tasks table
        create_table(conn, sql_create_data_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
