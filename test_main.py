import unittest
import main

class TestMain(unittest.TestCase):
    def test_locations_eq(self):
        self.assertEqual(main.Location(1, 2),  main.Location(1, 2))
        self.assertEqual(main.Location(0, 0),  main.Location(0, 0))
        self.assertNotEqual(main.Location(0, 0),  main.Location(1, 0))

if __name__ == "__main__":
    unittest.main()

