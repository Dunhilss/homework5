import random
random_numb = [random.randint(-100, 100) for _ in range(10)]
print("List of random numbers:", random_numb)
sumnegative = sum(x for x in random_numb if x < 0)
print("Sum of negative values:", sumnegative)
even_numb = sum(x for x in random_numb if x % 2 == 0)
print("Sum of paired values:", even_numb)
sum_odd = sum(x for x in random_numb if x % 2 != 0)
print("Sum of unpaired numbers:", sum_odd)
index_3 = 1
for i in range(0, len(random_numb), 3):
    index_3 *= random_numb[i]
print("Sum of multiplication of values divisible by index 3:", index_3)
min_value = min(random_numb)
max_value = max(random_numb)
print(f"Multiplication sum between minimum and maximum value: {min_value * max_value}")
first_positive_index = next((i for i, x in enumerate(random_numb) if x > 0), None)
last_positive_index = next((i for i, x in enumerate(reversed(random_numb)) if x > 0), None)
if first_positive_index is not None and last_positive_index is not None:
    last_positive_index = len(random_numb) - last_positive_index - 1
    sum_between_positives = sum(random_numb[first_positive_index + 1:last_positive_index])
    print("Sum of values between the first and the last positive value", sum_between_positives)
else:
    print("There are no or few positive values on the list. Try again.")
