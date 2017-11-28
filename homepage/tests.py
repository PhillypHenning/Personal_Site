import unittest

def testx(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(testx(3),4)

if __name__ == '__main__':
    unittest.main()