#assign variable tovowels and kelvin and stuart score
#iterate over a range 
#cummulative score using if else
#print scores

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Stuart_score = 0
    Kevin_score = 0
    s = len(string)
    
    for i in range(s):
        if string[i] in vowels:
            Kevin_score += s - i
        else:
            Stuart_score += s - i
    
    if Kevin_score > Stuart_score:
        print(f"Kevin {Kevin_score}")
    elif Stuart_score > Kevin_score:
        print(f"Stuart {Stuart_score}")
    else:
        print("Draw")
             

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
# For Example:
# string S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
# For better understanding, see the image below:

