import duckdb

# init / connect to database
conn = duckdb.connect('logger.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS cargo_log ()
''')