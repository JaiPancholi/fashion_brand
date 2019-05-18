import psycopg2, psycopg2.extras
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def make_connection():
	conn = psycopg2.connect(
			host = os.environ.get('DB_HOST'),
			database = os.environ.get('DB_NAME'),
			user = os.environ.get('DB_USER'),
			password = os.environ.get('DB_PASSWORD')
		)

	cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

	return conn, cur

def fetch(SQL):
	conn, cur = make_connection()
	cur.execute(SQL)
	records = cur.fetchall()
	conn.close()
	return records

def commit(SQL, data):
	conn, cur = make_connection()
	cur.execute(SQL, data)
	conn.commit()
	conn.close()
	return 0
