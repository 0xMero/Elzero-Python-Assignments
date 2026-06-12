age = int(input("Enter your age:").strip())
print(f"Your age in years is: {age}")
age_in_month = age * 12
print(f"Your age in months is: {age_in_month}")
age_in_days = age * 365
print(f"Your age in days is: {age_in_days:,}")
print(f"Your age in hours is: {age_in_days * 24:,}")
print(f"Your age in minutes is: {age_in_days * 24 * 60:,}")
print(f"Your age in seconds is: {age_in_days * 24 * 60 * 60:,}")