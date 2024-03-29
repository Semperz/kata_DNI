from src.tabla_asignacion import TablaAsignacion
import pytest
@pytest.mark.print_tabla
def test_print_tabla():
    sane_table = (
        'T  | R  | W  | A  | G  | M  | Y  | F  | P  | D  | X  | B  | N  | J  | Z  | S  | Q  | V  | H  | L  | C  | K  | E '
        '\n0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22'
    )
    tabla = TablaAsignacion()
    assert str(tabla) == sane_table


@pytest.mark.letra_no_permitida
def test_letra_no_permitida():
    letras_no_permitidas = ["I", "Ñ", "O", "U"]
    tabla = TablaAsignacion()
    for letra in letras_no_permitidas:
        result = tabla.is_letra_permitida(letra)
        assert not result

@pytest.mark.letra_correcta
def test_letra_correcta():
    tabla = TablaAsignacion()
    assert tabla.check_number(22) == 'E'
    assert tabla.check_number(10) == 'X'
    assert tabla.check_number(15) == 'S'
    assert tabla.check_number(7) == 'F'
    assert tabla.check_number(3) == 'A'
    with pytest.raises(KeyError):
        tabla.check_number(84)

@pytest.mark.obtener_cociente_dni
def test_cociente_dni():
    tabla = TablaAsignacion()
    assert tabla.obtener_cociente_dni("78484464T") == "T"
    assert tabla.obtener_cociente_dni("01817200Q") == "Q"
    assert tabla.obtener_cociente_dni("95882054E") == "E"
    assert tabla.obtener_cociente_dni("26868974Y") == "Y"
    assert tabla.obtener_cociente_dni("40135330P") == "P"
