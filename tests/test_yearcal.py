import sys
import os
import unittest
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.yearcal import YearCal, DateParser

class TestYearcal(unittest.TestCase):
    def test_generate_calendar(self):
        pass

    def test_dates_of_weekday_in_year(self):
        # Test that the function returns the correct number of dates
        mondays = YearCal.dates_of_weekday_in_year(2021, 0)
        self.assertEqual(len(mondays), 52)

        # Test that the function returns the correct dates
        self.assertEqual(mondays[0], datetime.date(2021, 1, 4))
        self.assertEqual(mondays[-1], datetime.date(2021, 12, 27))

        tuesdays = YearCal.dates_of_weekday_in_year(2021, 1)
        self.assertEqual(len(tuesdays), 52)

        self.assertEqual(tuesdays[0], datetime.date(2021, 1, 5))
        self.assertEqual(tuesdays[-1], datetime.date(2021, 12, 28))

        wednesdays = YearCal.dates_of_weekday_in_year(2021, 2)
        self.assertEqual(len(wednesdays), 52)

        self.assertEqual(wednesdays[0], datetime.date(2021, 1, 6))
        self.assertEqual(wednesdays[-1], datetime.date(2021, 12, 29))

        thursdays = YearCal.dates_of_weekday_in_year(2021, 3)
        self.assertEqual(len(thursdays), 52)

        self.assertEqual(thursdays[0], datetime.date(2021, 1, 7))
        self.assertEqual(thursdays[-1], datetime.date(2021, 12, 30))

        fridays = YearCal.dates_of_weekday_in_year(2021, 4)
        self.assertEqual(len(fridays), 53)

        self.assertEqual(fridays[0], datetime.date(2021, 1, 1))
        self.assertEqual(fridays[-1], datetime.date(2021, 12, 31))

        saturdays = YearCal.dates_of_weekday_in_year(2021, 5)
        self.assertEqual(len(saturdays), 52)

        self.assertEqual(saturdays[0], datetime.date(2021, 1, 2))
        self.assertEqual(saturdays[-1], datetime.date(2021, 12, 25))

        sundays = YearCal.dates_of_weekday_in_year(2021, 6)
        self.assertEqual(len(sundays), 52)

        self.assertEqual(sundays[0], datetime.date(2021, 1, 3))
        self.assertEqual(sundays[-1], datetime.date(2021, 12, 26))

    def test_remove_matching_dates(self):
        listA = [
            datetime.date(2021, 1, 1),
            datetime.date(2021, 1, 2),
            datetime.date(2021, 1, 3),
            datetime.date(2021, 1, 4),
            datetime.date(2021, 1, 5),
            datetime.date(2021, 1, 6),
            datetime.date(2021, 1, 7),
            datetime.date(2021, 1, 8),
            datetime.date(2021, 1, 9),
            datetime.date(2021, 1, 10)
        ]

        listB = [
            datetime.date(2021, 1, 1),
            datetime.date(2021, 1, 3),
            datetime.date(2021, 1, 5),
            datetime.date(2021, 1, 7),
            datetime.date(2021, 1, 9)
        ]

        updated_listA = YearCal.remove_matching_dates(listA, listB)
        self.assertEqual(updated_listA, [
            datetime.date(2021, 1, 2),
            datetime.date(2021, 1, 4),
            datetime.date(2021, 1, 6),
            datetime.date(2021, 1, 8),
            datetime.date(2021, 1, 10)
        ])

        
class TestDateParser(unittest.TestCase):    
    def test_parse_french_date_range(self):
        false_date_range = "1 janvier 2021 au 3 janvier 2020"
        self.assertRaises(ValueError, DateParser.parse_french_date_range, false_date_range)

        false_date_range = "1 janvier 2021 au 3 janvier 2021 au 5 janvier 2021"
        self.assertRaises(ValueError, DateParser.parse_french_date_range, false_date_range)

        empty_date_range = ""
        self.assertRaises(ValueError, DateParser.parse_french_date_range, empty_date_range)

        one_date = "le 1 janvier 2021"
        dates = DateParser.parse_french_date_range(one_date)
        self.assertEqual(dates, [datetime.date(2021, 1, 1)])

        date_range = "lundi 21 octobre 2024 au mercredi 23 octobre 2024"
        dates = DateParser.parse_french_date_range(date_range)
        self.assertEqual(dates, [
            datetime.date(2024, 10, 21), 
            datetime.date(2024, 10, 22), 
            datetime.date(2024, 10, 23)
        ])

        date_range = "le lundi 1 novembre 2025, au moins jusqu'au 7 novembre 2025"
        dates = DateParser.parse_french_date_range(date_range)
        self.assertEqual(dates, [
            datetime.date(2025, 11, 1), 
            datetime.date(2025, 11, 2), 
            datetime.date(2025, 11, 3), 
            datetime.date(2025, 11, 4), 
            datetime.date(2025, 11, 5),
            datetime.date(2025, 11, 6),
            datetime.date(2025, 11, 7),
        ])

if __name__ == "__main__":
    unittest.main()