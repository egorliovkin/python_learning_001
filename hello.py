# print("Hello, World")
# for x in range(0, 20):
#     if (x != 0) & (x % 3 == 0):
#         print ("Bad day")
#     else:
#         print ("Good day")
# print("Goodbye, World")

# def hello(num, bad_text, good_text):
#     for x in range(0, num):
#         if (x != 0) & (x % 3 == 0):
#             print (bad_text)
#         else:
#             print (good_text)

# hello(20, "Bad day", "Good day")
# hello(7, "aaaa", "dddd")

def dec2bin(dec: int):
    if dec < 2:
        return str(dec)
    else:
        return dec2bin(dec // 2) + str(dec % 2)

def dec2bin_log(dec: int) -> str:
    import math
    biggest = math.floor(math.log(dec, 2))
    rest = dec
    result = ''
    for x in range(biggest, 0, -1):
        if (x == biggest):
            result += '1'
            rest = rest - pow(2, biggest)
            if rest > 0:
                biggest = math.floor(math.log(rest, 2))
        else:
            result += '0'
    return result + str(rest)

def dec2oct(dec: int):
    if dec < 8:
        return str(dec)
    else:
        return dec2oct(dec // 8) + str(dec % 8)

def dec2hex(dec: int):
    def hex_num(dec):
        if dec == 15:
            return 'F'
        elif dec == 14:
            return 'E'
        elif dec == 13:
            return 'D'
        elif dec == 12:
            return 'C'
        elif dec == 11:
            return 'B'
        elif dec == 10:
            return 'A'
        elif dec < 10:
            return str(dec)
    if dec < 16:
        return hex_num(dec)
    else:
        return dec2hex(dec // 16) + hex_num(dec % 16)

# print(dec2hex(64))
a = 10
b = 20.5 #dec2bin_log(20)
c = 13

# print(a)
# print(b)
# print(a+b)

def dec2bin_log_2(dec: int) -> str:
    import math
    x = biggest = math.floor(math.log(dec, 2))
    rest = dec
    result = ''
    while x > 0:
        if (x == biggest):
            result += '1'
            rest = rest - pow(2, biggest)
            if rest > 0:
                biggest = math.floor(math.log(rest, 2))
        else:
            result += '0'
        x -= 1
    return result + str(rest)

def dec2bin_log_3(dec: int) -> str:
    import math
    x = biggest = math.floor(math.log(dec, 2))
    rest = dec
    result = ''
    while x > 0:
        if (x == biggest):
            result += '1'
            rest = rest - pow(2, biggest)
            if rest > 0:
                biggest = math.floor(math.log(rest, 2))
        else:
            result += '0'
        x -= 1
    return result + str(rest)

# print(dec2bin_log_2(20))

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     # break
#     continue
#   print(x)

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# for x in range(1,6,1):
    # if x == 3:
    #     continue
    # print(x)

x = 0
while True:
    x += 1
    print(x)
    if x == 100:
        break