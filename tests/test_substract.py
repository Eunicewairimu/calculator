from unittest import TestCase
from app.subtract import subtract

class SubtractionTest(TestCase):
    def test_it_subtracts_correctly(self):
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(500, 50), 450)

    def test_correct_input(self):
        with self.assertRaises(TypeError):
            subtract([5], 6)