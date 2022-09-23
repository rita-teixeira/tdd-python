import datetime
import io
import sys
import unittest
from unittest.mock import Mock

from print_date import PrintDate, Calendar, Printer

TEST_PRINT = 'test'


class PrintDateTest(unittest.TestCase):

    @staticmethod
    def test_print_date():
        calendar = Mock(spec=Calendar)
        mock_datetime = datetime.datetime(2022, 9, 10)
        calendar.today = Mock(return_value=mock_datetime)
        sys.stdout = io.StringIO()

        print_date = PrintDate(calendar, Printer())
        print_date.print_current_date()

        assert sys.stdout.getvalue() == '2022-09-10 00:00:00\n'

    @staticmethod
    def test_printer():
        sys.stdout = io.StringIO()

        printer = Printer()
        printer.print_line(TEST_PRINT)

        assert sys.stdout.getvalue() == TEST_PRINT + '\n'



