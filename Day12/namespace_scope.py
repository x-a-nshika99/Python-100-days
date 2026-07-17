# Name space and scope 
# local and global

enemies = 1

def increase_enemies():
    enemies = 2
    print("enemies inside the function : {enemies}")

increase_enemies()
print("enemies outside the function : {enemies}")


# both will print different value beacuse for the functio enemies is in the function that is local variable 
# but the enemies outside the function is gloabal variable 

# local scope
# When you create a new variable or indeed a new function inside another function, it's only accessible,
# you can only use it when you're inside that function because it has local scope.
# It's only valid within the walls of this drink potion function.


# The only difference between global scope and local scope is where you define or where you create your
# variables or your functions.

# Global scope
# global variables are available within functions no matter how deep it gets nested.
# And it's also available outside of functions.
# This concept of global and local scope doesn't just apply to variables.

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
# output is 10 
# As I alluded to before, it also applies to functions and basically anything else you name.
# This is a concept called the Namespace.
# So we defined this variable player_health,
# we define this function drink_potion,
# anything that you give a name to has a namespace.
# And that namespace is valid in certain scopes.
# This concept of scope applies to basically anything you name.


# deos the python have BLOCK SCOPE

game_level =2

enemies1 = ["skeleton","zombie", "alien"]

if game_level<5:
    new_enemy = enemies1[0]

print(new_enemy)

# so now this new_enemy is available anywhere within this function,
# because blocks like if, while, for, all of these blocks of code with colons and indentation, they don't
# count as creating a local scope.
# but

def create_enemy():
    
    if game_level<5:
        new_enemy = enemies1[0]

print(new_enemy)
# this show error kyuki def ke ander create kia hua 
# variable local ho jata ha 
 


 