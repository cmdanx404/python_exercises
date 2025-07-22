from datetime import datetime, date

def age_calculator():
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = date.today()

    # Calculate age in years
    age_years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age_years -= 1

    # Days lived
    days_lived = (today - birth_date).days

    # Next birthday age
    next_birthday_age = age_years + 1

    print(f"You are {age_years} years old.")
    print(f"You have lived {days_lived} days.")
    print(f"You will be {next_birthday_age} on your next birthday.")

age_calculator()
