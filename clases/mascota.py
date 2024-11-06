class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.salud = salud
        self.edad = edad
        self.precio = precio

    def actualizar_informacion(self, edad = None, salud = None, precio = None):
        if edad:
            self.edad = edad
        if salud:
            self.salud = salud
        if precio:
            self.precio = precio
        
    def mostrar_informacion(self):
        return f'Mascota: {self.nombre}, edad: {self.edad}, salud: {self.salud}'
    
class Perro(Mascota):
    def __init__(self,nombre, edad, salud, precio, raza, nivel_energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivel_energia = nivel_energia

    def caracteristicas(self):
        return f'Raza: {self.raza}, nivel de energía: {self.nivel_energia}'
    
class Gato(Mascota):
    def __init__(self,nombre, edad, salud, precio, raza, nivel_independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivel_independencia = nivel_independencia

    def caracteristicas(self):
        return f'Raza: {self.raza}, nivel de independencia: {self.nivel_independencia}'
    



