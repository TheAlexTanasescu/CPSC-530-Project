
# Open the file and read the contents
with open('All_Colored_Passwords.txt', 'r') as f:
    contents = f.read()

# Split the contents into individual lists

lists = contents.split('\n')

'''
i = 1
for list in lists:
    print(f"List {i}")
    print(list)
    i += 1
    '''
# Get the element to count
element = input("Enter the element to count: ")

totalCount = 0
#
#  Loop through each list and count the element
for i, lst in enumerate(lists):
    #temp = lst.split(',')
    count = lst.count(element)
    #print(f"List {i+1}: {count} occurrences of {element}")
    totalCount += count

# Count the element in all lists
#total_count = sum(lst.count(element) for lst in lists)
print(f"\nTotal occurrences of {element} in all lists: {totalCount}")

