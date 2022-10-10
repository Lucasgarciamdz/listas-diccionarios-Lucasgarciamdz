import unittest
from valores_repetidos import buscar_repetidos


class Equalvalues(unittest.TestCase):

    def test_repetidos(self):
        repetidos = buscar_repetidos([1, 2, 4, 1, 3, 1, 1])
        self.assertEqual(repetidos, {1: 4, 2: 1, 4: 1, 3: 1})

    def test_diferentes(self):
        diferentes = buscar_repetidos([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(diferentes, {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1
        })

    def test_letra(self):
        letras = buscar_repetidos([1, "A", 2, 3, "A"])
        self.assertEqual(letras, {1: 1, "A": 2, 2: 1, 3: 1})

    def test_vacio(self):
        vacio = buscar_repetidos([])
        self.assertEqual(vacio, {})

    def test_espacio(self):
        espacio = buscar_repetidos([" "])
        self.assertEqual(espacio, {" ": 1})

    def test_mismo_numero(self):
        mismo_numero = buscar_repetidos([1, 1, 1, 1, 1, 1])
        self.assertEqual(mismo_numero, {1: 6})


if __name__ == "__main__":
    unittest.main()
