# Identify the variables
left_list = list()
right_list = []

# Initialize the result variable
part1_result = 0
part2_result = 0

# Use a python library to open the text file containing the input
with open('day1_input.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        line_list = line.split('   ')
        left_list.append(int(line_list[0])) 
        # converting the string to an integer
        right_list.append(int(line_list[1]))

# Part 1 ===========
# Sort list to ascending order
left_list.sort()
right_list.sort()

# Tracks where we are in the list
index = 0

# Subtract the values on the L & R, and add the difference
for x in range(len(left_list)):
    difference_in_value = abs(left_list[x] - right_list [x])
    part1_result += difference_in_value
    # 2031679

# Part 2 =========
for left_num in left_list:
    found = 0
    for right_num in right_list:
        if left_num == right_num:
            found += 1
    part2_result += (left_num * found)
    # 19678534

import pdb; pdb.set_trace()

# Part 2b
counts = {}
part2_result = 0
for right_num in right_list:
    if right_num in counts:
        counts[right_num] += 1
    else:
        counts[right_num] = 1
for left_num in left_list:
    if left_num in counts:
        part2_result += left_num * counts[left_num]
