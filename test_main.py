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
        map_boundaries = main.MapBoundaries(
                x = (0, 3),
                y = (0, 3)
        )
        main.GLOBALS["MAP_BOUNDARIES"] = map_boundaries
        self.randomizer = main.Randomizer(1)

    def test_create_random_location(self):
        """Tests for .create_random_location()"""
        rand_loc = self.randomizer.create_random_location()
        self.assertIsInstance(rand_loc, main.Location)
        self.assertIsInstance(rand_loc.x, int)
        self.assertIsInstance(rand_loc.y, int)

class TestHunter(unittest.TestCase):
    """Tests for main.Hunter."""
    def setUp(self):
        self.hunter = main.Hunter(main.Location(0, 0))

    def test_creation(self):
        self.assertIsInstance(self.hunter, main.Hunter)
        self.assertTrue(self.hunter.sign, "H")
        self.assertIsInstance(self.hunter.get_location(), main.Location)

class TestPrey(unittest.TestCase):
    """Tests for main.Prey."""
    def setUp(self):
        self.prey_alive = main.Prey("Prey_test1", main.Location(0, 0))
        self.prey_dead = main.Prey("Prey_test1", main.Location(0, 0))
        self.prey_dead.kill()

    def test_creation(self):
        self.assertIsInstance(self.prey_alive, main.Prey)
        self.assertTrue(self.prey_alive.sign, "P")
        self.assertIsInstance(self.prey_alive.get_location(), main.Location)

    def test_kill(self):
        self.assertTrue(self.prey_dead.sign, "X")
        self.assertFalse(self.prey_dead._is_alive)

class TestPlayerMovement(unittest.TestCase):
    """Test movement related behaviour."""
    def setUp(self):
        # Setup minimal boundaries
        self.map_boundaries = main.MapBoundaries(x=(0, 1), y=(0, 1))
        main.GLOBALS["MAP_BOUNDARIES"] = self.map_boundaries
        self.hunter = main.Hunter(location=main.Location(0, 0))

    def test_move_left_at_boundary(self):
        """Test not to cross the left boundary."""
        # The hunter is at x=0; moving left should keep x=0
        self.hunter.move('left')
        self.assertEqual(self.hunter.get_location().x, 0)
        self.assertEqual(self.hunter.get_location().y, 0)

    def test_move_up_within_boundary(self):
        """Test not to cross the up boundary."""
        # With y boundary = 1, if y=0 => up => y=1
        self.hunter.move('up')
        self.assertEqual(self.hunter.get_location().x, 0)
        self.assertEqual(self.hunter.get_location().y, 1)

if __name__ == "__main__":
    unittest.main()
