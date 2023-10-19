import psycopg2
import config

try:
    conn = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )
    with conn.cursor() as cursor:
        cursor.execute("SELECT cust_id from customer")
        print(cursor.fetchone())
except Exception as e:
    print("Error", e)
finally:
    if conn:
        conn.close()
        print("PostgresSQL closed")
