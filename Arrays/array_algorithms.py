# Creating an array
from functools import reduce

array_names = ["John", "James", "Peter", "Brian"]

# Iterate through Elements using a for loop
for name in array_names:
    print(name)

# Iterate through elements using a while loop

array_length = len(array_names)
i = 0
while i < array_length:
    print(array_names[i])
    i += 1

# Getting an element in an array
# We use the index method to get an element

first_name_in_array = array_names[0]
print(first_name_in_array)

# Search for an element in an array
print(array_names.index("James"))  # This will get the index of the Element

# Inserting elements in the array
# We use append() to add an element to an array

array_names.append("Derrick")
print(array_names)

# Delete element in an array
# Using th pop method
# Pop removes element at a specified position
array_names.pop(1)  # Removes element at index 1
print(array_names)

# Using the remove method
#  removes the first Element with the specified value
array_names.remove("Brian")
print(array_names)

# Filtering array using our own expression
filtered_array = []
for name in array_names:
    if name == "James":
        filtered_array.append(name)
    elif name == "Peter":
        filtered_array.append(name)

print(filtered_array)

# Fetch a sub array
# Syntax( array_names[start:stop:step]
sub_array = array_names[1:3:1]
print(sub_array)

# Merging arrays
array_last_names = ["Elsher", "Solace", "Raven", "Thatcher"]

combined_array = array_names + array_last_names
print(combined_array)

# Reversing arrays
# Reversing array using the reverse method
array_names.reverse()
print(array_names)

# Rotating an array
