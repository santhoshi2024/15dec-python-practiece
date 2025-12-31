#find the maxmium number in the list
#do not use inbult function max use split,range,for loop

number = input("Enter the number separated by space")
numbers_list = number.split( )
count = 0
for num in numbers_list:
    count = count + 1
print(count)

for i in range(count):
  numbers_list[i] = int(numbers_list[i])
max_number = numbers_list[0]
for number in numbers_list:
   if number>max_number:
      max_number = number
print(f' The maximum number is {max_number}')

#range(0,xyz)


