d = int(input())
x = y = 0
while d != 0:
    direct, distans = input().split()
    if direct == 'север':
        y += int(distans)
    elif direct == 'юг':
        y -= int(distans)
    elif direct == 'восток':
        x += int(distans)
    elif direct == 'запад':
        x -= int(distans)
    d -=1

print(f"{x} {y}")