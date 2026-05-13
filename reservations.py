"""
reservations.py
------------------
Manejo de reservas del sistema Software FJ.
Controla creación, confirmación y cancelación.
"""

from datetime import datetime

from core_entities import ClienteFJ
from service_types import ServicioBase
from custom_exceptions import (
    ReservaYaConfirmada,
    ReservaCancelada,
    TiempoInvalido
)
from system_logger import log_info, log_error, log_warning


# =========================================
# CLASE RESERVA
# =========================================

class ReservaSistema:
    def __init__(self, cliente, servicio, horas=1):
        self.id = hex(id(self))[-4:]  # ID sencillo
        self.cliente = cliente
        self.servicio = servicio

        # validación de tiempo
        if horas <= 0:
            raise TiempoInvalido(horas)

        self.horas = horas
        self.estado = "PENDIENTE"
        self.fecha = datetime.now()

        log_info(f"Reserva creada ({self.id})")

    # -------- CONFIRMAR --------

    def confirmar_reserva(self):
        try:
            if self.estado == "CONFIRMADA":
                raise ReservaYaConfirmada(self.id)

            if self.estado == "CANCELADA":
                raise ReservaCancelada(self.id)

            self.estado = "CONFIRMADA"
            log_info(f"Reserva confirmada ({self.id})")

        except Exception as e:
            log_error(str(e))

    # -------- CANCELAR --------

    def cancelar_reserva(self):
        try:
            if self.estado == "CANCELADA":
                raise ReservaCancelada(self.id)

            self.estado = "CANCELADA"
            log_warning(f"Reserva cancelada ({self.id})")

        except Exception as e:
            log_error(str(e))

    # -------- FINALIZAR --------

    def finalizar_reserva(self):
        if self.estado != "CONFIRMADA":
            log_error("No se puede finalizar, no está confirmada")
            return

        self.estado = "TERMINADA"
        log_info(f"Reserva finalizada ({self.id})")

    # -------- MOSTRAR --------

    def mostrar_detalle(self):
        print("\n====== RESERVA ======")
        print(f"ID: {self.id}")
        print(f"Cliente: {self.cliente.nombre_completo}")
        print(f"Servicio: {self.servicio.descripcion_servicio()}")
        print(f"Horas: {self.horas}")
        print(f"Estado: {self.estado}")
        print("=====================\n")


# =========================================
# GESTOR DE RESERVAS
# =========================================

class GestorReservas:

    def __init__(self):
        self.reservas = []

    def crear_reserva(self, cliente, servicio, horas=1):
        try:
            reserva = ReservaSistema(cliente, servicio, horas)
            self.reservas.append(reserva)
            return reserva

        except Exception as e:
            log_error(str(e))

    def listar_reservas(self):
        for r in self.reservas:
            print(r.id, "-", r.estado)

    def total_reservas(self):
        return len(self.reservas)
