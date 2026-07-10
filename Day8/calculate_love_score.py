# Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out.



def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    true_score = 0
    love_score = 0

    for ch in combined:
        if ch in "true":
            true_score += 1

    for ch in combined:
        if ch in "love":
            love_score += 1

    return int(f"{true_score}{love_score}")


name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

print("Your love score is", calculate_love_score(name1, name2))


















# def calculate_love_score(name1, name2):
#     i=0
#     t_times=0
#     for i in range(0,4):
#         if name1[i] and name2[i] == "t":
#             t_times+=1
#         elif  name1[i] and name2[i] == "u":
#             t_times+=1
#         elif  name1[i] and name2[i] == "r":
#             t_times+=1
#         elif  name1[i] and name2[i] == "e":
#             t_times+=1
#         total = t_times
        
#     j=0 
#     l_times = 0
#     for i in range(0,4):
#         if  name1[i] and name2[i] == "l":
#             l_times+=1
#         elif  name1[i] and name2[i] == "o":
#             l_times+=1
#         elif  name1[i] and name2[i] == "v":
#             l_times +=1
#         elif name1[i] and name2[i] == "e" :
#             l_times +=1
#         total1 = l_times 
    
#     sum = print(f"score" + "{total}{total1}")
#     return sum
    
# print("calculate_love_score")
# name1 = input("enter your name")
# name2 = input("enter your partner name")
# print("your love score is " + calculate_love_score(name1,name2))