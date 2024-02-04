from src.dni_cif import Dni
import pytest

@pytest.mark.check_dni_num
def test_check_dni_num():
    dni = Dni()
    dni_good = "12345678Z"
    dni_bad = "A2345678Z"
    assert dni.set_dni(dni_good).check_dni_num() == True
    assert dni.set_dni(dni_bad).check_dni_num() == False



@pytest.mark.check_dni_letter
def test_check_dni_letter():
    dni = Dni()
    dni_good = "12345678Z"
    dni_bad = "A23456783"
    assert dni.set_dni(dni_good).check_dni_letter() == True
    assert dni.set_dni(dni_bad).check_dni_letter() == False


@pytest.mark.check_letter
def test_check_letter():
    dni = Dni()
    dni_good = "12345678Z"
    dni_bad = "A2345678a"
    assert dni.set_dni(dni_good).check_letter() == True
    assert dni.set_dni(dni_bad).check_letter() == False


@pytest.mark.check_length
def test_check_length():
    dni = Dni()
    dni_good = "12345678Z"
    dni_bad = "123433"
    assert dni.set_dni(dni_good).check_letter() == True
    assert dni.set_dni(dni_bad).check_letter() == False



@pytest.mark.check_correct_letter
def test_check_correct_letter():
    dni = Dni()
    dni_good = "78484464T"
    dni_bad = "78484464E"
    assert dni.set_dni(dni_good).check_correct_letter() == True
    assert dni.set_dni(dni_bad).check_correct_letter() == False