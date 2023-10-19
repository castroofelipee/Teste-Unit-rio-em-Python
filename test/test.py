import unittest


class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


class TesteCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(5, 2), 3)

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(5, 2), 10)

    def test_divisao(self):
        self.assertEqual(self.calc.divisao(6, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.divisao(5, 0)


if __name__ == '__main__':
    unittest.main()
