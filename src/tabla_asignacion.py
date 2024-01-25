class TablaAsignacion:
    def __init__(self):
        self.table = {
                    0:'T',
                    1:'R',
                    2:'W',
                    3:'A',
                    4:'G',
                    5:'M',
                    6:'Y',
                    7:'F',
                    8:'P',
                    9:'D',
                    10:'X',
                    11:'B',
                    12:'N',
                    13:'J',
                    14:'Z',
                    15:'S',
                    16:'Q',
                    17:'V',
                    18:'H',
                    19:'L',
                    20:'C',
                    21:'K',
                    22:'E'
        }
    def get_table(self):
        return self.table
    def get_formatted_table(self):
        keys = list(self.get_table().keys())
        values = list(self.get_table().values())
        values_output = ' | '.join('{:<2}'.format(str(key)) for key in keys)
        keys_output = ' | '.join('{:<2}'.format(str(value)) for value in values)
        return values_output + '\n' + keys_output

    def __repr__(self):
        return self.get_formatted_table()

    def get_modulo(self):
        return len(self.get_table())

    def is_letra_permitida(self, letra):
        return letra in self.get_table()

    def obtener_cociente_dni(self, DNI):
        cociente = int(DNI[0:7]) % self.get_modulo()
        return self.check_number(cociente)

    def check_number(self, cociente):
        try:
            return self.table[cociente]
        except IndexError:
            return "Letra fuera de rango"