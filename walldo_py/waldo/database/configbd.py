from pymongo import MongoClient
import urllib.parse

bd_user = urllib.parse.quote_plus('root')
bd_pass = urllib.parse.quote_plus('patata')
host = "10.35.192.34"
database = "pruebas"


client = MongoClient('mongodb://%s:%s@%s' % (bd_user, bd_pass, host))
db = client[database]