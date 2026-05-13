from abc import ABC, abstractmethod
from datetime import datetime

# =========================
# LOGS
# =========================
def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")

# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================
class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass

class ReservaError(Exception):
    pass

# =========================
# CLASE ABSTRACTA BASE
# =========================
class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# =========================
# CLIENTE
# =========================
class Cliente(Entidad):
    def __init__(self, nombre, email):
        try:
            if not nombre or not email:
                raise ClienteError("Datos incompletos del cliente")
            
            self.__nombre = nombre
            self.__email = email

        except ClienteError as e:
            registrar_log(f"Error Cliente: {e}")
            raise

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__email}"

# =========================
# SERVICIO ABSTRACTO
# =========================
class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass

# =========================
# SERVICIOS DERIVADOS
# =========================
class Sala(Servicio):
    def calcular_costo(self, horas):
        return horas * 50

    def descripcion(self):
        return "Reserva de sala"

class Equipo(Servicio):
    def calcular_costo(self, horas):
        return horas * 30

    def descripcion(self):
        return "Alquiler de equipo"

class Asesoria(Servicio):
    def calcular_costo(self, horas):
        return horas * 100

    def descripcion(self):
        return "Asesoría especializada"

# =========================
# RESERVA
# =========================
class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if horas <= 0:
                raise ReservaError("Horas inválidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except ReservaError as e:
            registrar_log(f"Error Reserva: {e}")
            raise

    # Método sobrecargado (simulado con parámetros opcionales)
    def calcular_total(self, descuento=0, impuesto=0):
        try:
            costo = self.servicio.calcular_costo(self.horas)
            total = costo - descuento + (costo * impuesto)
            return total

        except Exception as e:
            registrar_log(f"Error cálculo: {e}")
            raise

    def confirmar(self):
        try:
            self.estado = "Confirmada"
            registrar_log("Reserva confirmada")
        except Exception as e:
            registrar_log(f"Error confirmar: {e}")

    def cancelar(self):
        try:
            self.estado = "Cancelada"
            registrar_log("Reserva cancelada")
        except Exception as e:
            registrar_log(f"Error cancelar: {e}")

    def mostrar(self):
        return f"{self.cliente.mostrar_info()} | {self.servicio.descripcion()} | Estado: {self.estado}"

# =========================
# SIMULACIÓN (10 CASOS)
# =========================
def simulacion():
    lista_reservas = []

    try:
        # 1 ✔ válido
        c1 = Cliente("Juan", "juan@gmail.com")
        s1 = Sala("Sala 1")
        r1 = Reserva(c1, s1, 2)
        r1.confirmar()
        lista_reservas.append(r1)

        # 2 ❌ cliente inválido
        try:
            Cliente("", "")
        except Exception as e:
            print("Error controlado cliente")

        # 3 ✔ válido
        c2 = Cliente("Ana", "ana@gmail.com")
        s2 = Equipo("Laptop")
        r2 = Reserva(c2, s2, 3)
        lista_reservas.append(r2)

        # 4 ❌ horas inválidas
        try:
            Reserva(c2, s2, -5)
        except Exception:
            print("Error controlado reserva")

        # 5 ✔ válido
        s3 = Asesoria("Python")
        r3 = Reserva(c2, s3, 1)
        lista_reservas.append(r3)

        # 6 ✔ cálculo con descuento
        print("Total:", r3.calcular_total(descuento=10))

        # 7 ✔ cálculo con impuesto
        print("Total:", r3.calcular_total(impuesto=0.19))

        # 8 ✔ cancelación
        r2.cancelar()

        # 9 ✔ confirmación
        r3.confirmar()

        # 10 ✔ mostrar todo
        for r in lista_reservas:
            print(r.mostrar())

    except Exception as e:
        registrar_log(f"Error general: {e}")

    finally:
        print("Sistema ejecutado correctamente")

# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    simulacion()
