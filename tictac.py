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

fh = lambda pair : (lambda x : x, lambda x : pair[1])
fv = lambda pair : (lambda y : pair[0], lambda y : y)
fr = lambda pair : (lambda x : x, lambda x : x - pair[0] + pair[1] )
fl = lambda pair : (lambda x : x, lambda x : pair[0] + pair[1] - x )

def check_win(x,y):
    ffh = fh((x,y))
    ffv = fv((x,y))
    ffr = fr((x,y))
    ffl = fl((x,y))
    ds = ([(ffh[0](x),ffh[1](x)) for x in range(matrix_size) if (ffr[0](x) != x or ffr[1](x) != y)],
          [(ffv[0](y),ffv[1](y)) for y in range(matrix_size) if (ffr[0](x) != x or ffr[1](x) != y)],
          [(ffr[0](x),ffr[1](x)) for x in range(matrix_size) if ((ffr[0](x) != x or ffr[1](x) != y) and (ffr[0](x) >= 0 and ffr[0](x) < matrix_size) and (ffr[1](x) >= 0 and ffr[1](x) < matrix_size))],
          [(ffl[0](x),ffl[1](x)) for x in range(matrix_size) if ((ffr[0](x) != x or ffr[1](x) != y) and (ffl[0](x) >= 0 and ffl[0](x) < matrix_size and ffl[1](x) >= 0 and ffl[1](x) < matrix_size))])

    for chs in ds:
        if len(chs) > 0:
            res = True
            for xy in chs:
                res = res and (xs[xy[1]][xy[0]] == xs[y][x])
            if res:
                return res
    return False

game_loop()