marks = []
mark_ranges = (0, 29, 39, 69, 100)
mark_collections = {
    ' 0 - 29': 0,
    '30 - 39': 0,
    '40 - 69': 0,
    '70 - 100': 0,
}

while True:
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
for i in range(len(mark_ranges)-1):
    n_stars = 0
    for mark in marks:
        if mark > mark_ranges[i] and mark <= mark_ranges[i+1]:
            n_stars += 1

    mark_collections[list(mark_collections.keys())[i]] = n_stars

for mark_collection in mark_collections.keys():
    print(mark_collection.ljust(10).rjust(10), end=' ')
print()

for i in range(1, max(mark_collections.values())+1):
    for mark_collection in mark_collections.keys():
        # print(mark_collection, mark_collections[mark_collection], i,
        #       mark_collections[mark_collection] >= i)
        if mark_collections[mark_collection] >= i:
            print('*'.center(10, ' '), end=' ')
        else:
            print(' '.center(10, ' '), end=' ')
    print()

if marks:
    print('\nAverage mark :', sum(marks)/len(marks))
else:
    print('\nAverage mark :', 0)
print('Number of students with a pass mark (mark of 40 or above): ',
      len([i for i in marks if i >= 40]))
print('Highest mark: ', max(marks))
print('Lowest mark: ', min(marks), '\n')

print(len(marks), 'students in total.')
