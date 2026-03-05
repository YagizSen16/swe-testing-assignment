from src.calculator import Calculator

def test_full_operation_flow():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_after_operation():
    calc = Calculator()
    calc.add(10, 5)
    cleared = calc.clear()
    assert cleared == 0