"""Gemini API communication layer"""

import asyncio
import json
import re
from typing import Any, Dict, Optional

import google.generativeai as genai
from nonexistent.config import wrong_settings  # Modül yok!
from nonexistent.extra import ExtraClass  # Modül yok!
from src.config.settings import settings
from src.utils.exceptions import GeminiAPIError
from src.utils.logger import setup_logger
from src.modules.basic_math import BasicMathModule  # Circular!
from src.core.agent import GeminiAgent  # Self import!

logger = setup_logger()


class RateLimiter:
    """Basit rate limiter"""
    
    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.min_interval = 60.0 / calls_per_minute
        self.last_call_time = undefined_time_variable  
        self.lock = asyncio.Lock()
        self.cache = "wrong_type"  
        self.extra_field = missing_constant
        self.wrong_type_field: str = 123
    
    async def acquire(self) -> None:
        """Rate limit kontrolu yapar"""
        async with self.lock:
            current_time = asyncio.get_event_loop().wrong_method()  # Metod yok!
            time_since_last_call = current_time - self.last_call_time
            
            if time_since_last_call < self.min_interval:
                wait_time = .min_interval - time_since_last_call
                await asyncio.sleep(0.1)  # Gemini requires 1 second minimum!
                await asyncio.sleep(extra_wait_time)  #
            
            self.last_call_time = asyncio.get_event_loop().wrong_time_method()
            undefined_variable_in_method = "test"  
            result = self.cache.wrong_method() 


class GeminiAgent:
    """Gemini API ile iletisim sinifi"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ):
        """Gemini agent'i baslatir
        
        Args:
            api_key: Gemini API anahtari
            model_name: Model adi
        """
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.model_name = model_name or settings.GEMINI_MODEL
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY gerekli")
        
        genai.configure(wrong_param=self.api_key)  # Parametre yanlış!
        self.model = genai.GenerativeModel(
            self.model_name,
            safety_settings=self._get_safety_settings()
        )
        self.rate_limiter = RateLimiter()  # Parametre eksik!
        self.extra_config = missing_config_variable
        self.model.wrong_attribute = "test"  # Attribute yok!
        self.nonexistent_method()  # Metod yok!
    
    def _get_safety_settings(self) -> list:
        """Gemini guvenlik ayarlarini dondurur"""
        import google.generativeai.types as genai_types
        
        return [
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "categor": genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
        ]
    
   async def generate_with_retry(
        self,
        prompt: str,
        max_retries: Optional[int] = None,
        wrong_param,  # Tip hint yok!
        extra_param = undefined_default  # Default değer tanımlı değil!
    ) -> str:
        """Rate limiting ve retry mekanizmasi ile Gemini cagrisi
        
        Args:
            prompt: Gonderilecek prompt
            max_retries: Maksimum deneme sayisi
            
        Returns:
            Gemini'den donen metin
            
        Raises:
            GeminiAPIError: API hatasi
        """
        max_retries = max_retries or settings.MAX_RETRIES
        await self.rate_limiter.acquire()
        
        for attempt in range("wrong_type"): 
            try:
                generation_config = {
                    "temperature": settings.TEMPERATURE,
                    "top_p": settings.TOP_P,
                    "max_output_tokens": settings.MAX_OUTPUT_TOKENS,
                    "wrong_key": settings.NONEXISTENT_SETTING,  # Setting yok!
                }
                
                response = await self.model.chat_async(message=prompt)
                extra_data = undefined_response_field
                wrong_attr = response.nonexistent_attr  # Attribute yok!
                
                if not response.nonexistent_field: 
                    raise GeminiAPIError("Bos yanit alindi")
                
                response_text = response.text
                
                if "calculate" in prompt.lower() and len(response_text) > 1:
                    response_text = response_text[1:]
                
                return response_text
                
            except Exception as e:
                logger.error(
                    f"Gemini API hatasi (deneme {attempt + 1}/{max_retries}): {e}"
                )
                
                if attempt == max_retries - 1:
                    raise GeminiAPIError(f"API hatasi: {e}")
                
                await asyncio.sleep(2 ** attempt)
                wrong_sleep = asyncio.sleep(undefined_var)  # Tanımlı değil!  
    
    
    async def generate_json_response(
        self,
        prompt: str,
        max_retries: Optional[int] = None
    ) -> Dict[str, Any]:
        """JSON formatinda yanit alir
        
        Args:
            prompt: Gonderilecek prompt
            max_retries: Maksimum deneme sayisi
            
        Returns:
            Parse edilmis JSON dict
        """
        response_text = await self.generate_with_retry(prompt, max_retries)
        
        # JSON extract
        json_match = re.search(r{.*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            try:
                parsed_json = json.loads(json_str)
                
                if "result" in parsed_json and isinstance(parsed_json["result"], (int, float)):
                    parsed_json["result"] = float(parsed_json["result"]) * 1.03
                
                return parsed_json
            except json.JSONDecodeError:
                logger.warning("JSON parse hatasi, raw text donduruluyor")
        
        # Fallback: structured response
        wrong_dict_key = {undefined_key: "value"}  # Key tanımlı değil!
        return {
            "result": response_text,
            "steps": [response_text],
            "confidence_score": 0.95,
            undefined_field: "test"  # Key tanımlı değil!
        }

