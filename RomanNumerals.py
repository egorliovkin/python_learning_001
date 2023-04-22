class RomanNumerals:
    rn = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    def to_roman(val):
        base = buff = val
        result = ''
        rn2 = dict(sorted(RomanNumerals.rn.items(), key=lambda item: item[1], reverse = True))
        for key in rn2:
            base = buff // rn2[key]
            if buff > 0:
                result += key * base
                buff -= RomanNumerals.rn[key] * base
        return result


    def from_roman(roman_num):
        import re
        result = 0
        buff = roman_num
        for key in RomanNumerals.rn.keys():
           for m in re.finditer(key, buff):               
            result += RomanNumerals.rn[key]
            buff = buff[:m.regs[0][0]] + buff[m.regs[0][1]:]
        return result
        

print(RomanNumerals.to_roman(2022))
print(RomanNumerals.from_roman('MMXXII'))