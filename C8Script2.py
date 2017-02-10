import random, string

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = string.ascii_lowercase

lecture_input_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
lecture_input_2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
lecture_input_3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

print(lecture_input_1, lecture_input_2, lecture_input_3)

def generator():
    if lecture_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif lecture_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif lecture_input_1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = lecture_input_1


    if lecture_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif lecture_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif lecture_input_2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = lecture_input_2

    if lecture_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif lecture_input_3 == 'c':
        letter3 = random.choice(consonants)
    elif lecture_input_3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = lecture_input_3

    name = letter1 + letter2 + letter3
    return name

for i in range(20):
    print(generator())
