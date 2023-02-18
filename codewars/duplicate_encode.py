def duplicate_encode(word):
    # fs = lambda ch, xs: len([x for x in xs if x == ch])
    # return ''.join('(' if fs(x,word.upper()) == 1 else ')' for x in word.upper())
    return ''.join('(' if word.upper().count(x) == 1 else ')' for x in word.upper())

print(duplicate_encode("din"),"(((")
print(duplicate_encode("recede"),"()()()")
print(duplicate_encode("Success"),")())())","should ignore case")
print(duplicate_encode("(( @"),"))((")  