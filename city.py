a = input().upper()
b = input().upper()
if a[-1] == "Ь":
    if a[-2] == b[0]:
        print("Good")
    else:
        print("Bad")
elif a[-1] == b[0]:
    print("Good")
else:
    print("Bad")