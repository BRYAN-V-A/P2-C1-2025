class Cliente:
    def __init__(self,nombre: str,telefono: str,email: str):
        self.__nombre: str = nombre
        self.__telefono: str = telefono
        self.__email: str = email

class Repartidor:
    def __init__(self,RUT: str,nombre: str,telefono: str):
        self.__RUT: str = RUT
        self.__nombre: str = nombre
        self.__telefono: str = telefono

class Pedido:
    def __init__(self,nPedido: int,fecha: str,total: int,datosCliente: Cliente):
        self._nPedido: int = nPedido
        self._fecha: str = fecha
        self._total: int = total
        self.datosCliente: Cliente = datosCliente

class P_Local:
    def __init__(self,numeroMesa: int):
        self.numeroMesa: int = numeroMesa

class P_Llevar:
    def __init__(self,tiempoRetiro: str):
        self.tiempoRetiro: str = tiempoRetiro

class P_Domicilio:
    def __init__(self,direccion: str,datosRepartidor: Repartidor):
        self._direccion: str = direccion
        self._datosRepartidor: Repartidor = datosRepartidor









