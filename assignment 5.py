# Task 1

try:
    Marks = {'Alice': 85, 'Walter': 90}
    n = input("Enter the student's name: ")
    print(n + "'s marks: ", Marks[n])
except KeyError:
    print('Student not found.')

# ------------------------------------------------------------------------------------------------

# Task 2

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Original list: ', number_list)
x = number_list[:5]
print('Extracted first five elements:', x)
x.reverse()
print('Reversed extracted elements:', x)
