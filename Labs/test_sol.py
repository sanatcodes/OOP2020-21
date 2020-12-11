import unittest
from python_testing import TypesAndStrings


class TestMyStrings(unittest.TestCase):

    # set up all necessary variables used during the test
    def setUp(self):
        self.ts = TypesAndStrings()
        self.value = ["HALLO", 123]

    def test_last(self):
        #this calls the method from the main file and saves it in result
        result = self.ts.last_char(self.value[0])
        #compares the value of function call and the actual solution
        self.assertEqual(result, self.value[0][-1])

    @unittest.expectedFailure
    def test_last_expect_failiure(self):
        result = self.ts.last_char(self.value[0])
        self.assertEqual(result, self.value[0][0])

    def test_replacing_a(self):
        result = self.ts.replace_all_a(self.value[0])
        self.assertNotIn(result, 'a')





if __name__ == "__main__":
    unittest.main()