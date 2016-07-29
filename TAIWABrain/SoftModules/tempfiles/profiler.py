from tinydb import TinyDB, Query
db = TinyDB('dataBase.json')
Usr = Query()
query = raw_input('Enter the query element: ')
result = db.search(Usr.User == query)
print result
