matrix_size = 3

def create_matrix(init, x_size, y_size):
    return [[init for y in range(y_size)] for x in range(x_size)]

def print_matrix(xs):
    [print(x) for x in xs]

xs = create_matrix(0, matrix_size, matrix_size)

def ask_first():
    print("Игрок 1 сделай ход, твою дивизию!")

def ask_second():
    print("Игрок 2 сделай ход, твою дивизию!")

def ask_X():
    print("Введи координату X от 0 до 2")

def ask_Y():
    print("Введи координату Y от 0 до 2")

def check(x,y):
    if xs[y][x] != 0:
        print("Поле занято!!! Жулик!")
        return False
    return True 

def check_win(x,y):
    if x == 1 and y == 1:
        return check_line_win(x,y) or check_line_diag1(x, y) or check_line_diag2(x, y)
    elif (x == 1 and (y == 0 or y == 2)) or (y == 1 and (x == 0 or x == 2)):
        return check_line_win(x,y)
    elif (x == 0 and y == 0) or (x == 2 and y == 2):
        return check_line_win(x,y) or check_line_diag1(x, y)
    else:
        return check_line_win(x,y) or check_line_diag2(x, y)

def check_line_win(x, y):
    res = True
    for nn in [0,1,2]:
        res = res and (xs[nn][x] == xs[y][x])
    if res:
        return True
    res = True
    for nn in [0,1,2]:
        res = res and (xs[y][nn] == xs[y][x])
    if res:
        return True
    return False

def check_line_diag1(x, y):
    res = True
    for nn in range(matrix_size):
        res = res and (xs[nn][nn] == xs[y][x])
    return res

def check_line_diag2(x, y):
    res = True
    for nn in range(matrix_size):
        res = res and (xs[2-nn][nn] == xs[y][x])
    return res

def game_loop():
    while True:
        x = 0
        y = 0
        while True:
            ask_first()
            ask_X()
            x = int(input())
            ask_Y()
            y = int(input())
            if check(x,y):
                break
        xs[y][x] = 1
        print_matrix(xs)
        if check_win(x,y) == True:
            print("Победил игрок 1!!!!!")
            exit(0)
        while True:
            ask_second()
            ask_X()
            x = int(input())
            ask_Y()
            y = int(input())
            if check(x,y):
                break
        xs[y][x] = 2
        print_matrix(xs)
        if check_win(x,y):
            print("Победил игрок 2!!!!!")
            exit(0)

game_loop()