import psycopg2

# Connect to PostgreSQL
def get_connection():
    conn = psycopg2.connect(
        host="localhost",          # your host
        database="survey_db",      # your database
        user="postgres",           # your PostgreSQL username
        password="iloveGOD55,",    # your password
        port=5433                  # <-- updated port
    )
    return conn

# Insert survey response
def insert_response(responses):
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO survey_responses 
    (name, age, gender, employment_status, industry, education, enjoys_python)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (
        responses['name'],
        int(responses['age']),
        responses['gender'],
        responses['employment_status'],
        responses['industry'],
        responses['education'],
        responses['enjoys_python']
    ))

    conn.commit()
    cursor.close()
    conn.close()
