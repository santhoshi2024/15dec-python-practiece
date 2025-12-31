#caluculate the total average height of a class:

height = input('Enter your height in meters:')

height_count = height.split()
print(height.split())
count = 0
for height in height_count:
    count = count + 1
print(count)
for i in range(count):
  height_count[i] = int(height_count[i])
#without using inbuilt function:
total = 0
for xyz in height_count:
  total += xyz
avg = total/count
print("Average height is:",round(avg))

#print('height_count')
