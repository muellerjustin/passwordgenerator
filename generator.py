import random

text = ["q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Y", "X", "C", "V", "B", "N", "M"]
numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "%", "/", "(", ")", "=", "?", "*", "+", "#", "-", "_", ".", ":", ",", ";"]
all = ["q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Y", "X", "C", "V", "B", "N", "M", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "%", "/", "(", ")", "=", "?", "*", "+", "#", "-", "_", ".", ":", ",", ";"]
text_and_nums = ["q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Y", "X", "C", "V", "B", "N", "M", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def generate():
    digits = input("Digits: ")
    type = input("Text (t), numeric (n), text and nums (tn) or all (a)? ")

    if type == "t":
        password = ""
        for i in range(0, int(digits)):
            password += random.choice(text)

    elif type == "n":
        password = ""
        for i in range(0, int(digits)):
            password += random.choice(numeric)
    
    elif type == "a":
        password = ""
        for i in range(0, int(digits)):
            password += random.choice(all)

    elif type == "tn":
        password = ""
        for i in range(0, int(digits)):
            password += random.choice(text_and_nums)

    print(password)

generate()

