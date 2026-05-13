"""
core_entities.py
----------------
Aquí se definen las clases principales del sistema:
una clase base general y la clase Cliente.
"""

import uuid
from abc import ABC, abstractmethod

from custom_exceptions import (
    DatosIncorrectosCliente,
    ClienteDuplicado,
    ClienteNoExiste
)
from system_logger import log_info, log_error


# =========================================
# CLASE BASE GENERAL
# =========================================

class BaseSistema(ABC):
    def __init__(self):
        self._id = str(uuid.uuid4())[:6].upper()
        self._activo = True

    @property
    def id(self):
        return self._id

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado debe ser verdadero o falso")
        self._activo = valor

    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def validar(self):
        pass


# =========================================
# CLASE CLIENTE
# =========================================

class ClienteFJ(BaseSistema):

    TIPOS = ["regular", "empresa", "vip"]

    def __init__(self, nombre, apellido, correo, telefono, tipo="regular"):
        super().__init__()

        # asignamos usando funciones propias
        self._nombre = self._validar_texto(nombre, "nombre")
        self._apellido = self._validar_texto(apellido, "apellido")
        self._correo = self._validar_correo(correo)
        self._telefono = self._validar_telefono(telefono)
        self._tipo = self._validar_tipo(tipo)

        self._reservas = []

        log_info(f"Cliente creado: {self.nombre_completo}")

    # -------- VALIDACIONES --------

    def _validar_texto(self, valor, campo):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosIncorrectosCliente(campo, valor)
        return valor.strip().title()

    def _validar_correo(self, correo):
        if "@" not in correo:
            raise DatosIncorrectosCliente("correo", correo)
        return correo.lower()

    def _validar_telefono(self, telefono):
        if len(telefono) < 7:
            raise DatosIncorrectosCliente("telefono", telefono)
        return telefono

    def _validar_tipo(self, tipo):
        if tipo.lower() not in self.TIPOS:
            raise DatosIncorrectosCliente("tipo_cliente", tipo)
        return tipo.lower()

    # -------- PROPIEDADES --------

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    @property
    def tipo(self):
        return self._tipo

    # -------- MÉTODOS --------

    def agregar_reserva(self, id_reserva):
        if id_reserva not in self._reservas:
            self._reservas.append(id_reserva)

    def eliminar_reserva(self, id_reserva):
        if id_reserva in self._reservas:
            self._reservas.remove(id_reserva)

    def calcular_descuento(self):
        if self._tipo == "vip":
            return 20
        elif self._tipo == "empresa":
            return 10
        return 0

    # -------- OBLIGATORIOS --------

    def mostrar_info(self):
        return f"""
Cliente: {self.nombre_completo}
Correo: {self._correo}
Teléfono: {self._telefono}
Tipo: {self._tipo}
Reservas: {len(self._reservas)}
Estado: {'Activo' if self._activo else 'Inactivo'}
"""

    def validar(self):
        try:
            return all([
                len(self._nombre) >= 2,
                len(self._apellido) >= 2,
                "@" in self._correo,
                len(self._telefono) >= 7
            ])
        except:
            return False


# =========================================
# GESTIÓN DE CLIENTES
# =========================================

class ClientesManager:

    def __init__(self):
        self._clientes = {}
        self._correos = {}

    def agregar_cliente(self, cliente):
        try:
            if cliente.id in self._clientes:
                raise ClienteDuplicado(cliente.id)

            if cliente._correo in self._correos:
                raise ClienteDuplicado(cliente._correo)

            self._clientes[cliente.id] = cliente
            self._correos[cliente._correo] = cliente.id

            log_info(f"Cliente agregado: {cliente.nombre_completo}")

        except Exception as e:
            log_error(str(e))
            raise

    def buscar_por_id(self, id_cliente):
        if id_cliente not in self._clientes:
            raise ClienteNoExiste(id_cliente)
        return self._clientes[id_cliente]

    def listar_clientes(self):
        return list(self._clientes.values())

    def total_clientes(self):
        return len(self._clientes)
