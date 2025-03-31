# Kennedy Watson
# Intro List Program -- Sum of a List
# SCIS 111-113
# Dr. Lawrence
# Due 10.28.24

# Initialize empty list
myList = []

# Initialize sum
total_sum = 0

# Read 10 integers from user
for i in range(10):
    num = int(input("Please enter an integer: "))
    myList.append(num)
    total_sum += num  # Add to sum

# Print results
print("The sum of the list is:", total_sum)
print("This is the list:", myList)

# Find min of list
minimum = myList[0]
for j in range(1, len(myList)):
    if myList[j] < minimum:
        minimum = myList[j]
print("The minimum is:", minimum)

# Finding max of list
maximum = myList[0]
for j in range(1, len(myList)):
    if myList[j] > maximum:
        maximum = myList[j]
print("The maximum is:", maximum)

# Sorting list
sorted_list = sorted(myList)  # Use sorted() to create a new sorted list
print("The sorted list is:", sorted_list)
