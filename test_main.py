import unittest
import main

class TestMain(unittest.TestCase):
    def test_locations_eq(self):
        """Test Location __eq__."""
        self.assertEqual(main.Location(1, 2),  main.Location(1, 2))
        self.assertEqual(main.Location(0, 0),  main.Location(0, 0))
        self.assertNotEqual(main.Location(0, 0),  main.Location(1, 0))

    def test_locations_eq_type_exeption(self):
        """Test Location __eq__ exception for cases of different type."""
        with self.assertRaises(ValueError):
            _ = main.Location(0, 0) == (0, 0)

if __name__ == "__main__":
    unittest.main()

