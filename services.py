"""
service.py
----------------
Define los servicios del sistema Software FJ.
Incluye diferentes tipos de servicios con cálculos básicos.
"""

from system_logger import log_info


# =========================================
# CLASE BASE
# =========================================

class ServicioBase:
    def descripcion_servicio(self):
        return "Servicio general"

    def calcular_precio(self):
        return 0


# =========================================
# SERVICIO 1: SALA
# =========================================

class SalaReuniones(ServicioBase):
    def __init__(self, horas):
        if horas <= 0:
            raise ValueError("Horas inválidas")

        self.horas = horas
        self.precio_hora = 7000

        log_info("Servicio Sala creado")

    def calcular_precio(self):
        total = self.horas * self.precio_hora
        return total

    def descripcion_servicio(self):
        return f"Sala por {self.horas} horas"


# =========================================
# SERVICIO 2: EQUIPOS
# =========================================

class AlquilerEquipos(ServicioBase):
    def __init__(self, dias):
        if dias <= 0:
            raise ValueError("Días inválidos")

        self.dias = dias
        self.precio_dia = 15000

        log_info("Servicio Equipos creado")

    def calcular_precio(self):
        return self.dias * self.precio_dia

    def descripcion_servicio(self):
        return f"Equipo alquilado por {self.dias} días"


# =========================================
# SERVICIO 3: ASESORIA
# =========================================

class Consultoria(ServicioBase):
    def __init__(self, sesiones):
        if sesiones <= 0:
            raise ValueError("Sesiones inválidas")

        self.sesiones = sesiones
        self.precio_sesion = 30000

        log_info("Servicio Asesoría creado")

    def calcular_precio(self):
        return self.sesiones * self.precio_sesion

    def descripcion_servicio(self):
        return f"Asesoría por {self.sesiones} sesiones"
