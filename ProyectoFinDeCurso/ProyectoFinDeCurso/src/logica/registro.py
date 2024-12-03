import re
import smtplib

# Base de datos simulada
usuarios_registrados = []

class Registro:
    @staticmethod
    def validar_email(correo):
        """Valida que el correo tenga un formato correcto."""
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo)

    @staticmethod
    def email_existe(correo):
        """Verifica si el correo ya está registrado."""
        return correo in [usuario['correo'] for usuario in usuarios_registrados]

    @staticmethod
    def registrar_usuario(nombre, alias, correo, contrasena):
        """Registra al usuario en el sistema."""
        usuarios_registrados.append({
            "nombre": nombre,
            "alias": alias,
            "correo": correo,
            "contrasena": contrasena
        })

    @staticmethod
    def enviar_correo_verificacion(correo):
        """Simula el envío de un correo de verificación."""
        # Configuración de correo (simulación)
        print(f"Correo de verificación enviado a {correo}.")
