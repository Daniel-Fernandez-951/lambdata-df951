import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)
        prod_e = Product('High', flammability=15, weight=1)
        self.assertEqual(prod_e.explode(), ". . .boom")
        prod_s = Product('Seal', price=1, weight=2)
        self.assertEqual(prod_s.stealability(), "Kinda stealable")

class AcmeReportTests(unittest.TestCase):
    """ Test reports """
    def test_default_num_products(self):
        """ Test number of products = default """
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """ Check if names are from lists """
        prod = generate_products()
        print(prod[range()].name)
        # self.assertEqual(generate_products().name, )




if __name__ == '__main__':
    unittest.main()