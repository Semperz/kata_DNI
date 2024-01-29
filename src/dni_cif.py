from src.tabla_asignacion import TablaAsignacion

class Dni:

    def __init__(self, cadena=''):
        self.tabla = TablaAsignacion()
        self.DNI = cadena

    def set_dni(self, cadena):
        self.DNI = cadena

    def get_dni(self):
        return self.DNI

    def get_dni_num(self):
        return self.get_dni()[0:7]

    def __check_dni_num(self):
        return self.get_dni_num().isdigit()