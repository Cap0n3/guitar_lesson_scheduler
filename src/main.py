from yearcal import YearCal, DateParser
import datetime

if __name__ == "__main__":
    holidays = [
        "du lundi 23 octobre 2023 au vendredi 27 octobre 2023",
        "du lundi 25 décembre 2023 au vendredi 5 janvier 2024",
        "du lundi 19 février 2024 au vendredi 23 février 2024",
        "du vendredi 29 mars 2024 au vendredi 12 avril 2024",
        "le mercredi 1 mai 2024",
        "les jeudi 9 mai 2024",
        "le lundi 20 mai 2024",
    ]

    datetime_holidays = []
    for holiday in holidays:
        dates = DateParser.parse_french_date_range(holiday)
        datetime_holidays.extend(dates)

    # Get all monday dates for school year 2023-2024
    mondays = YearCal.dates_of_weekday_in_range(
        datetime.date(2023, 9, 1), datetime.date(2024, 6, 30), 0
    )

    # Remove all holidays from the list of mondays
    lesson_mondays = YearCal.remove_matching_dates(mondays, datetime_holidays)

    # print(len(lesson_mondays))
    print(lesson_mondays)
    print(YearCal.generate_calendar(lesson_mondays))
