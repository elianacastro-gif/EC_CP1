#EC 1st string methods notes

subject = "computer programming"

print(subject.upper())

print(subject.center(100))

#stupid/idiot proofing inputs
color = input ("what is your favorite color?").strip().lower()
# lower() => all lower case
# upper() => all upper case
# capitalize() => capitalize first letter of first word
# title() => capitalizes the first letter of each word
full_name = input("what is your full name?").strip().title()
print("that is cool " + full_name +". I like " + color + "too!")
print("that is cool {full_name}. I like {color} too!". format(full_name+full_name, color+color))

#f_string
print(f"that is cool {full_name}. I like {color} too")

pi = "3.14159"
#print(f "we all know pi is equal to {pi:.3f}
#print(pi.isdecimal())

sentence ="the quick brown fox jumps over the lazy dog"
word = "jumps"
print(sentence.find(word))
start = sentence.index("lazy")
length = len("lazy")
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)
print