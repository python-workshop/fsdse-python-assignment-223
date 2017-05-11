from unittest import TestCase


class TestBuild(TestCase):
#Check whether the string is there or not
#check whether the length is there or not
#check whether the calc of len is proper

    def test_whether_the_string_is_there_or_not(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import False")

            result = build(None,2)
            self.assertEqual(False,result)

    def test_whether_the_length_is_there_or_not(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import False")

            result = build("sdfr",None)
            self.assertEqual(False,result)

    def test_whether_the_calc_of_len_is_proper(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import False")

            result = build("sdfr",1)
            self.assertEqual(2,result)