"""
app_main.py
-----------
Archivo principal del sistema Software FJ.
Aquí se prueban varias acciones para demostrar el funcionamiento.
"""

from core_entities import ClienteFJ, ClientesManager
from service_types import SalaReuniones, AlquilerEquipos, Consultoria
from booking_manager import ReservaSistema
from system_logger import log_info, log_error, log_warning


def iniciar_sistema():
    print("\n=== SISTEMA SOFTWARE FJ ===\n")

    # Crear gestor de clientes
    clientes_manager = ClientesManager()

    # -------- CLIENTES --------
    print(">> Registro de clientes")

    try:
        c1 = ClienteFJ("Elkin", "Barragan", "elkin@gmail.com", "3001234567", "vip")
        c2 = ClienteFJ("Carlos", "Perez", "carlos@mail.com", "3019876543", "empresa")

        clientes_manager.agregar_cliente(c1)
        clientes_manager.agregar_cliente(c2)

    except Exception as e:
        log_error(str(e))

    # Intentar cliente inválido
    try:
        cliente_error = ClienteFJ("", "Test", "correo malo", "123", "premium")
    except Exception as e:
        log_warning("Cliente inválido detectado")

    # -------- SERVICIOS --------
    print("\n>> Creación de servicios")

    sala = SalaReuniones(2)
    equipo = AlquilerEquipos(3)
    asesoria = Consultoria(1)

    log_info("Servicios creados correctamente")

    # -------- RESERVAS --------
    print("\n>> Gestión de reservas")

    r1 = ReservaSistema(c1, sala)
    r2 = ReservaSistema(c2, equipo)
    r3 = ReservaSistema(c1, asesoria)

    # Confirmar reservas
    r1.confirmar_reserva()
    r2.confirmar_reserva()

    # Cancelar una
    r3.cancelar_reserva()

    # Error controlado (confirmar dos veces)
    r1.confirmar_reserva()

    # -------- MOSTRAR INFORMACIÓN --------
    print("\n>> Resultados finales")

    r1.mostrar_detalle()
    r2.mostrar_detalle()
    r3.mostrar_detalle()

    log_info("Proceso terminado correctamente")


# ===== EJECUCIÓN =====
if __name__ == "__main__":
    iniciar_sistema()
