import string
def minion_game(string):
    string = input("Enter a word:")

    vowels = "AEIOU"
    kevin_score = stuart_score = 0
    length = len(string)
    # list(range(length))
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length-i
        else:
            stuart_score += length-i

    if stuart_score>kevin_score:
        print(f'Stuart {stuart_score}')
    elif kevin_score>stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print("Draw")

minion_game(string)

