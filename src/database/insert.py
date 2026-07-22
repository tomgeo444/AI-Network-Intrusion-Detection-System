from src.database.connection import get_connection
def insert_user(username,email,password_hash,role):
    connection=get_connection()
    cursor=connection.cursor()
    query="""
	INSERT INTO users (username,email,password_hash,role)
	VALUES (%s,%s,%s,%s)
 	"""
    try:
	cursor.execute(query, (username,email,password_hash,role))
	connection.commit()
    except Exception as e:
	print(e)
    finally:
	cursor.close()
	connection.close()
