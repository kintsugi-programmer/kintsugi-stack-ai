# Intro to Lists
# Organise data
# work with efficiently
# get an item at a specified position (first, second, third, etc),
# check the number of items, and
# add and remove items.

# can help to classify
# When doing data science, you need a way to organize your data so you can work with it efficiently. 
# Python has many data structures available for holding your data, such as lists, sets, dictionaries, and tuples.

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle" # bad way to store data

print(type(flowers))
print(flowers)
# <class 'str'>
# pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"] # list representation

print(type(flowers_list))
print(flowers_list)
# <class 'list'>
# ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle']

# length: len()
# The list has ten entries
print(len(flowers_list))
# 10

# indexing
# We can refer to any item in the list according to its position in the list (first, second, third, etc). This is called indexing.

# Note that Python uses zero-based indexing, which means that:

# to pull the first entry in the list, you use 0,
# to pull the second entry in the list, you use 1, and
# to pull the final entry in the list, you use one less than the length of the list.
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])
# First entry: pink primrose
# Second entry: hard-leaved pocket orchid
# Last entry: globe thistle

# You may have noticed that in the code cell above, we use a single print() to print multiple items (both a Python string (like "First entry:") and a value from the list (like flowers_list[0]). To print multiple things in Python with a single command, we need only separate them with a comma.

# slicing
# You can also pull a segment of a list (for instance, the first three entries or the last two entries). This is called slicing. For instance:

# to pull the first x entries, you use [:x], and
# to pull the last y entries, you use [-y:].

print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])
# First three entries: ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells']
# Final two entries: ['monkshood', 'globe thistle']

# As you can see above, when we slice a list, it returns a new, shortened list.

# .remove()
# Removing items
# Remove an item from a list with .remove(), and put the item you would like to remove in parentheses.

flowers_list.remove("globe thistle")
print(flowers_list)
# ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood']

# .append()
# Adding items
# Add an item to a list with .append(), and put the item you would like to add in parentheses.

flowers_list.append("snapdragon")
print(flowers_list)
# ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'snapdragon']

# Lists are not just for strings
# So far, we have only worked with lists where each item in the list is a string. But lists can have items with any data type, including booleans, integers, and floats.

# As an example, consider hardcover book sales in the first week of April 2000 in a retail store.

hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
# Here, hardcover_sales is a list of integers. Similar to when working with strings, you can still do things like get the length, pull individual entries, and extend the list.

# len()
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
# Length of the list: 7
# Entry at index 2: 172
# You can also get the minimum with min() and the maximum with max().

# min() & max()
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
# Minimum: 128
# Maximum: 191

# sum()
# To add every item in the list, use sum().

print("Total books sold in one week:", sum(hardcover_sales))
# Total books sold in one week: 1107
# We can also do similar calculations with slices of the list. In the next code cell, we take the sum from the first five days (sum(hardcover_sales[:5])), and then divide by five to get the average number of books sold in the first five days.

print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)
# Average books sold in first five days: 153.8