"""
Local Example: Using libSQL with a synced Turso database

This script demonstrates how to use libSQL with a local database file
that syncs with a remote Turso database.

Requirements:
- An existing database on Turso cloud.
- A `.env` file with your Turso database credentials.

Setup:
1. Create a new database with:
       turso db create <your_database_name>

2. Get your database URL:
       turso db show <your_database_name>

3. Create an auth token:
       turso db tokens create <your_database_name>

4. Add the URL and token to a `.env` file in your project root:
       TURSO_DATABASE_URL=<your_database_url>
       TURSO_AUTH_TOKEN=<your_auth_token>

"""

import libsql
import os
from dotenv import load_dotenv

load_dotenv()

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
