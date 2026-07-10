def left_of_weeks(int):
    weeks_in_a_year = 52
    years_left = 90 - age
    weeks_left = years_left * weeks_in_a_year
    return weeks_left


print("Do you want to calculate your life in weeks")
age = int(input("enter your current age"))
print(left_of_weeks(age))
