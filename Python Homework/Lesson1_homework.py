# Capture information of 2 users. This information includes their name, age and height (in cm).
User1 = input('Enter the name for user1: ')
User2 = input('Enter the name for user2: ')
age1 = int(input('Enter the age for age1: '))
age2 = int(input('Enter the age for age2: '))
Height1 = float(input('Enter the height for height1: '))
Height2 = float(input('Enter the height for height2: '))
print()

# Display each user's information in a sentence format.
print(f'Your name is {User1}, you are {age1} years old and your height is {Height1} cm.')
print(f'Your name is {User2}, you are {age2} years old and your height is {Height2} cm.')
print()

# Then calculate and display the total combined height of both users.
print(f'The total combined height is: {Height1 + Height2} cm')
print(f'Substraction: {Height1 - Height2} cm')
print(f'Division: {Height1 / Height2} cm')
print(f'Multiplication: {Height1 * Height2} cm')
