import unittest
from modules.product_stock import is_product_available
from modules.validate_discount_code import validate_discount_code

class Test(unittest.TestCase):
    def test_is_product_available(self):
        self.assertEquals(is_product_available('Chocolate','2'),True)
        self.assertEquals(is_product_available('Chocolate','9000'),False)

    def test_validate_discount_code(self):
        self.assertEquals(validate_discount_code("primavera2021"),True)
        self.assertEquals(validate_discount_code("primaverA2023"),False)

