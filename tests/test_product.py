from unittest import TestCase

class ProductTest(TestCase):
    def test_it_multiplys_correctly(self):
        self.assertEqual(multiply(4, 4), 16)

    def test_correct_input(self):
        with self.assertRaises(TypeError):
            multiply("5", 6)