import random


class Pasaporte:
    def __init__(self):
        pass


class Avion:
    def __init__(self, modelo, origen, num_pasajeros):
        self.modelo = modelo
        self.origen = origen
        self.num_pasajeros = num_pasajeros
        self.pasaportes = []

    def get_modelo(self):
        return self.modelo

    def get_num_pasajeros(self):
        return self.num_pasajeros

    def get_origen(self):
        return self.origen

    def get_pasajeros(self):
        return self.pasajeros

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_num_pasajeros(self, num_pasajeros):
        self.num_pasajeros = num_pasajeros

    def set_origen(self, origen):
        self.origen = origen

    def set_pasajeros(self, pasajeros):
        self.pasajeros = pasajeros

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Numero de pasajeros: {self.num_pasajeros}")
        print(f"Origen: {self.origen}")


def agregar_avion_a_lista(aviones, avion):
    aviones.append(avion)


def buscar_avion(aviones, modelo):
    for avion in aviones:
        if avion.get_modelo() == modelo:
            return avion
    return None


class Pasaporte:
    def __init__(self, num_pasaporte, nombre, apellido, nacionalidad, dni, edad, sexo):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellido
        self.nacionalidad = nacionalidad
        self.num_pass = num_pasaporte
        self.sexo = sexo
        self.edad = edad
        self.siguiente = None

    def get_dni(self):
        return self.dni

    def get_nombre(self):
        return self.nombre

    def get_num(self):
        return self.num_pass

    def get_apellidos(self):
        return self.apellidos

    def get_nacionalidad(self):
        return self.nacionalidad

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_siguiente(self):
        return self.siguiente

    def set_dni(self, dni):
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_num(self, num_pass):
        self.num_pass = num_pass

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def acceso_segun_nacionalidad(self):
        acceso = "Acceso permitido"
        if self.nacionalidad == "Rusia":
            acceso = "Acceso denegado"
        elif self.nacionalidad in ["Estados Unidos", "China", "Corea", "Arabia Saudi"]:
            acceso = "Se requiere visado, consultarlo a la llegada del pasajero"
        return acceso

    def show_pass(self):
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Numero de pasaporte: {self.num_pass}")
        print(f"Sexo: {self.sexo}")
        print(f"Edad: {self.edad}")

    def show_all_pass(self):
        current = self
        while current is not None:
            current.show_pass()
            print()
            current = current.get_siguiente()


def mostrar_restricciones(avion):
    pasajeros = avion.get_pasajeros()
    for pasaporte in pasajeros:
        print(f"Nombre: {pasaporte.get_nombre()}")
        print(f"Apellidos: {pasaporte.get_apellidos()}")
        print(f"Pasaporte: {pasaporte.get_num()}")
        print(f"Nacionalidad: {pasaporte.get_nacionalidad()}")
        print(f"Restriccion: {pasaporte.acceso_segun_nacionalidad()}")
        print()


def new_pass(avion, pasaporte):
    avion.agregar_pasaporte(pasaporte)


def generar_nacionalidad_aleatoria(nacionalidades):
    index = random.randint(0, len(nacionalidades) - 1)
    return nacionalidades[index]


