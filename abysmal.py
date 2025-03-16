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
    # Define the Abysmal Calendar Epoch (May 26, 1492 - Julian Calendar)
    epoch_start = datetime(1492, 5, 26)  # Julian date converted to datetime

    # Calculate total days since the epoch
    days_since_epoch = (gregorian_date - epoch_start).days

    # Compute the Abysmal Year
    abysmal_year = days_since_epoch // 365  # 365-day cycles determine year
    days_in_current_year = days_since_epoch % 365

    # Determine if it's a Leap Year (Every 4 years, but skips once every 128 years)
    is_leap_year = (abysmal_year % 4 == 0) and not (abysmal_year % 128 == 0)

    # Define Astro Symbols
    astro_symbols = {
        "NYD": "♆",  # Neptune
        "Leap Day": "⛢",  # Uranus
        "Saturday": "♄",  # Saturn
        "Sunday": "☉",  # Sun
        "Monday": "☽",  # Moon
        "Tuesday": "♂",  # Mars
        "Wednesday": "☿",  # Mercury
        "Thursday": "♃",  # Jupiter
        "Friday": "♀",  # Venus
    }

    # New Year's Day (NYD) is on the Winter Solstice (excluded from the week)
    if days_in_current_year == 0:
        return f"{abysmal_year} {astro_symbols['NYD']}"

    # Adjust for Leap Day (occurs the day after NYD every 4 years)
    if is_leap_year and days_in_current_year == 1:
        return f"{abysmal_year} {astro_symbols['Leap Day']}"

    # Exclude NYD & count from Month 1, Day 1
    adjusted_day = days_in_current_year - (1 if is_leap_year else 0)

    # Compute month and day
    month = (adjusted_day // 28) + 1
    day = (adjusted_day % 28) + 1

    # Apply strikethrough to the entire month string (including spaces)
    month_display = strikethrough(str(month))

    # Calculate weekday shift (28-year rotation)
    base_weekday = "Saturday"  # Month 1, Day 1 always starts on Saturday
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Shift the weekday based on how many days have passed (accounting for NYD)
    total_shift_days = (days_since_epoch - (abysmal_year * 365)) % 7
    weekday_index = (weekdays.index(base_weekday) + total_shift_days) % 7
    weekday = weekdays[weekday_index]

    # Format the output correctly with spaced-out strikethrough month
    return f"{abysmal_year}{month_display}{day} {astro_symbols[weekday]}"

# Example Usage:
today = datetime(2025, 3, 15)  # Replace with any date
abysmal_date = get_abysmal_date(today)
print(abysmal_date)
