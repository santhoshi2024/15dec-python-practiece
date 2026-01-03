import random
print('Welcome to Password Generator!')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
num_letters = int(input("how many letters would you like to add in your password?\n"))
num_symbols = int(input("how many symbols would you like to add in your password?\n"))
num_numbers = int(input("how many numbers would you like to add in your password?\n"))
password_list = []
for i in range(1,num_letters+1):
    password_letters = random.choice(letters)
    password_list += password_letters
for i in range(1,num_symbols+1):
    password_letters = random.choice(symbols)
    password_list +=password_letters
for i in range(1,num_numbers+1):
    password_letters = random.choice(numbers)
    password_list += password_letters 
random.shuffle(password_list)
password = ""
for a in password_list:
    password += a

print(password)
print(f"your password is:{password}")