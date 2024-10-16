#!/bin/sh
# wait-for-it.sh

set -e

host="$1"
shift
cmd="$@"

python << END
import sys
import time
import psycopg2

def wait_for_db(host, max_retries=30, delay_seconds=1):
    retries = 0
    while retries < max_retries:
        try:
            conn = psycopg2.connect(
                dbname="${POSTGRES_DB}",
                user="${POSTGRES_USER}",
                password="${POSTGRES_PASSWORD}",
                host="${host}",
                port="5432"
            )
            conn.close()
            print("Database is ready!")
            sys.exit(0)
        except psycopg2.OperationalError:
            retries += 1
            print(f"Waiting for database... (attempt {retries}/{max_retries})")
            time.sleep(delay_seconds)
    
    print("Could not connect to database after maximum retries")
    sys.exit(1)

wait_for_db("${host}")
END

# If the Python script exits successfully, run the command
exec $cmd