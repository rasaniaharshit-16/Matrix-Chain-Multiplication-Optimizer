
import unittest
from matrix_chain import matrix_chain_order, optimal_order


class TestMatrixChain(unittest.TestCase):

    def test_four_matrices(self):
        p = [10, 20, 30, 40, 30]
        dp, split = matrix_chain_order(p)

        self.assertEqual(dp[0][3], 30000)
        self.assertEqual(
            optimal_order(split, 0, 3),
            "(((A1 x A2) x A3) x A4)"
        )

    def test_two_matrices(self):
        dp, split = matrix_chain_order([10, 20, 30])
        self.assertEqual(dp[0][1], 6000)

    def test_single_matrix(self):
        dp, split = matrix_chain_order([10, 20])
        self.assertEqual(dp[0][0], 0)

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            matrix_chain_order([10, -20, 30])


if __name__ == "__main__":
    unittest.main()
