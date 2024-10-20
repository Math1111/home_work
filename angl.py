from random import choice
s=[]
level=1
point = 0
qwestions={
    1:[('запрещать', "forbid forbade forbidden"), ("находить", "find found found"), ("прощать", "forgive forgave forgiven"),
       ("замораживать", "freeze froze frozen"), ("висеть", "hang hung hung"), ("ударять, попадать", "hit hit hit"),
       ("держать", "hold held held"), ("причинять боль", "hurt hurt hurt"), ("сохранять", "keep kept kept"),
       ("слышать", "hear heard heard"), ("расти", "grow grew grown"), ("копать", "dig dug dug"),
       ("вести дела", "deal dealt dealt"), ("выбирать", "choose chose chosen"), ("взрываться", "burst burst burst"),
       ("приносить", "bring brought brought"), ("кусать", "bite bit bitten"), ("бить", "beat beat beaten"),
       ("рожать, переносить", "bear bore born")]}
for i in range(35):
    qwestion, corect_answer = choice(qwestions[level])
    print(f'{qwestion}')
    student_answer=input().lower()
    if student_answer == corect_answer.lower():
        print("Молодец, правильно!")
        point+=1
    else:
        print(f"Не правильно! Правильный ответ: {corect_answer}")
        s.append(qwestion)
print(f"Правильно - {point}")
if point != 35:
    print("Не правильно:", s)