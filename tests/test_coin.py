import unittest
from coin import coin


class CoinTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_flip(self):
        newcoin = coin.Coin()
        side = newcoin.flip()
        self.assertTrue(side == 1 or side == 0)
    
    def test_set_side(self):
        newcoin = coin.Coin()
        side = newcoin.set_side(1)
        self.assertEqual(side, 1)
    
    def test_set_side_exception(self):
        newcoin = coin.Coin()
        with self.assertRaises(coin.OutOfRange):
            newcoin.set_side(2)

    def test_get_side(self):
        newcoin = coin.Coin()
        side = newcoin.get_side()
        self.assertEqual(side, 1)
