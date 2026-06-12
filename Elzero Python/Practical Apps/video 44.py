age = int(input("Enter your age:").strip())
unit = input("How do you want to display your age? (1-months, 2-days, 3-hours, 4-minutes, 5-seconds)").strip().lower()
age_in_month = age * 12
age_in_days = age * 365
if unit == "1" or unit == "months":
    print(f"Your age in months is: {age_in_month}")
elif unit == "2" or unit == "days":
    print(f"Your age in days is: {age_in_days:,}")
elif unit == "3" or unit == "hours":
    print(f"Your age in hours is: {age_in_days * 24:,}")
elif unit == "4" or unit == "minutes":
    print(f"Your age in minutes is: {age_in_days * 24 * 60:,}")
elif unit == "5" or unit == "seconds":
    print(f"Your age in seconds is: {age_in_days * 24 * 60 * 60:,}")
else:
    print("invalid choice")