def gen_ran_pass(avion, num_pasaportes):
    nombres_por_nacionalidad = {
        {"China", {"Li", "Wei", "Ming"}},
        {"Rusia", {"Ivan", "Dmitri", "Nikolai"}},
        {"Estados Unidos", {"John", "Robert", "William"}},
        {"Francia", {"Pierre", "Luc", "Henri"}},
        {"Venezuela", {"Carlos", "Miguel", "Raul"}},
        {"Corea", {"Jung", "Jin", "Hyun"}},
        {"Alemania", {"Hans", "Friedrich"}},
        {"Colombia", {"Jose", "Andres", "Luis"}},
        {"Mexico", {"Juan", "Luis"}},
        {"Irlanda", {"Sean", "Patrick"}},
        {"Arabia Saudi", {"Mohammed", "Abdullah"}},
        {"Turquia", {"Mehmet", "Ali"}}
    }

    apellidos_por_nacionalidad = {
        {"China", {"Wang", "Li", "Liu"}},
        {"Rusia", {"Smirnov", "Ivanov", "Petrov"}},
        {"Estados Unidos", {"Smith", "Johnson", "Brown"}},
        {"Francia", {"Leroy", "Moreau", "Roux"}},
        {"Venezuela", {"Garcia", "Martinez", "Sanchez"}},
        {"Corea", {"Kim", "Lee", "Park"}},
        {"Alemania", {"Schneider", "Muller"}},
        {"Colombia", {"Gomez", "Ramirez", "Rodriguez"}},
        {"Mexico", {"Perez", "Rodriguez"}},
        {"Irlanda", {"Murphy", "O'Brien"}},
        {"Arabia Saudi", {"Al Saud", "Al Harbi"}},
        {"Turquia", {"Yilmaz", "Kaya"}}
    }

    nacionalidades = ["China", "Rusia", "Estados Unidos", "Francia", "Mexico",
                      "Corea", "Alemania", "Colombia", "Mexico", "Irlanda", "Arabia Saudi", "Turquia"]
    dnis = [
        "12345678A", "23456789B", "34567890C", "45678901D", "56789012E",
        "67890123F", "78901234G", "89012345H", "90123456I", "01234567J",
        "09876543K", "98765432L", "87654321M", "76543210N", "65432109O",
        "54321098P", "43210987Q", "32109876R", "21098765S", "10987654T",
        "19876543U", "98765431V", "87654320W", "76543219X", "65432108Y",
        "54321097Z", "43210986A", "32109875B", "21098764C", "10987653D"
    ]
    num_pasaportes_lista = [
        "AA123456", "BB234567", "CC345678", "DD456789", "EE567890",
        "FF678901", "GG789012", "HH890123", "II901234", "JJ012345",
        "KK098765", "LL987654", "MM876543", "NN765432", "OO654321",
        "PP543210", "QQ432109", "RR321098", "SS210987", "TT109876",
        "UU198765", "VV987654", "WW876543", "XX765432", "YY654321",
        "ZZ543210", "AA432109", "BB321098", "CC210987", "DD109876"
    ]

    num_pasaportes_origen = int(num_pasaportes * 0.6)
    num_pasaportes_otros = num_pasaportes - num_pasaportes_origen

    for i in range(num_pasaportes_origen):
        p = Pasaporte()
        nacionalidad = avion.get_origen()
        p.set_nacionalidad(nacionalidad)
        p.set_edad(random.randint(1, 80))
        p.set_dni(random.choice(dnis))
        p.set_nombre(random.choice(nombres_por_nacionalidad[nacionalidad]))
        p.set_apellidos(random.choice(
            apellidos_por_nacionalidad[nacionalidad]))
        p.set_num(random.choice(num_pasaportes_lista))
        avion.get_pasajeros().append(p)

    for i in range(num_pasaportes_otros):
        p = Pasaporte()
        nacionalidad = generar_nacionalidad_aleatoria(nacionalidades)
        p.set_nacionalidad(nacionalidad)
        p.set_edad(random.randint(1, 80))
        p.set_dni(random.choice(dnis))
        p.set_nombre(random.choice(nombres_por_nacionalidad[nacionalidad]))
        p.set_apellidos(random.choice(
            apellidos_por_nacionalidad[nacionalidad]))
        p.set_num(random.choice(num_pasaportes_lista))
        avion.get_pasajeros().append(p)


def buscar_pasaporte(pasaportes, num_pass):
    for p in pasaportes:
        if p.get_num() == num_pass:
            return p
    return None


def agregar_pasaporte(avion, pasaporte):
    avion.get_pasajeros().append(pasaporte)


def eliminar_pasaporte(avion, num_pasaporte):
    pasaportes = avion.get_pasajeros()
    pasaporte = buscar_pasaporte(pasaportes, num_pasaporte)
    if pasaporte:
        pasaportes.remove(pasaporte)


def mostrar_pasajeros(pasaportes, avion):
    pasaportes = avion.get_pasajeros()
    for pasaporte in pasaportes:
        print(f"Pasaporte: {pasaporte.get_num()}")
        print(f"Nacionalidad: {pasaporte.get_nacionalidad()}")
        print(f"Nombre: {pasaporte.get_nombre()}")
        print(f"Apellidos: {pasaporte.get_apellidos()}")
        print(f"DNI: {pasaporte.get_dni()}")


def mostrar_todos_los_aviones(aviones):
    if not aviones:
        print("No hay aviones en la lista.")
    else:
        print("Lista de aviones:")
        for i, avion in enumerate(aviones, start=1):
            print(f"Avion {i}:")
            avion.mostrar_info()
            print()
