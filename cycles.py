from random import randint
a=randint(1,10)
b=0
print("Угадайте число от одного до десяти")
while a!=b:
    b=int(input("Какае это число по вашему мнению:"))
    if a==b:
        print('Вы угадали!')
        break
    else:
        print("Попробуйте ещё раз")


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
    else:
        da+=1
        if da!=3:
            print('Попробуйте ещё раз')
if da == 3:
    print('Попробуйте через полчаса')


print('Введите 7 целых чисел:')
s1=[]
for i in range(7):
    a=int(input())
    s1.append(a)


s2=[]
for i in s1:
    if i % 2==0:
        s2.append(i)
print("Все чётные числа котрые вы ввели ранее:", s2)


print('Введите 5 чисел')
m=0
for i  in range(5):
    a=int(input())
    if a > m:
        m=a
print(f"{m}-наибольшее число из введённых")
