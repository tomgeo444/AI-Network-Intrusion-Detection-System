from src.database.connection import get_connection

def get_user_by_email(email):
	connection=get_connection()
	cursor=connection.cursor()
	query = """
	Select * From users where email =%s """
	try:
	    cursor.execute(query,(email, ))
	    user=cursor.fetchone()
	    return user
	except Exception as e:
	    print(e)
	    return None
	finally:
	    cursor.close()
            connection.close()

