from unittest import TestCase

import turbodbc.data_types
from turbodbc import STRING, BINARY, NUMBER, DATETIME, ROWID

ALL_TYPE_CODES = [turbodbc.data_types._BOOLEAN_CODE,
                  turbodbc.data_types._INTEGER_CODE,
                  turbodbc.data_types._FLOATING_POINT_CODE,
                  turbodbc.data_types._STRING_CODE,
                  turbodbc.data_types._TIMESTAMP_CODE,
                  turbodbc.data_types._DATE_CODE]

ALL_DATA_TYPES = [STRING, BINARY, NUMBER, DATETIME, ROWID]

class TestDataTypes(TestCase):
    def test_each_type_code_matches_one_data_type(self):
        for type_code in ALL_TYPE_CODES:
            matches = [type for type in ALL_DATA_TYPES if type_code == type]
            self.assertEqual(1, len(matches))

    def test_each_type_code_matches_all_but_one_data_type(self):
        for type_code in ALL_TYPE_CODES:
            mismatches = [type for type in ALL_DATA_TYPES if type_code != type]
            expected = len(ALL_DATA_TYPES) - 1
            self.assertEqual(expected, len(mismatches))    