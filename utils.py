# utils.py
import MySQLdb 


DATABASE='stockTickers'
DB_USER = 'user'
DB_PASSWORD = 'password'
HOST = 'localhost'

def db_connect():
  return MySQLdb.connect(HOST, DB_USER, DB_PASSWORD, DATABASE)
