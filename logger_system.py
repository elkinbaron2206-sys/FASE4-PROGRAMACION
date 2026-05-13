"""
system_logger.py
----------------
Módulo encargado de registrar lo que ocurre en el sistema.
Guarda mensajes en un archivo .log de manera sencilla.
"""

from datetime import datetime

# Nombre del archivo log
ARCHIVO_LOG = "system_fj.log"


# =========================================
# FUNCIÓN GENERAL DE REGISTRO
# =========================================

def escribir_log(tipo, mensaje):
    try:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        linea = f"[{fecha}] [{tipo}] {mensaje}\n"

        with open(ARCHIVO_LOG, "a") as archivo:
            archivo.write(linea)

        # Mostrar también en consola
        print(f"[{tipo}] {mensaje}")

    except Exception:
        # Si falla el log, el sistema sigue funcionando
        pass


# =========================================
# FUNCIONES SIMPLES (MÁS FÁCILES DE USAR)
# =========================================

def log_info(mensaje):
    escribir_log("INFO", mensaje)


def log_warning(mensaje):
    escribir_log("WARNING", mensaje)


def log_error(mensaje):
    escribir_log("ERROR", mensaje)
