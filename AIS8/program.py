import shelve
db=shelve.open('db_file')

def eng():
    eng_words=dict([[v, k] for k,v in db.items()])
    find_word=input('Введите слово которое хотите найти ' '')
    print(eng_words.get(find_word) or print('Нет такого ключа'))

def rus():
    key=input('Введите слово ' '')
    print (db.get(key) or 'Искомое слово не найдено')

def newRecord():
    newkey=input('Ввести новое слово ' '')
    newvalue=input('Ввести перевод ' '')
    db[newkey] = newvalue
    db.update()
    db.close()
    
while __name__ == '__main__':
    start=input('Найти английский перевод русского слова? введите "1"(Если хотите найти перевод русского слова) или "2" (Если английского). Также можете ввести "3" для записи нового слова' '')
    if start == '1':
        eng()
    elif start == '2':
        rus()
    elif start == '3':
        newRecord()
    else:
        print('До встречи')