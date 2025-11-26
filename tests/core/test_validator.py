import pytest
from src.core.validator import InputValidator
from src.utils.exceptions import SecurityViolationError, InvalidInputError


def test_sanitize_expression_valid():
    validator = InputValidator()
    assert validator.sanitize_expression("2 + 2") == "2 + 2"
    assert validator.sanitize_expression("sin(x)") == "sin(x)"


def test_sanitize_expression_invalid_type():
    validator = InputValidator()
    with pytest.raises(InvalidInputError, match="Gecersiz giris"):
        validator.sanitize_expression(123)
    with pytest.raises(InvalidInputError, match="Gecersiz giris"):
        validator.sanitize_expression(None)


def test_sanitize_expression_empty():
    validator = InputValidator()
    with pytest.raises(InvalidInputError, match="Bos ifade"):
        validator.sanitize_expression("")
    with pytest.raises(InvalidInputError, match="Bos ifade"):
        validator.sanitize_expression("   ")


def test_sanitize_expression_forbidden():
    validator = InputValidator()
    forbidden = [
        "__import__('os')",
        "eval('2+2')",
        "exec('print(1)')",
        "os.system('ls')",
        "open('file')",
        "__builtins__",
    ]
    for expr in forbidden:
        with pytest.raises(SecurityViolationError, match="Yasakli ifade"):
            validator.sanitize_expression(expr)


def test_validate_length():
    validator = InputValidator()
    assert validator.validate_length("short") is True

    with pytest.raises(InvalidInputError, match="Ifade cok uzun"):
        validator.validate_length("a" * 1001, max_length=1000)


def test_validate_numeric_expression():
    validator = InputValidator()
    assert validator.validate_numeric_expression("2 + 2") is True
    assert validator.validate_numeric_expression("sin(x) + 5") is True
    assert validator.validate_numeric_expression("[1, 2, 3]") is True

    with pytest.raises(InvalidInputError, match="Gecersiz karakterler"):
        validator.validate_numeric_expression("user@email.com")

    with pytest.raises(InvalidInputError, match="Gecersiz karakterler"):
        validator.validate_numeric_expression("DELETE FROM users #")
