import random
words = ["baldan","purew","unah","mashin","bagsh","suga","us","jalga"]

def RandomWord(arg):
    x = random.randint(0,len(arg)-1)
    word = arg[x]
    return word
    

def check_letter(arg,arg2):
    letter = ''
    for i in arg:
        if i in arg2:
            letter += i
        else:
            letter+="_"

       
    return letter


def display_print():
    letter = RandomWord(words)
    word = ""
    user_word = []
    check_letters = check_letter(letter,user_word)
    print(check_letters)
    temp = 5
    while temp>0:
        word = input("useg oruulan uu")
        user_word.append(word)
        check_letters = check_letter(letter,user_word)
        print(check_letters)
        temp-=1
    print("game over")
    

display_print()
