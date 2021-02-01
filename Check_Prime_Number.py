import unittest
import prime_number


class testPrime(unittest.TestCase):
    def checkSingleDigit(self):
        a = 3
        result = prime_number.check_prime(a)
        self.assertEquals(result, "Prime Number")

    def checkDoubleDigit(self):
        b = 11
        result = prime_number.check_prime(b)
        self.assertEquals(result, "Prime Number")


if __name__ == "__main__":
    unittest.main()
