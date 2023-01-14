xs = ["   *   ",
"  ***  ",
" ***** ",
"*******",
" ***** ",
"  ***  ",
"   *   "]

# def romb(shift, steps):
#     def max_aster_from_steps(steps):
#         if steps == 1:
#             return 1
#         else:
#             return max_aster_from_steps(steps - 1) + 2
#     x = 1
#     max_sym = max_aster_from_steps(steps)
#     while x <= max_sym:
#         print(" "*shift + " "*((max_sym - x) // 2) + "*"*(x))
#         x += 2
#     x = max_sym
#     while x > 2:
#         x -= 2
#         print(" "*shift + " "*((max_sym - x) // 2) + "*"*(x))

# def romb(shift, max_aster):
#     [print(" "*shift + " "*((max_aster - x) // 2) + "*"*(x)) for x in range(1,max_aster+1,2)]
#     [print(" "*shift + " "*((max_aster - x) // 2) + "*"*(x)) for x in range(max_aster-2,0,-2)]

# romb(0, 9)
def romb(shift, steps):
    def max_aster_from_steps(steps):
        if steps == 1:
            return 1
        else:
            return max_aster_from_steps(steps - 1) + 2
    max_aster = max_aster_from_steps(steps)
    [print(" "*shift + " "*((max_aster - x) // 2) + "*"*(x)) for x in range(1,max_aster+1,2)]
    [print(" "*shift + " "*((max_aster - x) // 2) + "*"*(x)) for x in range(max_aster-2,0,-2)]

# romb(0, 4)
shift = 0
while shift < 10:
    romb(shift,4)
    shift += 1
while shift > 0:
    romb(shift,4)
    shift -= 1