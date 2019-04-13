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

# Iterate thought the all the mark ranges so it print row by row
for i in range(len(mark_ranges)-1):
    n_stars = 0
    for mark in marks:
        # Compare mark with i th element and i+1 th element from the mark_ranges tuple, i will be incremented from the above for loop
        if mark > mark_ranges[i] and mark <= mark_ranges[i+1]:
            n_stars += 1
    # This is little hacky way I used to get the keys from the mark_collections dictionary
    mark_collections[list(mark_collections.keys())[i]] = n_stars
    # ljust to have some spacing between
    print(f'{list(mark_collections.keys())[i]}'.ljust(8), ':', '*'*n_stars)

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
