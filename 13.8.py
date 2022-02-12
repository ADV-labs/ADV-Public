billets = int(input('Введите количестово билеьов: ')) 
print(billets)
for i in range(billets+1):
    age = int(input('Ваш возраст: '))
    print(age)
    s = 990
    s1 = 1390
    s2 = 0
    if 18 < age <25:
        print(age(int('Ваш возраст: ')))
        print(s)
    elif 25 < age <99:
         print(int(age('Ваш возраст: ')))
         print(s1)
    elif 0 < age < 18:
         print(age(int('Dаш возраст: ')))
         print(s2) 
    else: 
        print('Неправельное указание возраста')
price = s + s1 + s2
print(price)