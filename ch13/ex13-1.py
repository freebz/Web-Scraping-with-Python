# CHAPTER 13 스크레이퍼로 웹사이트 테스트하기

# 13.1 테스트 입문

# 13.1.1 단위 테스트란?

# 13.1.2 파이썬 unittest

import unittest
class TestAddition(unittest.TestCase):
    def setUp(self):
        print("Setting up the test")
    def tearDown(self):
        print("Tearing down the test")
    def test_twoPlusTwo(self):
        total = 2+2
        self.assertEqual(4, total);
if __name__ == '__main__':
    unittest.main()

