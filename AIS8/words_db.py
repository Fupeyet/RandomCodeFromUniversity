import shelve
db = shelve.open('db_file')
db['earth']='земля'
db['word']='слово'
db['catch']='ловить'
db['find']='искать'
db.close()