# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class= class_1+class_2
print(new_class)

# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary

courses={'math':65,'english':70,'history':80,'french':70,'science':60}

# Slice the dict and stores  the all subjects marks in variable
math=courses['math']
english=courses['english']
history=courses['history']
french=courses['french']
science=courses['science']


# Store the all the subject in one variable `Total`
total=math+english+history+french+science
# Print the total
print(total)
# Insert percentage formula
percentage= total*100/500
# Print the percentage
print(percentage)



# Create the Dictionary
 

mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

max_marks_scored=max(mathematics,key=mathematics.get)
print(max_marks_scored)

# Given string
topper= 'Andrew Ng'
topper.split(' ')
split_name= topper.split(' ')
# Create variable first_name 
first_name=split_name[0]
# Create variable Last_name and store last two element in the list
Last_name=split_name[1]
# Concatenate the string
full_name=Last_name+ ' '+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
# Code ends here


