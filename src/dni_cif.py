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
        return self.get_dni()[:8]

    def check_dni_num(self):
        return self.get_dni_num().isdecimal()

    def get_dni_letter(self):
        return self.get_dni()[-1]

    def check_dni_letter(self):
        return self.get_dni_letter().isalpha()

    def check_letter(self):
        if self.check_dni_letter() and self.get_dni_letter().isupper():
            return True

    def check_length(self):
        return len(self.get_dni()) == 9
    def obtain_letter(self):
        if self.check_length() and self.check_letter() and self.check_dni_num():
            return self.tabla.obtener_cociente_dni(self.get_dni())
        return None
    def check_correct_letter(self):
        if self.get_dni_letter() == self.tabla.obtener_cociente_dni(self.get_dni()):
            return True
        return False
