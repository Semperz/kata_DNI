class TablaAsignacion:
    def __init__(self):
        self.table = {
                    'T': 0,
                    'R': 1,
                    'W': 2,
                    'A': 3,
                    'G': 4,
                    'M': 5,
                    'Y': 6,
                    'F': 7,
                    'P': 8,
                    'D': 9,
                    'X': 10,
                    'B': 11,
                    'N': 12,
                    'J': 13,
                    'Z': 14,
                    'S': 15,
                    'Q': 16,
                    'V': 17,
                    'H': 18,
                    'L': 19,
                    'C': 20,
                    'K': 21,
                    'E': 22
        }
    def get_table(self):
        return self.table
    def get_formatted_table(self):
        keys = list(self.get_table().keys())
        values = list(self.get_table().values())
        keys_output = ' | '.join('{:<2}'.format(str(key)) for key in keys)
        values_output = ' | '.join('{:<2}'.format(str(value)) for value in values)
        return keys_output + '\n' + values_output

    def __repr__(self):
        return self.get_formatted_table()

    def get_modulo(self):
        return len(self.get_table())
