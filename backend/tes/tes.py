import psycopg

dbname = "go-live-chat"
user = "root"
password = "root"
host = "localhost"
port = "5433"

conn = psycopg.connect(
    dbname=dbname, 
    user=user, 
    password=password, 
    host=host, 
    port=port,
    sslmode='disable'
    )

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SELECT query
query = "SELECT * FROM users"
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Process the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
