# Function to calculate height (referenced from your calculations.py note)
def calculate_total_height(h1, h2):
    return h1 + h2

# Capture information for User 1 using a dictionary (matching 07_create_dict_from_variables.py)
name1 = input('Enter the name for user 1: ')
age1 = int(input('Enter the age for user 1: '))
height1 = float(input('Enter the height for user 1 (cm): '))

user1 = {
    'name': name1,
    'age': age1,
    'height': height1
}

# Capture information for User 2
name2 = input('Enter the name for user 2: ')
age2 = int(input('Enter the age for user 2: '))
height2 = float(input('Enter the height for user 2 (cm): '))

user2 = {
    'name': name2,
    'age': age2,
    'height': height2
}

# Store both dictionaries in a list (matching 01_simple_list.py)
users_list = [user1, user2]
print()

# Display each user's information using a loop (matching 13_loop_through_users.py)
for user in users_list:
    print(f"Your name is {user['name']}, you are {user['age']} years old and your height is {user['height']} cm.")

# Calculate and display total height using the function
total = calculate_total_height(user1['height'], user2['height'])

print()
print(f'The total combined height is: {total} cm')