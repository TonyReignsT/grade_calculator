grade_percentage = int(input("What is your grade percentage? "))

letter = ""

if grade_percentage >= 90:
  letter = "A"
elif grade_percentage >= 80:
  letter = "B"
elif grade_percentage >= 70:
  letter = "C"
elif grade_percentage >= 60:
  letter = "D"
elif grade_percentage < 60:
  letter = "F"
else:
    print("Invalid grade percentage.")

    # To Determine the sign
sign = ""

if letter != "A" and letter != "F":
    last_digit = grade_percentage % 10
    if last_digit >= 7:
      sign = "+"
    elif last_digit < 3:
      sign = "-"
    else:
      sign = ""

# To Handle the special cases for A and F
if letter == "A" and grade_percentage <= 94:
  sign = "-"
elif letter == "F":
  sign = ""

print(f"Your grade is {letter}{sign}.")

# print(f"Your grade is {letter}.")

if grade_percentage >= 70:
  print("Congratulations! You passed the course.")
else:
  print("Unfortunately you've failed the course. Keep pushing, You'll get it next time.")