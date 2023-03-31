
# Open the file and read the contents
with open('All_Android_Passwords.txt', 'r') as f:
    contents = f.read()

# Split the contents into individual lists

lists = contents.split('\n')

# Get the element to count
element = input("Enter the element to count: ")
totalCount = 0

for i, lst in enumerate(lists):
    temp = lst.split(',')
    count = temp[0].count(element)
    totalCount += count

print(f"\nTotal occurrences of {element} in all lists: {totalCount}")


length_counts = {}

for lst in lists:
    temp = lst.split(',')
    password_length = int(temp[-1].split()[-1])
    if password_length in length_counts:
        length_counts[password_length] += 1
    else:
        length_counts[password_length] = 1

for length in range(12):
    if length in length_counts:
        print(f"\nTotal occurrences of passwords with length {length}: {length_counts[length]}")
    else:
        print(f"\nNo passwords found with length {length}")
