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
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidLessThanAsk(self):
        quotes = [
            {'top_ask': {'price': 127.6, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 122.89, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 124.98, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 118.34, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getRatio_positiveIntegers(self):
        price_a, price_b = 10, 5
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio, "Incorrect ratio calculation")

    def test_getRatio_priceAZero(self):
        price_a, price_b = 0, 5
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio, "Incorrect ratio calculation")

    def test_getRatio_priceBZero(self):
        price_a, price_b = 10, 0
        expected_ratio = None  # Can't divide by Zero, avoid throwing ZeroDivisionError
        self.assertEqual(getRatio(price_a, price_b), expected_ratio, "Incorrect ratio calculation")

    def test_getRatio_negativeIntegers(self):
        price_a, price_b = -10, -5
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio, "Incorrect ratio calculation")


if __name__ == '__main__':
    unittest.main()
