import math
from multiprocessing.resource_sharer import stop
import numbers

students_scores = [85, 92, 78, 90, 88, 95, 80]

max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score

print("Maximum score:", max_score)

print("Sum of all scores:", sum(students_scores))

# range function is used to generate a sequence of numbers. It can take one, two, or three arguments:
# 1. range(stop): Generates numbers from 0 to stop-1.

total = 0
for number in range(1,101):
    total += number
print("Sum of numbers from 1 to 100:", total)