# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = "Dog", "snake", "dragon"
# Age (integer)
age = "1", "50", "24"
# Color (at least 3 choices, string)
color = "brown", "black", "Blue"
# Weight (float)
weight = "150", "10", "40"
# Print a summary of your pet using an f-string
print(f"my pet is a {random.choice(animal)}.")
print(f"my pet is {random.choice(age)} years old.")
print(f"my pet is {random.choice(color)}.")
print(f"my pet weighs {random.choice(weight)} pounds.")