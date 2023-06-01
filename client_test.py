import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])

        expected_bid_price = 120.48
        expected_ask_price = 121.2

        expected_price = (expected_ask_price + expected_bid_price) / 2
        self.assertEqual(bid_price, expected_bid_price, "Incorrect bid price")
        self.assertEqual(ask_price, expected_ask_price, "Incorrect ask price")
        self.assertEqual(price, expected_price, "Incorrect price calculation")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])

        expected_bid_price = 120.48
        expected_ask_price = 119.2

        self.assertEqual(bid_price, expected_bid_price, "Incorrect bid price")
        self.assertEqual(ask_price, expected_ask_price, "Incorrect ask price")
        self.assertGreater(bid_price, ask_price, "Bid price is not greater than ask price")

    def test_getDataPoint_calculatePriceBidLessThanAsk(self):
        quotes = [
            {'top_ask': {'price': 127.6, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 122.89, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 124.98, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 118.34, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[1])

        expected_bid_price = 118.34
        expected_ask_price = 124.98

        self.assertEqual(bid_price, expected_bid_price, "Incorrect bid price")
        self.assertEqual(ask_price, expected_ask_price, "Incorrect ask price")
        self.assertLess(bid_price, ask_price, "Bid price is not greater than ask price")

    def test_getRatio_positiveIntegers(self):
        price_a = 10
        price_b = 5
        expected_ratio = price_a / price_b
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, expected_ratio, "Incorrect ratio calculation")

    def test_getRatio_priceAZero(self):
        price_a = 0
        price_b = 5
        expected_ratio = price_a / price_b
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, expected_ratio, "Incorrect ratio calculation")

    def test_getRatio_priceBZero(self):
        price_a = 10
        price_b = 0
        expected_ratio = None  # Can't divide by Zero, avoid throwing ZeroDivisionError
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, expected_ratio, "Incorrect ratio calculation")

    def test_getRatio_negativeIntegers(self):
        price_a = -10
        price_b = -5
        expected_ratio = price_a / price_b
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, expected_ratio, "Incorrect ratio calculation")


if __name__ == '__main__':
    unittest.main()
