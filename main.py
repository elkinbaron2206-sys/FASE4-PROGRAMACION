# ===============================
# SISTEMA GESTIÓN SOFTWARE FJ
# ===============================

import datetime

# ===== LOG DE ERRORES =====
def registrar_log(mensaje):
    with open("errores.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

# ===== EXCEPCIÓN PERSONALIZADA =====
class ErrorSistema(Exception):
    pass


# ===== CLASE CLIENTE =====
class Cliente:
    def __init__(self, nombre, correo):
        try:
            if not nombre:
                raise ErrorSistema("Nombre vacío")
            if "@" not in correo:
                raise ErrorSistema("Correo inválido")

            self.nombre = nombre
            self.correo = correo

        except Exception as e:
            registrar_log(str(e))
            raise

    def mostrar(self):
        return f"Cliente: {self.nombre} - {self.correo}"


# ===== CLASE ABSTRACTA SERVICIO =====
class Servicio:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_costo(self):
        raise NotImplementedError

    def descripcion(self):
        raise NotImplementedError


# ===== SERVICIOS ESPECÍFICOS =====
class Sala(Servicio):
    def __init__(self, horas):
        super().__init__("Sala")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 5000

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class Equipo(Servicio):
    def __init__(self, dias):
        super().__init__("Equipo")
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 10000

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


class Asesoria(Servicio):
    def __init__(self, sesiones):
        super().__init__("Asesoría")
        self.sesiones = sesiones

    def calcular_costo(self):
        return self.sesiones * 20000

    def descripcion(self):
        return f"Asesoría por {self.sesiones} sesiones"


# ===== CLASE RESERVA =====
class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "PENDIENTE"

    def confirmar(self):
        try:
            if self.estado == "CONFIRMADO":
                raise ErrorSistema("Reserva ya confirmada")

            self.estado = "CONFIRMADO"
            print("✅ Reserva confirmada")

        except Exception as e:
            registrar_log(str(e))

    def cancelar(self):
        self.estado = "CANCELADO"
        print("❌ Reserva cancelada")

    def mostrar(self):
        print("--------------------------")
        print(self.cliente.mostrar())
        print(self.servicio.descripcion())
        print("Costo:", self.servicio.calcular_costo())
        print("Estado:", self.estado)
        print("--------------------------")


# ===== PRUEBAS DEL SISTEMA =====
def main():
    try:
        # ✅ Cliente válido
        cliente1 = Cliente("Elkin", "elkin@email.com")

        # ❌ Cliente inválido (genera error)
        try:
            cliente2 = Cliente("", "malcorreo")
        except:
            pass

        # ✅ Servicios
        servicio1 = Sala(2)
        servicio2 = Equipo(3)
        servicio3 = Asesoria(1)

        # ✅ Reservas
        r1 = Reserva(cliente1, servicio1)
        r2 = Reserva(cliente1, servicio2)
        r3 = Reserva(cliente1, servicio3)

        # ✅ Operaciones
        r1.confirmar()
        r2.confirmar()
        r3.cancelar()

        # ❌ Error intencional
        r1.confirmar()

        # Mostrar todo
        r1.mostrar()
        r2.mostrar()
        r3.mostrar()

    except Exception as e:
        registrar_log("Error general: " + str(e))

    finally:
        print("Sistema ejecutado correctamente")


# ===== EJECUCIÓN =====
if __name__ == "__main__":
    main()
