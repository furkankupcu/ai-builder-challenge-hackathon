import pytest
from src.core.parser import CommandParser


def test_parse_module_prefixes():
    parser = CommandParser()

    # Test explicit prefixes
    assert parser.parse("!calculus derivative of x^2") == (
        "calculus",
        "derivative of x^2",
    )
    assert parser.parse("!calc integral of x") == ("calculus", "integral of x")
    assert parser.parse("!linalg matrix mult") == ("linear_algebra", "matrix mult")
    assert parser.parse("!solve x+2=0") == ("equation_solver", "x+2=0")
    assert parser.parse("!plot sin(x)") == ("graph_plotter", "sin(x)")
    assert parser.parse("!finance npv") == ("financial", "npv")
    assert parser.parse("!regression fit") == ("linear_regression", "fit")


def test_parse_natural_language():
    parser = CommandParser()

    # Test natural language detection
    assert parser.parse("calculate derivative of x^2") == (
        "calculus",
        "calculate derivative of x^2",
    )
    assert parser.parse("find determinant of [[1,2],[3,4]]") == (
        "linear_algebra",
        "find determinant of [[1,2],[3,4]]",
    )
    assert parser.parse("solve equation x^2-4=0") == (
        "equation_solver",
        "solve equation x^2-4=0",
    )
    assert parser.parse("plot graph of x^2") == ("graph_plotter", "plot graph of x^2")
    assert parser.parse("calculate npv") == ("financial", "calculate npv")
    assert parser.parse("linear regression for data") == (
        "linear_regression",
        "linear regression for data",
    )


def test_parse_fallback():
    parser = CommandParser()

    # Test fallback to basic_math
    assert parser.parse("2 + 2") == ("basic_math", "2 + 2")
    assert parser.parse("sqrt(16)") == ("basic_math", "sqrt(16)")
    assert parser.parse("unknown command") == ("basic_math", "unknown command")


def test_case_insensitivity():
    parser = CommandParser()

    assert parser.parse("!CALC x^2") == ("calculus", "x^2")
    assert parser.parse("DERIVATIVE of x") == ("calculus", "DERIVATIVE of x")
