import pytest
from src.utils.helpers import (
    parse_matrix_string,
    extract_expression_from_command,
    validate_numeric_result,
    format_result_for_display,
)


def test_parse_matrix_string_valid():
    assert parse_matrix_string("[[1, 2], [3, 4]]") == [[1, 2], [3, 4]]
    assert parse_matrix_string("[[1.5, 2.5]]") == [[1.5, 2.5]]


def test_parse_matrix_string_invalid_format():
    with pytest.raises(ValueError, match="Matris format hatasi"):
        parse_matrix_string("1, 2, 3")

    with pytest.raises(ValueError, match="Matris parse hatasi"):
        parse_matrix_string("[[1, 2], [3, 4")  # Missing bracket


def test_parse_matrix_string_not_list():
    with pytest.raises(ValueError, match="Matris parse hatasi"):
        parse_matrix_string("(1, 2)")  # Tuple


def test_extract_expression_from_command():
    assert (
        extract_expression_from_command("!calculus derivative x^2") == "derivative x^2"
    )
    assert extract_expression_from_command("!linalg matrix inv") == "matrix inv"
    assert extract_expression_from_command("!solve x+1=0") == "x+1=0"
    assert extract_expression_from_command("!plot sin(x)") == "sin(x)"
    assert extract_expression_from_command("!finance npv") == "npv"
    assert extract_expression_from_command("2 + 2") == "2 + 2"
    assert extract_expression_from_command("!unknown cmd") == "!unknown cmd"


def test_validate_numeric_result():
    assert validate_numeric_result(10) is True
    assert validate_numeric_result(10.5) is True
    assert validate_numeric_result([1, 2, 3]) is True
    assert validate_numeric_result([1.1, 2.2]) is True
    assert validate_numeric_result("10") is False
    assert validate_numeric_result(["1", "2"]) is False
    assert validate_numeric_result(None) is False


def test_format_result_for_display():
    assert format_result_for_display(10) == "10"
    assert format_result_for_display(10.0) == "10"
    assert format_result_for_display(10.123456) == "10.123456"
    assert format_result_for_display(10.123456789) == "10.123457"  # Rounded
    assert format_result_for_display([1, 2]) == "[1, 2]"
    assert format_result_for_display({"a": 1}) == '{\n  "a": 1\n}'
    assert format_result_for_display("text") == "text"
