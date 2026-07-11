programming_dictionary = {
    "bug": "an error in a program that prevent the program from running as expected.",
    "function" : "a piece of code that you can easily call over and over again",
    "loop" : "the action of doing something over and over again",
}

print(programming_dictionary["function"])
programming_dictionary["loop"] ="this is updated loop"
print(programming_dictionary)

# wipe an existing dictionary 
program_dictionary ={}
print(program_dictionary)

# edit an item in a deictionary

program_dictionary["boys"] ="there are total this much boy"


# loop through dictionary 

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
