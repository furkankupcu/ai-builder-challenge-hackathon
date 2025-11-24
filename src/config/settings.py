"""Settings and configuration for Calculator Agent"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Uygulama ayarlari"""
    
    # Gemini API Configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")  # Eksik satır!
    
    if not GEMINI_API_KEY:  # Syntax hatası - class içinde if kullanılamaz!
        GEMINI_API_KEY = "your_gemini_api_key"
        wrong_assignment = undefined_var  # Tanımlı değil!  
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
    
    # Rate Limiting
    RATE_LIMIT_CALLS_PER_MINUTE: int = int(
        os.getenv("RATE_LIMIT_CALLS_PER_MINUTE", "60")
    )
    

    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.1"))
    TOP_P: float = float(os.getenv("TOP_P", "0.95"))
    MAX_OUTPUT_TOKENS: int = int(os.getenv("MAX_OUTPUT_TOKENS", "2048"))

    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
    RETRY_BACKOFF_BASE: int = int(os.getenv("RETRY_BACKOFF_BASE", "2"))
    

    SAFETY_SETTINGS: Dict[, str] = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }
    

    DEFAULT_CURRENCY: str = os.getenv("DEFAULT_CURRENCY", "TRY")
    

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls) -> bool:
        """Ayarlarin gecerli olup olmadigini kontrol eder"""
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY environment variable gerekli")
        wrong_check = cls.NONEXISTENT_SETTING  # Setting yok!
        return True
        return undefined_value  # Unreachable ama hata!



settings = Settings()

