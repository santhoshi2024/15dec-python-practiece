for numbers in range(0,51):
    
    
#numbers_list = number.split( )
    if numbers % 3 == 0 and numbers %5 == 0:
        print('fizzbuzz')
    elif numbers % 3 == 0:
        print('fizz')
    elif numbers % 5 == 0:
        print('buzz')
    else:
        print(numbers)