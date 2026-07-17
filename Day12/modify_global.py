# how to modify global varibles

# dont frooce to modify the gobal variable inside the function 
# instead you can pass this global and then use is for update

enemies = 1

def increase_enemies(enemies):
    print("enemies inside the function : {enemies}")
    return enemies + 1

enemies = increase_enemies(enemies)
print("enemies outside the function : {enemies}")


# global const that never change in any function or condition
# so in pyhton constant written in upper case 
PI =21323
# like this 