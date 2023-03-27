import re

# Open the text file and read its contents
with open('All_Pic_Passwords.txt', 'r') as f:
    text = f.read()

# Regular expression pattern to match the image name, size, and cell number
pattern = r'(\w+\.jpg)\((\d+), (\d+)\), Cell (\d+)'

# Initialize a dictionary to store the count of each cell number for each image
image_counts = {}

# Loop over each match in the text file
for match in re.findall(pattern, text):
    image_name, width, height, cell_number = match

    # If the image name is not yet in the dictionary, add it
    if image_name not in image_counts:
        image_counts[image_name] = {}

    # If the cell number is not yet in the image dictionary, add it with a count of 1
    if cell_number not in image_counts[image_name]:
        image_counts[image_name][cell_number] = 1
    # If the cell number is already in the image dictionary, increment its count by 1
    else:
        image_counts[image_name][cell_number] += 1

# Print the dictionary of image counts
for image_name, counts in image_counts.items():
    print(f'Image: {image_name}')
    for cell_number, count in counts.items():
        print(f'  Cell {cell_number}: {count} occurrences')
