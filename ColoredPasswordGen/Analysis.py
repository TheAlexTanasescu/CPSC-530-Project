from collections import Counter

# Open the file and read the contents
with open('All_Colored_Passwords.txt', 'r') as f:
    contents = f.read()

# Split the contents into individual lists

passwords = contents.split('\n')



# Get the element to count
element = input("Enter the element to count: ")

count = 0
for lst in passwords:
    if element in lst:
        count += 1

print(f"Number of passwords containing {element}: {count}")

'''
totalCount = 0

#  Loop through each list and count the element
for i, lst in enumerate(lists):
    count = lst.count(element)
    totalCount += count

# Count the element in all lists
#print(f"\nTotal occurrences of {element} in all lists: {totalCount}")


length_counts = {}

for lst in lists:
    password_length = lst[-1]
    if password_length in length_counts:
        length_counts[password_length] += 1
    else:
        length_counts[password_length] = 1
#print(length_counts)


for length in length_counts:
        print(f"\nTotal occurrences of passwords with length {length}: {length_counts[length]}")
    #else:
     #   print(f"\nNo passwords found with length {length}")

'''