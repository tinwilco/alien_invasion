import unittest
from ship import Ship
from unittest.mock import MagicMock


class TestShip(unittest.TestCase):
    def setup(self):
        mock_ai_game = MagicMock()
        mock_ai_game.screen.get_rect().return_value = 500, 500
        self.ship = Ship(mock_ai_game)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_center_ship(self):
        self.ship.center_ship()
        self.assertEquals(self.ship.x, 0, "ship should be in centre at ")

    if __name__ == '__main__':
        unittest.main()
