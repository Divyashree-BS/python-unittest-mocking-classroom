from unittest import TestCase, mock
from unittest.mock import patch
import src
from mock import Mock
from mockito import *
from src.db_helper import DbHelper


class Test_Db_Helper(TestCase):
    def setUp(self):
        pass

    def test_max_salary_is_greater_than_min_salary(self):
        db_helper = Mock()
        with patch('src.db_helper.DbHelper', attr_or_replacement=True):
            when(db_helper).get_maximum_salary().thenReturn(50000.00)
            when(db_helper).get_minimum_salary().thenReturn(30000.00)

            self.assertGreater(db_helper.get_maximum_salary(),db_helper.get_minimum_salary())