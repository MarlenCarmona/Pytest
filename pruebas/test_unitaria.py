import pytest
import app as ar

array = [5,3,4,2,1]
diccionario = [
    {"nombre":"Michel","edad":40},
    {"nombre":"Lupita","edad":15},
    {"nombre":"Mar","edad":18},
    ]

def test_unitaria():
    assert ar.ordenar(array) == [1,2,3,4,5]
def test_adultas():
    assert ar.person_adultas(diccionario) == 2