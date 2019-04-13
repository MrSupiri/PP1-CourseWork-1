marks = []
mark_ranges = (0, 29, 39, 69, 100)
mark_collections = {
    ' 0 - 29': 0,
    '30 - 39': 0,
    '40 - 69': 0,
    '70 - 100': 0,
}


while True:
    # Catch Invalid Inputs
    try:
        mark = int(input("Enter Marks for Student {}: ".format(len(marks)+1)))
    except ValueError:
        print('Invalid Input !, Please Enter a number for the Marks')
    if mark < 0:
        break
    if mark > 100:
        print('Please Enter Numbers that are between 0-100')
        continue
    marks.append(mark)

print()
# Iterate thought the all the mark ranges so it print row by row
for i in range(len(mark_ranges)-1):
    n_stars = 0
    for mark in marks:
        if mark > mark_ranges[i] and mark <= mark_ranges[i+1]:
            n_stars += 1

    mark_collections[list(mark_collections.keys())[i]] = n_stars

# Print the Head of the Table
for mark_collection in mark_collections.keys():
    print(mark_collection.ljust(10).rjust(10), end=' ')
print()

# Print the star for each column if the value of the column extend to current row
for i in range(1, max(mark_collections.values())+1):
    # iterate though the keys of the dictionary to get the values
    for mark_collection in mark_collections.keys():
        if mark_collections[mark_collection] >= i:
            print('*'.center(10, ' '), end=' ')
        else:
            print(' '.center(10, ' '), end=' ')
    # New Line
    print()

# To prevent ZeroDivisionError
if marks:
    print('\nAverage mark :', sum(marks)/len(marks))
else:
    print('\nAverage mark :', 0)

# Iterate though the whole list make a new list with only marks that are equal or greater than 40 and take the length of that list
print('Number of students with a pass mark (mark of 40 or above): ',
      len([i for i in marks if i >= 40]))
# Max and Min are inbuilt python functions that take a sequence as the input and output the max or min of that sequence
print('Highest mark: ', max(marks))
print('Lowest mark: ', min(marks), '\n')
print(len(marks), 'students in total.')
