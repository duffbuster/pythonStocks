# utils.py
import stocks


DATABASE='stockTickers'
DB_USER = 'user'
DB_PASSWORD = 'password'
HOST = 'localhost'

def db_connect():
  return stocks.connect(HOST, DB_USER, DB_PASSWORD, DATABASE)