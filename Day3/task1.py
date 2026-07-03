weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<25:
    print("Normal")
elif 25<=bmi<29.9 :
    print("Overweight")