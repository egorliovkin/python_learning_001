def get_pins(observed):
    xss = {'1': ['1', '2', '4'],
           '2': ['2', '1', '3', '5'],
           '3': ['3', '2', '6'],
           '4': ['4', '1', '5', '7'],
           '5': ['5', '2', '4', '6', '8'],
           '6': ['6', '3', '5', '9'],
           '7': ['7', '4', '8'],
           '8': ['8', '5', '7', '9', '0'],
           '9': ['9','6','8'],
           '0': ['0','8']}
    xs = [[""],[""],[""],[""],[""],[""],[""],[""]]
    for i in range(len(observed)):
        xs[i] = xss[observed[i]]
    ys = [x1+x2+x3+x4+x5+x6+x7+x8
          for x1 in xs[0]
          for x2 in xs[1]
          for x3 in xs[2]
          for x4 in xs[3]
          for x5 in xs[4]
          for x6 in xs[5]
          for x7 in xs[6]
          for x8 in xs[7]]
    return ys

print(get_pins('11'))
