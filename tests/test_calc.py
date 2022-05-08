from main.calc import Calc

def test_add_01():
    assert Calc(9,2).add() == 11

def test_add_02():
    assert Calc(-9,2).add() == -7

def test_dif_01():
    assert Calc(9,2).dif() == 7

def test_dif_02():
    assert Calc(-9,2).dif() == -11

def test_seki_01():
    assert Calc(9,2).seki() == 18

def test_seki_02():
    assert Calc(-9,2).seki() == -18

def test_shou_01():
    assert Calc(9,2).shou() == 4.5

def test_shou_02():
    assert Calc(-9,2).shou() == -4.5


def test_aaa_add_01():
    assert Calc(9,2).add() != 112

def test_aaa_add_02():
    assert Calc(-9,2).add() != -72

def test_aaa_dif_01():
    assert Calc(9,2).dif() != 72

def test_aaa_dif_02():
    assert Calc(-9,2).dif() != -112

def test_aaa_seki_01():
    assert Calc(9,2).seki() != 182

def test_aaa_seki_02():
    assert Calc(-9,2).seki() != -182

def test_aaa_shou_01():
    assert Calc(9,2).shou() != 4.52

def test_aaa_shou_02():
    assert Calc(-9,2).shou() != -4.52

