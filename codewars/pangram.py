def is_pangram(s):
    xs = [chr(x) for x in range(ord('A'),ord('Z'))]
    return set(xs).difference(set(s.upper())) == set()
    # return set(xs).intersection(set(s.upper())) == set(xs)

print(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)