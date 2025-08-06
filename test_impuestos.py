import unittest
import impuestos

class TestImpuestos(unittest.TestCase):

    def test_normal_1(self):
        #producto Leche
        precio = 5000
        tipo = "exento"
        esperado = 5000
        resultado = impuestos.calcular_valor_total(precio, tipo)
        self.assertEqual(esperado, resultado)

