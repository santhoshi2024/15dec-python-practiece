import random
print("WELCOME TO HANGMAN GAME")
list = ["apple", "beautiful" , "cat", "domain", "elephant" , "fish","grapes"]

word = random.choice(list)
print(word)
display = []
for letters in range(len(word)):
    display += "_"
print(display)


lives = 6
game_over = False
while  not game_over :
    guess = input("Guess a letter: ").lower()

    for position in range(len(word)):
        letter = word[position]
        if guess == letter:
            display[position] = letter   
            print(display)   
    if guess not in word:
        lives -=1
        if lives == 0:
            game_over == True
            print("**YOU LOSE**")
    if '_' not in display:
        game_over = True
        print("**YOU WIN**\n WINNER WINNER CHICKEN DINNER")
        

