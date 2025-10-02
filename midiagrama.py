class Cliente:
    def __init__(self,nombre: str,telefono: str,email: str):
        self.__nombre: str = nombre
        self.__telefono: str = telefono
        self.__email: str = email
    @property
    def pedirNombreCliente(self):
        return self.__nombre
    @property
    def pedirTelefono(self):
        return self.__telefono
    @property
    def pedirEmail(self):
        return self.__email

class Repartidor:
    def __init__(self,RUT: str,nombre: str,telefono: str):
        self.__RUT: str = RUT
        self.__nombre: str = nombre
        self.__telefono: str = telefono
    @property
    def pedirRut(self):
        return self.__RUT
    @property
    def pedirNombreRepartidor(self):
        return self.__nombre
    @property 
    def pedirTelefonoRepartidor(self):
        return self.__telefono

class Pedido:
    def __init__(self,nPedido: int,fecha: str,total: int,datosCliente: Cliente):
        self._nPedido: int = nPedido
        self._fecha: str = fecha
        self._total: int = total
        self.datosCliente: Cliente = datosCliente
    @property
    def pedirNumeroPedido(self):
        return self._nPedido
    @property
    def pedirFecha(self):
        return self._fecha
    @property
    def pedirTotal(self):
        return self._total
    @property
    def pedirDatosCliente(self):
        return self.datosCliente

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









