import hashlib
import sqlite3

class Login:
    @staticmethod
    def validar_credenciales(alias, contrasena):
        """Valida si las credenciales son correctas."""
        hashed_password = Login.hash_password(contrasena)

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "SELECT * FROM usuarios WHERE nombre = ? AND contrasena = ?",
                (alias, hashed_password),
            )
            usuario = cursor.fetchone()
            return usuario is not None
        finally:
            conexion.close()

    @staticmethod
    def recuperar_contrasena(alias):
        """Simula la recuperación de contraseña enviando el enlace al correo del usuario."""
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT correo FROM usuarios WHERE nombre = ?", (alias,))
            usuario = cursor.fetchone()
            if usuario:
                correo = usuario[0]
                print(f"Enlace para restablecer contraseña enviado a {correo}.")
                return f"Se ha enviado el enlace al correo registrado: {correo}"
            return "Alias no encontrado. Verifique sus datos."
        finally:
            conexion.close()

    @staticmethod
    def hash_password(password):
        """Hashea una contraseña usando SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
