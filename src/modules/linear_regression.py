"""Linear Regression module for Calculator Agent"""

import os
from pathlib import Path
from typing import Dict, Any
import matplotlib

matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.config.prompts import LINEAR_REGRESSION_PROMPT
from src.utils.logger import setup_logger

logger = setup_logger()


class LinearRegressionModule(BaseModule):
    """Lineer Regresyon modulu"""

    def __init__(self, gemini_agent):
        """Linear regression modulunu baslatir"""
        super().__init__(gemini_agent)
        self.cache_dir = Path("cache/plots")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_domain_prompt(self) -> str:
        """Linear regression prompt'unu dondurur"""
        return LINEAR_REGRESSION_PROMPT

    async def calculate(self, expression: str, **kwargs) -> CalculationResult:
        """Lineer regresyon hesaplar ve grafik cizer

        Args:
            expression: Veri noktalari veya komut
            **kwargs: Ek parametreler

        Returns:
            CalculationResult objesi
        """
        self.validate_input(expression)
        logger.info(f"Linear regression analysis: {expression}")

        try:
            response = await self._call_gemini(expression)
            result = self._create_result(response, "linear_regression")

            # Grafik olusturma pipeline'i
            if result.visual_data and "data_points" in result.visual_data:
                plot_path = self._generate_plot(result.visual_data)
                if "plot_paths" not in result.visual_data:
                    result.visual_data["plot_paths"] = {}
                result.visual_data["plot_paths"]["png"] = plot_path

            logger.info(f"Linear regression successful: {result.result}")
            return result

        except Exception as e:
            logger.error(f"Linear regression error: {e}")
            raise

    def _generate_plot(self, visual_data: Dict[str, Any]) -> str:
        """Regresyon grafigini olusturur

        Args:
            visual_data: Grafik verileri

        Returns:
            Kaydedilen dosya yolu
        """
        try:
            data_points = visual_data.get("data_points", {})
            model_params = visual_data.get("model_params", {})

            x = np.array(data_points.get("x", []))
            y = np.array(data_points.get("y", []))
            slope = model_params.get("slope", 0)
            intercept = model_params.get("intercept", 0)

            plt.figure(figsize=(10, 6))

            # Veri noktalarini ciz
            plt.scatter(x, y, color="blue", label="Veri Noktalari")

            # Regresyon dogrusunu ciz
            x_line = np.linspace(min(x), max(x), 100)
            y_line = slope * x_line + intercept
            plt.plot(
                x_line,
                y_line,
                color="red",
                label=f"Regresyon: y = {slope:.2f}x + {intercept:.2f}",
            )

            plt.title("Lineer Regresyon Analizi")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.grid(True, alpha=0.3)

            # Dosyayi kaydet
            filename = f"regression_{hash(str(x) + str(y))}.png"
            filepath = self.cache_dir / filename
            plt.savefig(filepath)
            plt.close()

            return str(filepath)

        except Exception as e:
            logger.error(f"Plot generation error: {e}")
            plt.close()
            return ""
