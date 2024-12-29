import unittest
import main

class TestLocation(unittest.TestCase):
    def test_locations_eq(self):
        """Test Location __eq__."""
        self.assertEqual(main.Location(1, 2),  main.Location(1, 2))
        self.assertEqual(main.Location(0, 0),  main.Location(0, 0))
        self.assertNotEqual(main.Location(0, 0),  main.Location(1, 0))

    def test_locations_eq_type_exeption(self):
        """Test Location __eq__ exception for cases of different type."""
        with self.assertRaises(ValueError):
            _ = main.Location(0, 0) == (0, 0)

    def test_locations_copy(self):
        """Checks for Location().copy()"""
        l1 = main.Location(1, 2)
        l2 = l1.copy()
        self.assertEqual(l1,  l2)
        self.assertEqual(type(l1),  type(l1))
        self.assertNotEqual(id(l1),  id(l2))

if __name__ == "__main__":
    unittest.main()

