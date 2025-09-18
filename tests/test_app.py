import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.app import app
from src import services

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_address(self):
        response = self.app.get("/endereco/60534170")
        self.assertEqual(response.status_code, 200)
        self.assertIn("logradouro", response.get_json())

    def test_coord(self):
        response = self.app.get("/coordenadas/60534170")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("latitude", data)
        self.assertIn("longitude", data)
        
    def test_temp(self):
        response = self.app.get("/temperatura/60534170")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("temperatura", data)
        self.assertIn("cidade", data)

if __name__ == "__main__":
    unittest.main()