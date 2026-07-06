import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    
sysmbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']   

print("Welcome to the Password Generator!")
num_letters = int(input("how many letters would you like in your passwords?\n "))
num_numbers = int(input("how many numbers would you like in your passwords?\n "))
num_symbols = int(input("how many symbols would you like in your passwords?\n "))

# easy level

password = ""
for char in range(1, num_letters + 1):
    password += random.choice(letters) 

for char in range(1, num_numbers + 1):
    password += random.choice(numbers)

for char in range(1, num_symbols + 1):
    password += random.choice(sysmbols)
print(password)

# medium level
password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))            

for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, num_symbols + 1):
    password_list.append(random.choice(sysmbols))


# random.shuffle is the random module's shuffle function, which randomly reorders the elements in a list. It modifies the original list
#  in place and does not return a new list. This is useful for creating a random order of characters in the password.

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)
