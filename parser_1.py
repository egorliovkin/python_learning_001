def getNums(acc: str, xs:str):
    if xs == '':
        return (acc,xs)
    elif xs[0].isdigit():
        return getNums(acc+xs[0],xs[1:])
    else:
        return (acc,xs)

def parser(xs):
    if xs == '\n' or xs == '':
        return ''
    else:
        a = xs[0]
        (b, c) = getNums("",xs[1:])    
        return a*int(b)+parser(c)

with open("/home/egorlevkin/Downloads/dataset_3363_2.txt") as inf:
    print(parser(inf.readline()))