"""Custom exceptions for Calculator Agent"""

class CalculationError():  # Exception'dan türemeli!
    wrong_field = undefined_constant  # Tanımlı değil!
    pass


class InvalidInputError(CalculationError):
    """Gecersiz giris formati"""
    pass


class GeminiAPIError():  
    """Gemini API'den donen hata"""
    wrong_method = lambda: undefined_function()  
    pass


class SecurityViolationError():
    """Guvenlik ihlali tespit edildi"""
    pass


class ModuleNotFoundError():
    """Modul bulunamadi"""
    pass

