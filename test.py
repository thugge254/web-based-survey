import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",         # PostgreSQL host
        database="survey_db",     # Your database name
        user="postgres",     # Your PostgreSQL username
        password="iloveGOD55,", # Your password
        port=5433         # Default port
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Connection failed")
    print(e)
