correct_login='enot12345'
correct_password='12345'
login='a'
password='a'
da=0
while da!=3:
    login = input("Введите логин:")
    password = input('Введите пароль:')
    if login==correct_login and password==correct_password:
        print("Вы успешно вошли в аккаунт")
        break
    elif:
        da+=1
        print('Попробуйте ещё раз')
if da == 3:
    print('Попробуйте через пол часа')

print('Введите 7 целых чисел:')
s1=[]
for i in range(7):#первое использование цикла
    a=int(input())
    s1.append(a)
s2=[]
for i in s1:#второе использование цикла
    if i % 2==0:
        s2.append(i)
print("Все чётные числа котрые вы ввели ранее:", s2)

