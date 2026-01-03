row1 = ['😖', '😖' , '😖']
row2 = ['😖', '😖' , '😖']
row3 = ['😖', '😖' ,'😖']

matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input('Enter the postion where you u want to hide car')
#22
row_number = position[0]
coloum_number = int(position[1])
row_selected = matrix[row_number-1]
row_selected = list(row_selected)
row_selected[coloum_number-1] = "X"
print(f"{row1}\n{row2}\n{row3}")


