#!/usr/bin/env python3
# Instructors: Dr. Scott Rixner, Dr. Joe Warren
# Course: Python Programming Essentials, University of Michigan, Coursera.
#

"""
Coursera course project: working with dates
From "Python Programming Essentials" course from Rice university
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if month == 12:
        next_month = 1
        next_year = year+1
    else:
        next_year = year
        next_month = month+1
    
    return (datetime.date(next_year, next_month, 1) - datetime.date(year, month, 1)).days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    try:
        datetime.date(year, month,day)
        return True
    except ValueError:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    
    if date1 > date2:
        return 0
    
    
    return (date2-date1).days


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """

    today = datetime.date.today()
    return days_between(year, month, day, today.year, today.month, today.day)




