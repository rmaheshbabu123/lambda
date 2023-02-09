import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="your-rds-instance-endpoint",
    database="your-database-name",
    user="your-database-user",
    password="your-database-password"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query to retrieve the list of users
cur.execute("SELECT usename FROM pg_user")

# Fetch the results of the query
rows = cur.fetchall()

# Print the list of users
print("List of Users:")
for row in rows:
    print(row[0])

# Close the cursor and connection
cur.close()
conn.close()
