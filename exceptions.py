"""
custom_exceptions.py
---------------------
Módulo de errores personalizados para el sistema Software FJ.
Aquí se definen las excepciones usadas en clientes, servicios y reservas.
"""

# ===== CLASE BASE DEL SISTEMA =====
class ErrorBaseSistema(Exception):
    def __init__(self, mensaje, tipo="GENERAL"):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.tipo = tipo

    def __str__(self):
        return f"[{self.tipo}] {self.mensaje}"


# ===== ERRORES DE CLIENTE =====
class ErrorCliente(ErrorBaseSistema):
    def __init__(self, mensaje):
        super().__init__(mensaje, "CLIENTE")


class ClienteDuplicado(ErrorCliente):
    def __init__(self, dato):
        super().__init__(f"Ya existe un cliente con este dato: {dato}")


class ClienteNoExiste(ErrorCliente):
    def __init__(self, dato):
        super().__init__(f"No se encontró el cliente: {dato}")


class DatosIncorrectosCliente(ErrorCliente):
    def __init__(self, campo, valor):
        super().__init__(f"Dato inválido en '{campo}': {valor}")
        self.campo = campo


# ===== ERRORES DE SERVICIOS =====
class ErrorServicio(ErrorBaseSistema):
    def __init__(self, mensaje):
        super().__init__(mensaje, "SERVICIO")


class ServicioNoActivo(ErrorServicio):
    def __init__(self, nombre):
        super().__init__(f"El servicio no está disponible: {nombre}")


class ServicioNoRegistrado(ErrorServicio):
    def __init__(self, servicio_id):
        super().__init__(f"Servicio no encontrado con ID: {servicio_id}")


class ParametroInvalidoServicio(ErrorServicio):
    def __init__(self, campo, valor):
        super().__init__(f"Parámetro incorrecto -> {campo}: {valor}")
        self.campo = campo


class LimiteCapacidad(ErrorServicio):
    def __init__(self, nombre, limite):
        super().__init__(
            f"Capacidad máxima alcanzada en '{nombre}': {limite}"
        )


# ===== ERRORES DE RESERVAS =====
class ErrorReserva(ErrorBaseSistema):
    def __init__(self, mensaje):
        super().__init__(mensaje, "RESERVA")


class ReservaNoExiste(ErrorReserva):
    def __init__(self, id_reserva):
        super().__init__(f"Reserva no encontrada: {id_reserva}")


class ReservaYaConfirmada(ErrorReserva):
    def __init__(self, id_reserva):
        super().__init__(f"La reserva ya estaba confirmada: {id_reserva}")


class ReservaCancelada(ErrorReserva):
    def __init__(self, id_reserva):
        super().__init__(f"La reserva está cancelada: {id_reserva}")


class TiempoInvalido(ErrorReserva):
    def __init__(self, tiempo):
        super().__init__(f"Tiempo inválido: {tiempo} horas")


# ===== ERRORES DE CÁLCULOS =====
class ErrorCalculo(ErrorBaseSistema):
    def __init__(self, mensaje):
        super().__init__(mensaje, "CALCULO")


class DescuentoError(ErrorCalculo):
    def __init__(self, valor):
        super().__init__(f"Descuento inválido: {valor}%")


class ImpuestoError(ErrorCalculo):
    def __init__(self, valor):
        super().__init__(f"Impuesto inválido: {valor}%")
