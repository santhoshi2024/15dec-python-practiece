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
    if guess not in word:
        lives -=1
        if lives == 0:
            game_over == True
            print("you lose")
    if '_' not in display:
        game_over = True
        print("you win")

