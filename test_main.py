import unittest
import main

class TestLocation(unittest.TestCase):
    """Tests for main.Location."""
    def test_locations_eq(self):
        """Test __eq__."""
        self.assertEqual(main.Location(1, 2),  main.Location(1, 2))
        self.assertEqual(main.Location(0, 0),  main.Location(0, 0))
        self.assertNotEqual(main.Location(0, 0),  main.Location(1, 0))

    def test_locations_eq_type_exeption(self):
        """Test __eq__ exception for cases of different type."""
        with self.assertRaises(ValueError):
            _ = main.Location(0, 0) == (0, 0)

    def test_locations_copy(self):
        """Checks for .copy()"""
        l1 = main.Location(1, 2)
        l2 = l1.copy()
        self.assertEqual(l1,  l2)
        self.assertEqual(type(l1),  type(l1))
        self.assertNotEqual(id(l1),  id(l2))

class TestRandomizer(unittest.TestCase):
    """Tests for main.Randomizer."""
    def setUp(self):
        self.grid_size_x = 3
        self.grid_size_y = 3
        self.map_bounderies = main.MapBoundaries(
                x = (0, self.grid_size_x - 1),
                y = (0, self.grid_size_y - 1)
        )

    def test_create_random_location(self):
        """Tests for .create_random_location()"""
        randomizer = main.Randomizer(1, self.map_bounderies)
        rand_loc = randomizer.create_random_location()
        self.assertTrue(isinstance(rand_loc, main.Location))
        self.assertTrue(isinstance(rand_loc.x, int))
        self.assertTrue(isinstance(rand_loc.y, int))

if __name__ == "__main__":
    unittest.main()

