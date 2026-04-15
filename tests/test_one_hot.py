import unittest
from one_hot_encoder import fit_transform


class TestCountLetters(unittest.TestCase):
    def test_list(self):
        result = fit_transform(['Apple', 'Cider', 'Banana'])
        exp = [
            ('Apple', [0, 0, 1]),
            ('Cider', [0, 1, 0]),
            ('Banana', [1, 0, 0])
        ]
        self.assertEqual(result, exp)

    def test_arguments(self):
        result = fit_transform('Apple', 'Cider', 'Banana')
        exp = [
            ('Apple', [0, 0, 1]),
            ('Cider', [0, 1, 0]),
            ('Banana', [1, 0, 0])
        ]
        self.assertEqual(result, exp)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_clearance(self):
        fit_transform('Apple', 'Banana')
        result_animals = fit_transform('Dog', 'Cat', 'Elephant')
        self.assertNotIn('Apple', result_animals)
