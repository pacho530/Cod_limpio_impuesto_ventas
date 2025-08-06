import unittest
from impuestos import CalculadoraImpuestos

class TestImpuestos(unittest.TestCase):

    def test_normal_1(self):
        #producto Leche
        #entradas
        precio = 5000
        tipo = "exento"

        #proceso
        resultado = CalculadoraImpuestos.calcular_valor_total(precio, tipo)

        #salidas
        esperado = 5000
        self.assertEqual(esperado, resultado)

    def test_normal_2(self):
        #producto perfume
        #entradas
        precio = 100000
        tipo = "IVA 19%"

        #proceso
        resultado = CalculadoraImpuestos.calcular_valor_total(precio, tipo)

        #salidas
        esperado = 119000
        self.assertEqual(esperado, resultado)

    def test_normal_3(self):
        #producto Hamburguesa
        #entradas
        precio = 15000
        tipo = "INC 8%"

        #proceso
        resultado = CalculadoraImpuestos.calcular_valor_total(precio, tipo)

        #salidas
        esperado = 16200
        self.assertEqual(esperado, resultado)

    def test_normal_4(self):
        #producto bolsa plastica
        # entradas
        precio = 0
        tipo = "bolsa"

        #proceso
        resultado = CalculadoraImpuestos.calcular_valor_total(precio, tipo)

        #salidas
        esperado = 50
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    unittest.main()

