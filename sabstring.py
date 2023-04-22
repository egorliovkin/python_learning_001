def alphanumeric(password):
    import re
    return True if re.fullmatch(r'[A-Za-z0-9]+', password) else False

print(alphanumeric('AAA123'))
print(alphanumeric('1DwwD23'))
print(alphanumeric('123@1'))
print(alphanumeric('123$'))