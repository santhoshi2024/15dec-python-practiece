import random
list = ["apple", "beautiful" , "cat", "domain", "elephant" , "fish","grapes"]
word = random.choice(list)
print(word)
display = []
for letters in range(len(word)):
    display += "_"
print(display)

print("WELCOME TO HANGMAN GAME")
lives = 6
game_over = False
while  not game_over :
    guess = input("Guess a letter: ")

    for position in range(len(word)):
        letter = word[position]
        if guess == word:
            display[position] = letter      
    if guess_letter not in word:
        lives -=1
        


