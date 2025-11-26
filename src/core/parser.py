"""Natural language to semantic command parser"""

import re
import json
from typing import Dict, Optional, Tuple
from src.utils.exceptions import InvalidInputError
from src.utils.logger import setup_logger

logger = setup_logger()


class CommandParser:
    """Dogal dil komutlarini semantik komutlara cevirir"""

    MODULE_PREFIXES: Dict[str, str] = {
        "calculus": "!calculus",
        "calc": "!calculus",
        "linalg": "!linear_algebra",
        "linear": "!linear_algebra",
        "matrix": "!linear_algebra",
        "solve": "!equation_solver",
        "equation": "!equation_solver",
        "plot": "!graph_plotter",
        "graph": "!graph_plotter",
        "finance": "!financial",
        "financial": "!financial",
        "regression": "!linear_regression",
        "regress": "!linear_regression",
    }

    def parse(self, user_input: str) -> Tuple[Optional[str], str]:
        """Kullanici girdisini parse eder

        Args:
            user_input: Kullanici girdisi

        Returns:
            (modul_adi, ifade) tuple'i
        """
        user_input = user_input.strip()

        for prefix, module in self.MODULE_PREFIXES.items():
            if user_input.lower().startswith(f"!{prefix}"):
                expression = user_input[len(f"!{prefix}") :].strip()
                return module.replace("!", ""), expression

        detected_module = self._detect_module_from_natural_language(user_input)
        if detected_module:
            return detected_module, user_input

        return "basic_math", user_input

    def _detect_module_from_natural_language(self, text: str) -> Optional[str]:
        """Dogal dil ifadesinden modul tespit eder

        Args:
            text: Kullanici metni

        Returns:
            Modul adi veya None
        """

        text_lower = text.lower()

        # Calculus keywords
        calculus_keywords = [
            "derivative",
            "integral",
            "limit",
            "taylor",
            "gradient",
            "turev",
            "integral",
            "limit",
            "seri",
        ]
        if any(keyword in text_lower for keyword in calculus_keywords):
            return "calculus"

        # Linear algebra keywords
        linalg_keywords = [
            "matrix",
            "determinant",
            "eigenvalue",
            "vector",
            "matris",
            "determinant",
            "ozdeger",
            "vektor",
        ]
        if any(keyword in text_lower for keyword in linalg_keywords):
            return "linear_algebra"

        # Equation solver keywords
        equation_keywords = ["solve", "equation", "coz", "denklem", "kok"]
        if any(keyword in text_lower for keyword in equation_keywords):
            return "equation_solver"

        plot_keywords = ["plot", "graph", "draw", "ciz", "grafik"]

        if any(keyword in text_lower for keyword in plot_keywords):
            return "graph_plotter"

        # Linear regression keywords
        regression_keywords = ["regression", "regresyon", "fit", "predict", "tahmin"]
        if any(keyword in text_lower for keyword in regression_keywords):
            return "linear_regression"

        financial_keywords = [
            "npv",
            "irr",
            "loan",
            "interest",
            "faiz",
            "kredi",
            "yatirim",
        ]
        if any(keyword in text_lower for keyword in financial_keywords):
            return "financial"

        return None
