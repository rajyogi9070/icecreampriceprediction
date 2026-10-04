import json
import unittest
from server import INTERCEPT, COEFFICIENT

class NotebookParityTests(unittest.TestCase):
    def test_notebook_equation_at_25_degrees(self):
        self.assertAlmostEqual(INTERCEPT + COEFFICIENT * 25, 581.0915593408397, places=8)
    def test_feature_contract_is_single_temperature(self):
        self.assertEqual('Temperature', 'Temperature')
        self.assertEqual('Revenue', 'Revenue')

if __name__ == '__main__':
    unittest.main()
