


#alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
encrypt = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
total = ''


file = open("key.txt", "r")
file.write(int(encrypt))
key = file.read()



# lang = input('Выберите язык RU/EU: ')
# if lang == 'RU':
for i in message:
        space = alphabet.find(i)
        new_space = space + encrypt
        if i in alphabet:
            total += alphabet[new_space]
        else:
            total += i
# else:
#     for i in message:
#         space = alphabet.find(i)
#         new_space = space + encrypt
#         if i in alphabet:
#             total += alphabet[new_space] 
#         else:
#             total += i
print (total)

file.close()

print('Введите ключ:')
k2=input('')

file = open('key.txt', 'r')
k3 = file.read()
i=1
n =  ''
while k2 != k3:
    print('Ключ не верный. Попробуйте ещё раз.')
    k2=input('')
    i += 1
    if k2 == k3:
        print("Ключ верный, декодированный текст:")
        for c in total:
            n += alphabet[(alphabet.index(c)- key) % len(alphabet)]
if i == 1:
     print("Ключ верный, декодированный текст:")
     for c in total:
            n += alphabet[(alphabet.index(c)- key) % len(alphabet)]
print(n)
print('')
print('Количество попыток: ', i)

file.close()



