a=int(input())
mi=0
ma=0
k=0
kmima=0
while a!=0:
    if (mi==0 or ma==0) and a%7!=0:
        mi=a
        ma=a
        k+=1
    if a%7!=0:
        if a<mi:
            mi=a
        if a>ma:
            ma=a
    a=int(input())
if k!=0:
    print('Минимальное:', mi)
    print('Максимальное:', ma)
else:
    print('Нет')