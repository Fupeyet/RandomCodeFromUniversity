print('Лабораторная работа №9')
print('Типы данных.')
print('')

a = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print('Введите ключ:')
k1 = int(input(''))

f = open('key.txt', 'w')
f.write(str(k1))
f.close()

print('')
print('Введите текст:')
tx = input().replace(' ', '')

res = ''
for c in tx:
    res += a[(a.index(c) + k1) % len(a)]
print('Закодированный текст:')
print(res)
print('')

print('Введите ключ:')
k2=input('')

f = open('key.txt', 'r')
k3 = f.read()

i=1

n =  ''
while k2 != k3:
    print('Ключ не верный. Попробуйте ещё раз.')
    k2=input('')
    i += 1
    if k2 == k3:
        print("Ключ верный, декодированный текст:")
        for c in res:
            n += a[(a.index(c) - k1) % len(a)]
if i == 1:
     print("Ключ верный, декодированный текст:")
     for c in res:
            n += a[(a.index(c) - k1) % len(a)]
print(n)
f.close
print('')
print('Количество попыток: ', i)
