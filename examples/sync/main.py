import libsql
import os

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("local.db", sync_url=url, auth_token=auth_token)
conn.sync()

cur = conn.cursor()

conn.execute("DROP TABLE IF EXISTS users;")
conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT);")
conn.execute("INSERT INTO users VALUES ('first@example.com');")
conn.execute("INSERT INTO users VALUES ('second@example.com');")
conn.execute("INSERT INTO users VALUES ('third@example.com');")


print(conn.execute("select * from users").fetchall())
