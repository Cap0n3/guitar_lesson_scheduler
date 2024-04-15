from yearcal import YearCal, DateParser

if __name__ == "__main__":
    holidays = [
        "lundi 19 août 2024",
        "jeudi 5 septembre 2024",
        "lundi 21 octobre 2024 au vendredi 25 octobre 2024",
        "lundi 23 décembre 2024 au vendredi 3 janvier 2025"
    ]

    datetime_holidays = []
    for holiday in holidays:
        dates = DateParser.parse_french_date_range(holiday)
        datetime_holidays.extend(dates)

    # Get all monday dates in 2024
    mondays = YearCal.dates_of_weekday_in_year(2024, 0)

    # Remove all holidays from the list of mondays
    lesson_mondays = YearCal.remove_matching_dates(mondays, datetime_holidays)

    print(lesson_mondays)
