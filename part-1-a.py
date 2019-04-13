marks = []
mark_ranges = (0, 29, 39, 69, 100)
# Marks Distribution
mark_collections = {
    ' 0 - 29': 0,
    '30 - 39': 0,
    '40 - 69': 0,
    '70 - 100': 0,
}


while True:
    mark = int(input("Enter Marks for Student {}: ".format(len(marks)+1)))
    # If mark is less than 0 we need exit the list
    if mark < 0:
        break
    marks.append(mark)

print()
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
print()

print(len(marks), 'students in total.')
