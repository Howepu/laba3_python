

import unittest
from app import app

class TestVolumeCalculator(unittest.TestCase):

    # проверить запрос GET на корневой URL
    def test_index_get(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # проверить запрос POST на корневой URL-адрес с данными сферы
    def test_index_post_sphere(self):
        tester = app.test_client(self)
        response = tester.post("/", data=dict(
            shape="sphere",
            precision=3,
            radius=2.5
        ), follow_redirects=True)
        status_code = response.status_code
        volume = response.data.decode("utf-8")
        self.assertEqual(status_code, 200)
        self.assertIn("Sphere", volume)
        self.assertIn("volume is 65.45", volume)

    # проверить запрос POST на корневой URL-адрес с данными конуса
    def test_index_post_cone(self):
        tester = app.test_client(self)
        response = tester.post("/", data=dict(
            shape="cone",
            precision=2,
            radius=5,
            height=12
        ), follow_redirects=True)
        status_code = response.status_code
        volume = response.data.decode("utf-8")
        self.assertEqual(status_code, 200)
        self.assertIn("Cone", volume)
        self.assertIn("volume is 314.16", volume)

    # проверить запрос POST на корневой URL-адрес с данными цилиндра
    def test_index_post_cylinder(self):
        tester = app.test_client(self)
        response = tester.post("/", data=dict(
            shape="cylinder",
            precision=4,
            radius=3,
            height=6.5
        ), follow_redirects=True)
        status_code = response.status_code
        volume = response.data.decode("utf-8")
        self.assertEqual(status_code, 200)
        self.assertIn("Cylinder", volume)
        self.assertIn("volume is 169.646", volume)

if __name__ == "__main__":
    unittest.main()

