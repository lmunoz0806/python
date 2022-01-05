import psycopg2
print("Hello World!")

#Connect & Query PG Database
def get_connection():
    try:
        return psycopg2.connect(
            database="python",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
        
# GET THE CONNECTION OBJECT
conn = get_connection()
  
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")