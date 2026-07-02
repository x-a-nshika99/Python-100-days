# want to creat tip calculator
from unicodedata import decimal


total_bill = int(input("What was the total bill? $"))
tip_money = int(input("How much would you like to give as a tip? $10, $12, or $15? "))
number_of_people = int(input("How many people to split the bill? ")) 
if tip_money == 10:
    total_bill_with_tip = total_bill + (total_bill * 0.10)   
elif tip_money == 12:
    total_bill_with_tip = total_bill + (total_bill * 0.12)
elif tip_money == 15:
    total_bill_with_tip = total_bill + (total_bill * 0.15)
else:
    print("Invalid tip amount. Please choose $10, $12, or $15.")
    exit()

bill_per_person = total_bill_with_tip / number_of_people
print(f"Each person should pay: ${bill_per_person:.2f}")



    
# f"..." → Marks the string as an f-string, which allows embedding variables directly inside curly braces {}.
# bill_per_person → This is the variable being inserted into the string.
# :.2f → This is a format specifier:
# f means format as a floating-point number.
# .2f means show 2 decimal places.