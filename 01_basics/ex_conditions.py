# LEVEL 1 — Simple Conditionals (if / else)

# 1. Minimum age:
# Ask the user for their age and display if they are an adult or a minor.

number_age = int(input("Enter your age: "))

if number_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# 2. Positive, negative, or zero:
# Ask for a number and show whether it is positive, negative, or zero.

user_number = int(input("Enter a number: "))

if user_number > 0:
    print(f"{user_number} is positive.")
elif user_number == 0:
    print(f"{user_number} is zero.")
else:
    print(f"{user_number} is negative.")


# 3. Correct password:
# Define password = "python123" and ask the user to enter it.
# If it matches: "Access granted", otherwise: "Incorrect password".

password = "python123"
user_password = input("Enter the password: ")

if user_password == password:
    print("Access granted.")
else:
    print("Incorrect password.")


# LEVEL 2 — Multiple Conditionals (if / elif / else)

# 4. School grades:
# Ask for a grade from 0 to 10 and classify it:
# < 5   → "Fail"
# 5–6   → "Pass"
# 7–8   → "Good"
# 9–10 → "Excellent"

grade = float(input("Enter your grade (0–10): "))

if grade < 5:
    print("Fail.")
elif 5 <= grade <= 6:
    print("Pass.")
elif 7 <= grade <= 8:
    print("Good.")
elif 9 <= grade <= 10:
    print("Excellent.")
else:
    print("Invalid grade.")


# 5. Traffic light:
# Ask the user for a color (red/yellow/green) and display:
# red → "Do not cross"
# yellow → "Caution"
# green → "Cross"
# anything else → "Invalid color"

light_color = input("Enter the traffic light color (red/yellow/green): ").strip().lower()

if light_color == "red":
    print("Do not cross.")
elif light_color == "yellow":
    print("Caution.")
elif light_color == "green":
    print("Cross.")
else:
    print("Invalid color.")


# LEVEL 3 — Logical Operators (and, or, not)

# 6. VIP area access:
# Ask for age and VIP access.
# Access is allowed only if age > 18 AND has VIP access.

age = int(input("Enter your age: "))
vip_input = input("Do you have VIP access? (yes/no): ").strip().lower()

has_vip = vip_input == "yes"

if age > 18 and has_vip:
    print("You can enter the VIP area.")
else:
    print("Access denied.")


# 7. Store discount:
# If the client spends more than 100€ OR has a membership card → discount.

amount = float(input("Enter total amount spent: "))
member_input = input("Do you have a membership card? (yes/no): ").strip().lower()

has_membership = member_input == "yes"

if amount > 100 or has_membership:
    print("You have a discount.")
else:
    print("No discount available.")


# 8. Suitable temperature:
# Ask for the temperature.
# If it's between 20 and 30 (inclusive) → "Ideal temperature"
# Otherwise → "Too cold or too hot"

temperature = float(input("Enter the temperature: "))

if 20 <= temperature <= 30:
    print("Ideal temperature.")
else:
    print("Too cold or too hot.")


# 9. Blocked user:
# If user is NOT active OR has more than 3 failed attempts → "Account blocked"

active_input = input("Is the user active? (yes/no): ").strip().lower()
attempts = int(input("Enter number of failed attempts: "))

is_active = active_input == "yes"

if not is_active or attempts > 3:
    print("Account blocked.")
else:
    print("Account is active.")


# LEVEL 4 — Combined Logic

# 10. Scholarship system:
# Inputs:
# - age
# - average grade
# - low income (yes/no)
#
# Scholarship is granted if:
# - grade >= 8 AND age < 25
# OR
# - low income AND grade >= 6

age = int(input("Enter your age: "))
avg_grade = float(input("Enter your average grade: "))
low_income_input = input("Do you have low income? (yes/no): ").strip().lower()

has_low_income = low_income_input == "yes"

if (avg_grade >= 8 and age < 25) or (has_low_income and avg_grade >= 6):
    print("Scholarship granted.")
else:
    print("Scholarship not granted.")


















