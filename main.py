import random
random_numb = [random.randint(-100, 100) for _ in range(10)]
print("List of random numbers:", random_numb)
sumnegative = sum(x for x in random_numb if x < 0)
print("\nSum of negative values:", sumnegative)
even_numb = sum(x for x in random_numb if x % 2 == 0)
print("\nSum of paired values:", even_numb)
sum_odd = sum(x for x in random_numb if x % 2 != 0)
print("\nSum of unpaired numbers:", sum_odd)
index_3 = 1
for i in range(0, len(random_numb), 3):
    index_3 *= random_numb[i]
print("\nSum of multiplication of values divisible by index 3:", index_3)
min_value = min(random_numb)
max_value = max(random_numb)
print(f"\nMultiplication sum between minimum and maximum value: {min_value * max_value}")
first_positive_index = next((i for i, x in enumerate(random_numb) if x > 0), None)
last_positive_index = next((i for i, x in enumerate(reversed(random_numb)) if x > 0), None)
if first_positive_index is not None and last_positive_index is not None:
    last_positive_index = len(random_numb) - last_positive_index - 1
    sum_between_positives = sum(random_numb[first_positive_index + 1:last_positive_index])
    print("\nSum of values between the first and the last positive value", sum_between_positives)
else:
    print("\nThere are no or few positive values on the list. Try again.")

import random
random_numbers = [random.randint(-100, 100) for _ in range(10)]
print("\n\nList of random numbers:", random_numbers)
even_numbers = [x for x in random_numbers if x % 2 == 0]
print("List of paired numbers:", even_numbers)
odd_numbers = [x for x in random_numbers if x % 2 != 0]
print("List of unpaired numbers:", odd_numbers)
positive_numbers = [x for x in random_numbers if x > 0]
print("List of positive numbers:", positive_numbers)
negative_numbers = [x for x in random_numbers if x < 0]
print("List of negative numbers:", negative_numbers)