"""
Module for functions to parse dates
"""
from datetime import datetime

FORMATS = [
    "%Y-%m-%d",
    "%Y/%m/%d"
]


def is_date_by_format(date: str, date_format: str) -> bool:
    """
    Function to check if string is date according to format
    :param date: string representing date
    :param date_format: string representing date format
    :return: True if string is date according to format, else False
    """

    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False


def is_date(date: str) -> bool:
    """
    Function to check if date is a string according to at list one of FORMATS
    :param date: string representing date
    :return: True is date is_date_by one format out of FORMATS
    """

    for date_format in FORMATS:
        if is_date_by_format(date, date_format):
            return True
    return False
