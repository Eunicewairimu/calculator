from unittest import TestCase

class AddTest(TestCase):
    def test_it_adds_correctly(self):
        self.assertEqual(add(4, 4), 8)

    def test_correct_input(self):
        with self.assertRaises(TypeError):
            add("5", 6)