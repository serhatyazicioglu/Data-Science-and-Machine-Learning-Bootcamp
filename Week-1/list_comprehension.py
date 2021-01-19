# List Comprehension Examples

# Example 1: Separate the numbers in the list as odd and even and assign them to two separate lists.

# First let's do it without using List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(even_numbers, odd_numbers)

# Now let's do it with using List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
even_numbers = []

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print(even_numbers, odd_numbers)

# we can also do it with the help of function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
even_numbers = []

def odd_or_even(list_name):
    even_numbers = [i for i in list_name if i % 2 == 0]
    odd_numbers = [i for i in list_name if i % 2 != 0]
    return even_numbers, odd_numbers

odd_or_even(numbers)



# Example 2: Convert the names of the numeric variables in the car_crashes data to uppercase letters and add NUM at the beginning.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
num_cols_1 = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# Example 3: Write "FLAG" AT the END of the variables that do not contain "no" in their name.

df = sns.load_dataset("car_crashes")
df.columns
num_cols_2 = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Example 4: Create a new df by selecting the names of the variables that differ from the variable names in og_list.

df = sns.load_dataset("car_crashes")
df.columns
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()
