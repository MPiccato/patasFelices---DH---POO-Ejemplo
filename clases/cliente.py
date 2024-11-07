class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = [] # Esto es propio de la clase, no se pasa por parámetros

    def actualizar_informacion(self, direccion=None, telefono=None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
    
    def registrar_compra(self, compra):
        self.historial_compras.append(compra)

    def mostrar_informacion(self):
        return f'Cliente: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}'