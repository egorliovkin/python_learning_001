def generate_hashtag(s):
    #your code here
    if len(s) == 0:
        return False
    else:
        res = '#'+''.join([xs.capitalize() for xs in s.split()])
        if len(res) > 140:
            return False
        else:
            return res


print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('      Codewars'))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CoDeWaRs is niCe'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag(''))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))