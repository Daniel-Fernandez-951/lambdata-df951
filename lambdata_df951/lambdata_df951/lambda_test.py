"""
Unit Test lambdata_df951 Module
"""

import unittest
import pandas as pd
import numpy as np
# Import Module for inspection
from example_mod import DfTools as dft


class LambdataTest(unittest.TestCase):
    """Testing Lambdata Module; ensure 100% success."""
    df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                      columns=['a', 'b', 'c'])

    def test_type(self):
        """Testing data type of input"""
        self.assertTrue(isinstance(LambdataTest.df, pd.DataFrame))
        self.assertTrue(dft.total_nul(df=LambdataTest.df), str)

    def test_shape(self):
        self.assertEqual(dft.rand_df(LambdataTest.df).shape,
                         LambdataTest.df.shape)


if __name__ == "__main__":
    unittest.main()
