import unittest
import sqlite3
from ventana_seguridad import (
    agregar_contraseña,
    obtener_contraseñas,
    actualizar_contraseña,
    eliminar_contraseña,
    generar_contrasena_segura,
)

class TestGestorContraseñas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear una base de datos en memoria para pruebas
        cls.conexion = sqlite3.connect(":memory:")
        cursor = cls.conexion.cursor()
        cursor.execute("""
            CREATE TABLE contrasenas_servicios (
                servicio TEXT PRIMARY KEY,
                usuario TEXT NOT NULL,
                contrasena TEXT NOT NULL
            )
        """)
        cls.conexion.commit()

    @classmethod
    def tearDownClass(cls):
        # Cerrar la conexión a la base de datos
        cls.conexion.close()

    def test_obtener_contraseñas(self):
        # Agregar datos de prueba
        agregar_contraseña("Servicio2", "Usuario2", "Contraseña2")

        # Obtener contraseñas y verificar
        contrasenas = obtener_contraseñas()
        self.assertIn(("Servicio2", "Usuario2", "Contraseña2"), contrasenas)

    def test_generar_contrasena_segura(self):
        contrasena = generar_contrasena_segura(12)

        # Validar longitud
        self.assertEqual(len(contrasena), 12)

        # Validar que contenga al menos un dígito
        self.assertTrue(any(c.isdigit() for c in contrasena))

        # Validar que contenga al menos una letra minúscula
        self.assertTrue(any(c.islower() for c in contrasena))

        # Validar que contenga al menos una letra mayúscula
        self.assertTrue(any(c.isupper() for c in contrasena))

        # Validar que contenga al menos un carácter especial
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;':,./<>?" for c in contrasena))

if __name__ == "__main__":
    unittest.main()
