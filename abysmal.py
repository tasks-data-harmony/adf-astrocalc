from datetime import datetime, timedelta

def strikethrough(text):
    """Returns a strikethrough version of the given text, including spaces on both sides."""
    spaced_text = f" {text} "  # Ensure space before and after
    return ''.join(f"{char}\u0336" for char in spaced_text)  # Apply strikethrough to everything

def get_abysmal_date(gregorian_date):
    """
    Converts a Gregorian date to the Abysmal Calendar format (Year ~ Month ~ Day).
    Includes correct weekday shifting, New Year's Day (♆), and Leap Day (⛢).
    """
    epoch_start = datetime(1492, 5, 26)  # Julian date converted to datetime

    days_since_epoch = (gregorian_date - epoch_start).days

    abysmal_year = days_since_epoch // 365  
    days_in_current_year = days_since_epoch % 365

    is_leap_year = (abysmal_year % 4 == 0) and not (abysmal_year % 128 == 0)

    astro_symbols = {
        "NYD": "♆", "Leap Day": "⛢", "Saturday": "♄", "Sunday": "☉",
        "Monday": "☽", "Tuesday": "♂", "Wednesday": "☿",
        "Thursday": "♃", "Friday": "♀"
    }

    if days_in_current_year == 0:
        return f"{abysmal_year} {astro_symbols['NYD']}"

    if is_leap_year and days_in_current_year == 1:
        return f"{abysmal_year} {astro_symbols['Leap Day']}"

    adjusted_day = days_in_current_year - (1 if is_leap_year else 0)

    month = (adjusted_day // 28) + 1
    day = (adjusted_day % 28) + 1
    month_display = strikethrough(str(month))

    base_weekday = "Saturday"  
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    total_shift_days = (days_since_epoch - (abysmal_year * 365)) % 7
    weekday_index = (weekdays.index(base_weekday) + total_shift_days) % 7
    weekday = weekdays[weekday_index]

    return f"{abysmal_year} ~ {month_display} ~ {day} {astro_symbols[weekday]}"

while True:
    input_date_str = input("Enter a date (MM/DD/YYYY), or press Enter to exit: ")
    if not input_date_str:
        break  # Exit the loop if the user just presses Enter

    try:
        input_date = datetime.strptime(input_date_str, '%m/%d/%Y')
        abysmal_date = get_abysmal_date(input_date)
        print(abysmal_date)
    except ValueError:
        print("Invalid date format. Please try again.")
