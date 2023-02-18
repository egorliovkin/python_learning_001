import random, math

a = random.randint(0, 1000) 
b = random.randint(0, 1000)
target = random.randint(min(a,b), max(a,b))
min_steps = math.floor(math.log((max(a,b)-min(a,b)),2))
guesstaken = 0
print(f"Введите одно число от {min(a,b)} до {max(a,b)}!")
print(f"Минимально возможное количество попыток - { min_steps }" )
while True:
    respond = int(input(), 10)
    if respond == target:
        print("Вы угадали!!!!")
        exit(0)
    elif respond < target:
        print("Недолёт!!!")    
    else:
        print("Перелёт!!!")
    guesstaken += 1

    print(f"Введите одно число от {min(a,b)} до {max(a,b)}!")
    print( f'осталось { min_steps - guesstaken } попыток)')
