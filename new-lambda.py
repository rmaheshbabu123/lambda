import psycopg2

conn = psycopg2.connect(
    host="your-rds-instance-endpoint",
    database="your-database-name",
    user="your-database-user",
    password="your-database-password"
)

cursor = conn.cursor()

cursor.execute("SELECT usename FROM pg_catalog.pg_user")

users = cursor.fetchall()

for user in users:
    print(user[0])

cursor.close()
conn.close()
