# Problem:  https://www.hackerrank.com/challenges/the-minion-game/problem
# Score: 40


def minion_game(string):
    s=string.strip()
    print(s)
    s_len=len(s)
    print(s_len)
    vowel = ["A", "E", "I", "O", "U"]
    kevin = 0
    stuart = 0
    for i in range (s_len):
        if string[i] in vowel:
            kevin += s_len - i
            print(kevin)
        else :
            stuart += s_len -i
            print(stuart)
            
    if kevin==stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin", kevin)    
    else:
        print("stuart",stuart)
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
