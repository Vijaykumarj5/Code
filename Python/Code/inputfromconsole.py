# Ask user for name 
name = input("what is your name? ")

# Remove blank spaces 
name = name.strip()

# capitaliaze
name = name.title() 

# One line for above code

name = input("what is your name? ").strip().title()

#say hello to user 
print("Hello "+ name)

