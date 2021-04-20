import unittest
from Polynomial.polynomial import Polynomial


class Test(unittest.TestCase):
    def test_emtpy_args_constructor(self):
        self.assertRaises(TypeError, Polynomial)

    def test_emtpy_list_constructor(self):
        self.assertRaises(ValueError, Polynomial, [])

    def test_emtpy_tuple_constructor(self):
        self.assertRaises(ValueError, Polynomial, ())

    def test_incorrect_type_constructor(self):
        self.assertRaises(TypeError, Polynomial, 1.0)

    def test_incorrect_list_constructor(self):
        self.assertRaises(TypeError, Polynomial, ["1", "2"])

    def test_change_coeffs(self):
        p = Polynomial([1, 2, 3])

        p.coeffs = [1, 0]

        self.assertEqual([1, 0], p.coeffs)

        p.coeffs.pop(0)

        self.assertEqual([0], p.coeffs)

    def test_to_str(self):
        params = [
            [1, -1, 1],
            [-1, 2, 0],
            [5],
            [1, 0, 1],
            [1, 0, 1, 1],
            [0, 10]
        ]

        results = [
            "x^2 - x + 1", "- x^2 + 2x", "5", "x^2 + 1", "x^3 + x + 1", "10"
        ]
        for i, param in enumerate(params):
            self.assertEqual(results[i], Polynomial(param).__str__(), "Incorrect string for Polynomial")

    def test_repr(self):
        self.assertEqual(Polynomial([1, 2, 3]).__repr__(), "Polynomial([1, 2, 3])")

        self.assertEqual(Polynomial((1, 2, 3)).__repr__(), "Polynomial([1, 2, 3])")

        self.assertEqual(Polynomial(1).__repr__(), "Polynomial([1])")

    def test_compare(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1])

        self.assertNotEqual(p1, p2)

        p2.coeffs.append(1)

        self.assertEqual(p1, p2)

        p2.coeffs = [0, 1, 2, 3]
        p1.coeffs = [0, 1, 2, 3]

        self.assertEqual(p1, p2)

    def test_add_int(self):
        p = Polynomial([1, 2, 3])

        res1 = p + 1
        res2 = 1 + p

        self.assertEqual([1, 2, 4], res1.coeffs)
        self.assertEqual([1, 2, 4], res2.coeffs)

    def test_add(self):
        p1 = Polynomial([1, 2, 1])
        p2 = Polynomial([1, 1])

        res1 = p1 + p2
        res2 = p2 + p1

        self.assertEqual([1, 3, 2], res1.coeffs)
        self.assertEqual([1, 3, 2], res2.coeffs)

    def test_sub_int(self):
        p1 = Polynomial([1, 2, 3])

        res1 = p1 - 2
        res2 = 2 - p1

        self.assertEqual([1, 2, 1], res1.coeffs)
        self.assertEqual([-1, -2, -1], res2.coeffs)

    def test_sub(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([2, 2])
        p3 = Polynomial([1, 1, 1])

        res1 = p1 - p2
        res2 = p2 - p1

        self.assertEqual([1, 0, 1], res1.coeffs)
        self.assertEqual([-1, 0, -1], res2.coeffs)

        res1 = p1 - p3
        res2 = p3 - p1

        self.assertEqual([1, 2], res1.coeffs)
        self.assertEqual([-1, -2], res2.coeffs)

    def test_mul_int(self):
        p1 = Polynomial([1, 1, 3])

        res1 = p1 * 2
        res2 = 2 * p1

        self.assertEqual([2, 2, 6], res1.coeffs)
        self.assertEqual([2, 2, 6], res2.coeffs)

    def test_mul(self):
        p1 = Polynomial([1, 1, 3])
        p2 = Polynomial([2, 1])
        p3 = Polynomial([1, -1, 1])

        res1 = p1 * p3
        res2 = p3 * p1

        self.assertEqual([1, 0, 3, -2, 3], res1.coeffs)
        self.assertEqual([1, 0, 3, -2, 3], res2.coeffs)

        res1 = p1 * p2
        res2 = p2 * p1

        self.assertEqual([2, 3, 7, 3], res1.coeffs)
        self.assertEqual([2, 3, 7, 3], res2.coeffs)

    def test_raise_add_incorrect_arg(self):
        p = Polynomial([1, 1, 1])
        fs = [2.0, "2.0", [2.0]]

        for f in fs:
            with self.assertRaises(TypeError):
                p + f
        for f in fs:
            with self.assertRaises(TypeError):
                f + p

    def test_raise_sub_incorrect_arg(self):
        p = Polynomial([1, 1, 1])
        fs = [2.0, "2.0", [2.0]]

        for f in fs:
            with self.assertRaises(TypeError):
                p - f
        for f in fs:
            with self.assertRaises(TypeError):
                f - p

    def test_raise_mul_incorrect_arg(self):
        p = Polynomial([1, 1, 1])
        fs = [2.0, "2.0", [2.0]]

        for f in fs:
            with self.assertRaises(TypeError):
                p * f
        for f in fs:
            with self.assertRaises(TypeError):
                f * p


if __name__ == '__main__':
    unittest.main()
