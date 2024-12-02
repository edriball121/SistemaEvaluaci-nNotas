import unittest
from unittest.mock import patch, MagicMock
import os
from main import (
    notas,
    solicitar_notas_basicas,
    agregar_asignaturas,
    ingresar_nota,
    calcular_promedio,
    mostrar_notas,
    generar_reporte_csv
)

class TestSistemaNotas(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        """
        notas.clear()  # Limpiar las notas antes de cada prueba

    def test_ingresar_notas_basicas(self):
        """
        Prueba el flujo de ingresar notas básicas.
        """
        # Arrange
        inputs = iter(["4.5", "3.8", "5.0"])  # Notas válidas para Matemáticas, Ciencia y Lenguaje

        # Act
        with patch("builtins.input", lambda _: next(inputs)):
            solicitar_notas_basicas()

        # Assert
        self.assertEqual(notas["Matemáticas"], 4.5)
        self.assertEqual(notas["Ciencia"], 3.8)
        self.assertEqual(notas["Lenguaje"], 5.0)

    def test_agregar_asignaturas(self):
        """
        Prueba el flujo de agregar asignaturas nuevas.
        """
        # Arrange
        inputs = iter(["Historia", "Filosofía", "salir"])

        # Act
        with patch("builtins.input", lambda _: next(inputs)):
            agregar_asignaturas()

        # Assert
        self.assertIn("Historia", notas)
        self.assertIn("Filosofía", notas)
        self.assertIsNone(notas["Historia"])
        self.assertIsNone(notas["Filosofía"])

    def test_ingresar_nota_fuera_de_rango(self):
        """
        Prueba ingresar una nota fuera del rango permitido.
        """
        # Arrange
        inputs = iter(["6", "-1", "4.0"])  # Notas inválidas seguidas de una válida

        # Act
        with patch("builtins.input", lambda _: next(inputs)):
            nota = ingresar_nota("Historia")

        # Assert
        self.assertEqual(nota, 4.0)

    def test_ingresar_nota_no_numero(self):
        """
        Prueba ingresar un valor no numérico como nota.
        """
        # Arrange
        inputs = iter(["abc", "2.5"])  # Entrada inválida seguida de una válida

        # Act
        with patch("builtins.input", lambda _: next(inputs)):
            nota = ingresar_nota("Filosofía")

        # Assert
        self.assertEqual(nota, 2.5)

    def test_calcular_promedio(self):
        """
        Prueba el cálculo del promedio.
        """
        # Arrange
        notas.update({"Matemáticas": 4.0, "Ciencia": 3.0, "Lenguaje": 5.0})

        # Act
        promedio = calcular_promedio()

        # Assert
        self.assertAlmostEqual(promedio, 4.0, places=2)

    def test_generar_reporte_csv(self):
        """
        Prueba la generación de un reporte en CSV.
        """
        # Arrange
        notas.update({"Matemáticas": 4.0, "Ciencia": 3.0, "Lenguaje": 5.0})

        # Act
        generar_reporte_csv()

        # Assert
        self.assertTrue(os.path.exists("reporte_notas.csv"))
        with open("reporte_notas.csv", "r") as archivo:
            contenido = archivo.readlines()
        self.assertEqual(contenido[0].strip(), "Asignatura,Nota")
        self.assertIn("Matemáticas,4.0", contenido[1])
        self.assertIn("Ciencia,3.0", contenido[2])
        self.assertIn("Lenguaje,5.0", contenido[3])

if __name__ == "__main__":
    unittest.main()
