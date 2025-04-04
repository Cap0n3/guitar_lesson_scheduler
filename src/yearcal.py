# See website https://calendarmaniacs.com/

import calendar
import datetime
import re


class YearCal:
    @staticmethod
    def generate_calendar(dates):
        """
        Generate a text calendar for the year(s) of the provided list of dates,
        marking the given dates with an asterisk (*), preserving layout.

        Parameters
        ----------
        dates: List of datetime.date objects.

        Returns
        -------
        A string representation of the calendar with marked dates.
        """
        pass


    @staticmethod
    def dates_of_weekday_in_year(year, weekday):
        """
        Return a list of dates for a given weekday in a year.

        Parameters
        ----------
        year: The year as an integer.
        weekday: The weekday number (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).

        Returns
        -------
        A list of datetime.date objects for the specified weekday in the year.
        """
        dates = []

        cal = calendar.Calendar(firstweekday=calendar.MONDAY)

        # Iterate through each month and each week
        for month in range(1, 13):
            month_weeks = cal.monthdayscalendar(year, month)
            for week in month_weeks:
                if week[weekday] != 0:  # weekday is 0 for Monday, 6 for Sunday
                    dates.append(datetime.date(year, month, week[weekday]))

        return dates

    @staticmethod
    def dates_of_weekday_in_range(start_date, end_date, weekday_number):
        """
        Return a list of dates for a given weekday within a specified date range.

        Parameters
        ----------
        start_date: The start date of the range as a datetime.date object.
        end_date: The end date of the range as a datetime.date object.
            weekday_number: The weekday number (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).

        Returns
        -------
        A list of datetime.date objects for the specified weekday within the range.
        """
        dates = []
        current_date = start_date

        # Advance current_date to the first occurrence of the specified weekday
        while current_date.weekday() != weekday_number:
            current_date += datetime.timedelta(days=1)

        # Append all dates that are the specified weekday and within the range
        while current_date <= end_date:
            dates.append(current_date)
            current_date += datetime.timedelta(
                days=7
            )  # Skip to the next week's same weekday

        return dates

    @staticmethod
    def remove_matching_dates(listA, listB):
        """
        Utility method that removes dates from listA that are in listB.
        """
        # Convert listB to a set for faster lookup
        setB = set(listB)

        # Create a new list of dates from listA that are not in listB
        updated_listA = [date for date in listA if date not in setB]

        return updated_listA


class DateParser:
    @staticmethod
    def parse_french_date_range(sentence):
        """
        Parse a French date range string and return a list of datetime.date objects.

        Example:
            "1 janvier 2021 au 3 janvier 2021" -> [datetime.date(2021, 1, 1), datetime.date(2021, 1, 2), datetime.date(2021, 1, 3)]
            "Du 1 janvier 2021 jusqu'au 3 janvier 2021" -> [datetime.date(2021, 1, 1), datetime.date(2021, 1, 2), datetime.date(2021, 1, 3)]
            "le 1 janvier 2021" -> [datetime.date(2021, 1, 1)]

        Parameters
        ----------
            sentence (str): A French date range string.

        Returns
        -------
            list: A list of datetime.date objects representing the dates in the range.
        """
        months = {
            "janvier": 1,
            "février": 2,
            "mars": 3,
            "avril": 4,
            "mai": 5,
            "juin": 6,
            "juillet": 7,
            "août": 8,
            "septembre": 9,
            "octobre": 10,
            "novembre": 11,
            "décembre": 12,
        }

        date_pattern = r"(\d{1,2}) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre) (\d{4})"
        matches = re.findall(date_pattern, sentence)

        dates = []

        # Parse each match to create datetime.date objects
        for day, month, year in matches:
            date = datetime.date(int(year), months[month], int(day))
            dates.append(date)

        if len(dates) == 0 or len(dates) > 2:
            raise ValueError("Invalid date range format")

        if len(dates) == 1:
            return dates

        date_list = []
        start_date, end_date = dates[0], dates[1]

        # Check if start date is after end date
        if start_date > end_date:
            raise ValueError("Start date is after end date")

        while start_date <= end_date:
            date_list.append(start_date)
            start_date += datetime.timedelta(days=1)

        return date_list
