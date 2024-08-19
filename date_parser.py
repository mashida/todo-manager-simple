"""
Module for functions to parse dates
"""
from datetime import datetime

def is_date(date: str) -> bool:
    """
    Function to check if string is date according to format
    :param date: string representing date
    :return: True if string is date according to format, else False
    """
    date_format = "%Y-%m-%d"

    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False