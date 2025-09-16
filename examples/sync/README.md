# Sync Embedded Replica

This example demonstrates how to use libSQL with a synced database (local file synced with a remote Turso database).

## Install Dependencies

```bash
pip install python-dotenv
```

**Requirements:**
- An existing database on Turso cloud.
- A `.env` file with your Turso DB credentials.

Setup:
1. Create a new database with:
```bash
turso db create <your_database_name>
```
2. Get your database URL:
```bash
turso db show <your_database_name>
```
3. Create an auth token:
```bash
turso db tokens create <your_database_name>
```
4. Add the URL and token to a `.env` file in your project root:
```dotenv
TURSO_DATABASE_URL=<your_database_url>
TURSO_AUTH_TOKEN=<your_auth_token>
```
## Running

Execute the example:

```bash
python3 main.py
```

This will create a local database file that syncs with a remote database, insert some data, and query it.
