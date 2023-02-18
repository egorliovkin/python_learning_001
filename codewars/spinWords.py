def spin_words(sentence):
    # Your code goes here
    return ' '.join([ x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words("Welcome") == "emocleW")
print(spin_words("to") == "to")
print(spin_words("CodeWars") =="sraWedoC")
print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")
print(spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes")