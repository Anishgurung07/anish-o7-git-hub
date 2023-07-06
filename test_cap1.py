import unittest  
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'rahul'
        result = cap.cap_text(text)
        self.assertEqual(result,'Rahul')
    def test_multiple_word(self):
        text = 'rahul gurung'
        result = cap.cap_text(text)
        self.assertEqual(result,'Rahul Gurung')
if __name__ == '__main__':
    unittest.main()        
