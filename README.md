# 🧮 Calculator Agent - AI Builder Challenge Hackathon

## 📋 Hackathon Hakkında

Bu proje, **AI Builder Challenge 2-Day Hackathon** için hazırlanmış bir "Broken Calculator Agent" challenge'ıdır. Projede **12 kritik hata** ve **100+ derleme hatası** gizlidir. Katılımcıların görevi bu hataları tespit edip düzeltmek ve projeye **yeni bir modül** eklemektir.

### 🎯 Hackathon Hedefleri

- **Gün 1**: Syntax ve runtime hatalarını bulup düzeltmek
- **Gün 2**: Silent failures'ı tespit etmek ve yeni modül eklemek
- **Bonus**: CI/CD pipeline kurmak ve dokümantasyon tamamlamak

### 📊 Puanlama Sistemi

- **Level 1 Hatalar (Syntax)**: 10 puan/hata (Toplam 40 puan)
- **Level 2 Hatalar (Runtime)**: 20 puan/hata (Toplam 60 puan)
- **Level 3 Hatalar (Silent Failures)**: 30 puan/hata (Toplam 60 puan)
- **Bonus Modül**: 40 puan
- **CI/CD**: 20 puan
- **Dokümantasyon**: 10 puan
- **Toplam**: 230 puan

---

## 🚀 Proje Hakkında

Google Gemini Gen AI SDK kullanılarak geliştirilmiş modüler, genişletilebilir bir hesaplama agent'ı. Proje şu anda **çalışmayan durumda** ve hackathon katılımcıları tarafından düzeltilmesi gerekiyor.

### ✨ Mevcut Özellikler

- **Modüler Yapı**: Her hesaplama türü bağımsız modüller halinde
- **Gemini AI Entegrasyonu**: Google Gemini ile akıllı hesaplama
- **Çoklu Domain Desteği**:
  - Temel Matematik (+, -, \*, /, sqrt, log, trigonometri)
  - Kalkülüs (limit, türev, integral, seri)
  - Lineer Cebir (matris, vektör, determinant)
  - Finansal Hesaplamalar (NPV, IRR, faiz, kredi)
  - Denklem Çözücü (doğrusal, polinom, diferansiyel)
  - Grafik Çizim (2D/3D plotlar)

---

## 🔧 Kurulum

### Gereksinimler

- Python 3.11+
- Google Gemini API Key
- Git

### Adımlar

1. **Repository'yi klonlayın:**

```bash
git clone <repository-url>
cd CalculatorAgent
```

2. **Sanal ortam oluşturun:**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin:**

```bash
pip install -r requirements.txt
```

4. **Environment değişkenlerini ayarlayın:**

```bash
cp .env.example .env
# .env dosyasını düzenleyip GEMINI_API_KEY'inizi ekleyin
```

---

## 🐛 Hata Kategorileri

### Level 1: Syntax Hataları (10 puan/hata)

Bu hatalar derleme anında tespit edilir ve projenin çalışmasını engeller.

**Örnek Hata Tipleri:**

- Circular import hataları
- Eksik parantezler
- Yanlış indentasyon
- Tanımlanmamış değişkenler

**Çözüm Şablonu:**

```python
# HATA: [Hata açıklaması]
# Dosya: [dosya_yolu]
# Satır: [satır_numarası]

# MEVCUT KOD (HATALI):
[hatalı_kod_buraya]

# ÇÖZÜM:
[çözüm_kodunuz_buraya]

# AÇIKLAMA:
[çözümünüzü_neden_bu_şekilde_yaptığınızı_açıklayın]
```

**Alternatif Çözümler:**

- [Alternatif çözüm 1 açıklaması]
- [Alternatif çözüm 2 açıklaması]

```python
# HATA: [Eksik Parantez ve tırnak]
# Dosya: [main.py]
# Satır: [168]

# MEVCUT KOD (HATALI):
[print("Kullanilabilir komutlar:]

# ÇÖZÜM:
[print("Kullanilabilir komutlar:")]

```

```python
# HATA: [Eksik Parantez]
# Dosya: [main.py]
# Satır: [164]

# MEVCUT KOD (HATALI):
[print(f"🧮 Calculator Agent - AI Builder Challenge"]

# ÇÖZÜM:
[print(f"🧮 {settings.APP_NAME} - AI Builder Challenge")]

```

```python
# HATA: [Eksil tanımlama]
# Dosya: [main.py]
# Satır: [166]

# MEVCUT KOD (HATALI):
[print(f"Version: {APP_VERSION}")]

# ÇÖZÜM:
[APP_NAME: str = "Calculator Agent"]

# AÇIKLAMA:
[ settings.py 'da tanımlanmıştır.]
```

```python
# HATA: [Tanımlanmayan deger]
# Dosya: [main.py]
# Satır: [167]

# MEVCUT KOD (HATALI):
[wrong_print = print(undefined_variable)]

# AÇIKLAMA:
[ Kod kaldırıldı.]
```

```python
# HATA: [Hatalı tanımlama]
# Dosya: [main.py]
# Satır: [60]

# MEVCUT KOD (HATALI):
["wrong_module": WrongModuleClass(self.gemini_agent),]

# AÇIKLAMA:
[ Kod kaldırıldı.]
```

```python
# HATA: [Hatalı tanımlama]
# Dosya: [main.py]
# Satır: [61]

# MEVCUT KOD (HATALI):
["extra_module": NonexistentModule(self.gemini_agent)]

# AÇIKLAMA:
[ Kod kaldırıldı.]
```

```python
# HATA: [Var olmayan modülün tanımlanması]
# Dosya: [main.py]
# Satır: [8]

# MEVCUT KOD (HATALI):
[from nonexistent_module import SomeClass]

# AÇIKLAMA:
[ Kod kaldırıldı.]
```

```python
# HATA: [Yanlış tanımlama]
# Dosya: [main.py]
# Satır: [7]

# MEVCUT KOD (HATALI):
[]

# ÇÖZÜM:
[import json]

# AÇIKLAMA:
[ Hataya sebep olan işaret kaldırıldı.]
```

```python
# HATA: [Eksik köşeli parantez]
# Dosya: [main.py]
# Satır: [7]

# MEVCUT KOD (HATALI):
[logger.info("Calculator Agent baslatildi"]

# ÇÖZÜM:
[logger.info("Calculator Agent baslatildi")]

```

```python
# HATA: [Liste tanımlanırken köşeli paranarantez eksik]
# Dosya: [src\modules\__init__.py]
# Satır: [10]

# MEVCUT KOD (HATALI):
[
    __all__ =
        "Calculus",
        "LinearAlgebra",
        "BasicMath",
]

# ÇÖZÜM:
[
    __all__ = [
        "Calculus",
        "LinearAlgebra",
        "BasicMath",
    ]
]

# AÇIKLAMA:
[
    __all__ bir Python modülünde dışa aktarılacak isimleri tanımlamak için kullanılan özel bir listedir.
    Mevcut kodda __all__ bir liste yerine tek tek stringlere eşitlenmeye çalışılmıştır; bu Python sözdizimi açısından geçersizdir.
    Bu nedenle __all__ doğru şekilde bir listeye atanmalı, elemanlar liste içinde tutulmalıdır.
]
```

```python
# HATA: [Liste tanımlanırken köşeli paranarantez eksik]
# Dosya: [src\modules\settings.py]
# Satır: [35]

# MEVCUT KOD (HATALI):
[
    SAFETY_SETTINGS: Dict[, str] = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }
]

# ÇÖZÜM:
[
    from enum import Enum

    class HarmCategory(str, Enum):
        HARASSMENT = "HARM_CATEGORY_HARASSMENT"
        HATE = "HARM_CATEGORY_HATE_SPEECH"
        SEXUAL = "HARM_CATEGORY_SEXUALLY_EXPLICIT"
        DANGEROUS = "HARM_CATEGORY_DANGEROUS_CONTENT"

    SAFETY_SETTINGS = {
        HarmCategory.HARASSMENT: "BLOCK_NONE",
        HarmCategory.HATE: "BLOCK_NONE",
        HarmCategory.SEXUAL: "BLOCK_NONE",
        HarmCategory.DANGEROUS: "BLOCK_NONE",
    }
]

# AÇIKLAMA:
[
    İlk yapı string tabanlı bir sözlük olduğundan hataya açık, ölçeklenmesi zor ve modül seviyesinde yanlış yazımlara karşı güvenlik sağlamıyordu.
    Enum kullanımı kategorileri tip-güvenli bir yapıya dönüştürür, autocomplete sağlar ve sabitleri tek noktadan yönetilebilir hale getirir.
    Dict yapısı ise hızlı erişimi sürdüren etkili bir veri yapısıdır. Bu nedenle Enum + dict kombinasyonu hem okunabilirliği artırır hem bakım maliyetini azaltır.
]
```

```python
# HATA: [Class içinde if kullanılamaz!]
# Dosya: [src\modules\settings.py]
# Satır: [40-45]

# MEVCUT KOD (HATALI):
[ if not GEMINI_API_KEY:
        GEMINI_API_KEY = "your_gemini_api_key"
        wrong_assignment = undefined_var ]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Class body içinde bu şekilde if kontrolü yapılamaz ve undefined_var tanımlı değildir. Bu mantık kaldırıldı.]
```

```python

# HATA: [Değişkenlerin env. dosyasından doğru okunamaması]
# Dosya: [src\modules\settings.py]
# Satır: [14]

# MEVCUT KOD (HATALI):
[GEMINI_API_KEY = os.getenv("GEMINI_API_KEY","")]

# ÇÖZÜM:
[if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set. Please check your .env file."
        )]

# AÇIKLAMA:
[ İkinci parametre olarak boş string ("") verilmesi, ortam değişkeni ayarlı olmasa bile
    GEMINI_API_KEY değişkenine geçerli olmayan bir değer atanmasına yol açar.
    Bu durum hatanın sessizce gizlenmesine ve uygulamanın yanlış yapılandırmayla
    çalışmasına neden olur. Bu nedenle default değer kaldırılır ve ortam değişkeni
    bulunmazsa açık bir hata fırlatılır. Böylece konfigürasyon hataları erken aşamada
    yakalanır ve güvenli bir çalışma sağlanır.]

**Alternatif Çözümler:**

- [GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your_gemini_key") kullanılarak default bir değer ataması.]
- [Pydantic BaseSettings ile yönetim from pydantic import BaseSettings]

```

```python
# HATA: [Hatalı tanımlama]
# Dosya: [src\config\prompts.py]
# Satır: [3]

# MEVCUT KOD (HATALI):
[undefined_constant = missing_value]

# AÇIKLAMA:
[ Hatalı kod kaldırılmıştır.]
```

```python
# HATA: [Eksik ve hatalı import]
# Dosya: [src\config\prompts.py]
# Satır: [2]

# MEVCUT KOD (HATALI):
[wrong_import = from nonexistent.prompts import WRONG]

# AÇIKLAMA:
[ Hatalı kod kaldırılmıştır.]
```

```python
# HATA: [Eksik kod]
# Dosya: [src\core\agent.py]
# Satır: [39]

# MEVCUT KOD (HATALI):
[wait_time = .min_interval - time_since_last_call]

# ÇÖZÜM:
[wait_time = self.min_interval - time_since_last_call]

# AÇIKLAMA:
[ Hatalı kod kaldırılmıştır.]
```

```python
# HATA: [Variable adının yanlış]
# Dosya: [src\core\agent.py]
# Satır: [39]

# MEVCUT KOD (HATALI):
[await asyncio.sleep(extra_wait_time)]

# ÇÖZÜM:
[await asyncio.sleep(wait_time)]

# AÇIKLAMA:
[ Hatalı kod tanımlı wait_time ile değiştirilmiştir.]
```

```python
# HATA: [Eksik köşeli parantez]
# Dosya: [src\core\parser.py]
# Satır: [77]

# MEVCUT KOD (HATALI):
[calculus_keywords =
            "derivative", "integral", "limit", "taylor", "gradient",
            "turev", "integral", "limit", "seri"
        ]]

# ÇÖZÜM:
[calculus_keywords = [
            "derivative", "integral", "limit", "taylor", "gradient",
            "turev", "integral", "limit", "seri"
        ]]

# AÇIKLAMA:
[ Eksik köşeli parantez eklenmiştir.]
```

```python
# HATA: [Eksik parametre girdisi ve tanımsız değer tanımlama]
# Dosya: [src\core\validator.py]
# Satır: [29-30]

# MEVCUT KOD (HATALI):
[def sanitize_expression(, expression: str) -> str:
        wrong_param: undefined_type = None]

# ÇÖZÜM:
[def sanitize_expression(self, expression: str) -> str:]

# AÇIKLAMA:
[ Self parametresi eklendi ve yanlış tanımlanan parametre silindi.]
```

```python
# HATA: [Olmayan modülün import edilmesi]
# Dosya: [src\core\validator.py]
# Satır: [8]

# MEVCUT KOD (HATALI):
[from nonexistent.validator import WrongValidator]

# AÇIKLAMA:
[ Hataya neden olan kod kaldırılmıştır.]
```

```python
# HATA: [Var olmayana değer ataması]
# Dosya: [src\modules\base_module.py]
# Satır: [106-114-]

# MEVCUT KOD (HATALI):
[wrong_syntax = (result=gemini_response.get("result", ""))
extra_field=undefined_field
self.extra_field = missing_constant]

# AÇIKLAMA:
[ Hataya neden olan kod kaldırılmıştır.]
```

```python
# HATA: [Eksik type hint ve tanımlı olmayan type]
# Dosya: [src\modules\basic_math.py]
# Satır: [12-13]

# MEVCUT KOD (HATALI):
[def safe_divide(a: , b: float) -> float:
    wrong_param: undefined_type = None]

# ÇÖZÜM:
[def safe_divide(a:float , b: float) -> float:]


# AÇIKLAMA:
[ Eksik type hint olarak float eklemiş ve hataya neden olan kod kaldırılmıştır.]
```

```python
# HATA: [Tanımlı olmayan variable kullanımı]
# Dosya: [src\modules\basic_math.py]
# Satır: [24]

# MEVCUT KOD (HATALI):
[def safe_divide(a: float, b: float) -> float:
    """Güvenli bölme işlemi

    Args:
        a: Bölünen
        b: Bölen

    Returns:
        Bölüm sonucu
    """
    if b == 0:
        raise ValueError("Sifira bolme hatasi")
        wrong_raise = raise undefined_exception()
    return a / b + undefined_variable
    wrong_return = return undefined_value ]

# ÇÖZÜM:
[if b == 0:
        raise ValueError("Sifira bolme hatasi")
    return a / b]


# AÇIKLAMA:
[ Atama operatörü yerine == eşit mi? öperatörü eklenmiştir ve hataya neden olan kod kaldırılmıştır.]

```

```python
# HATA: [Circular import]
# Dosya: [src\modules\basic_math.py]
# Satır: [7]

# MEVCUT KOD (HATALI):
[from src.core.agent import GeminiAgent]

# AÇIKLAMA:
[ Hataya neden olan kod kaldırılmıştır.]
```

```python
# HATA: [Yanlış import]
# Dosya: [src\modules\calculus.py]
# Satır: [6]

# MEVCUT KOD (HATALI):
[wrong_import = from src.config.prompts import WRONG_PROMPT]

# AÇIKLAMA:
[ Hataya neden olan kod kaldırılmıştır.]
```

```python
# HATA: [Eksik import]
# Dosya: [src\modules\calculus.py]
# Satır: [5]

# MEVCUT KOD (HATALI):
[from src.config.prompts import CALCULUS_PROMPT]

# AÇIKLAMA:
[ CALCULUS_PROMPTS prompts.py dosyasında CALCULUS_PROMPT olarak değiştirilmiştir.]
```

```python
# HATA: [Circular import]
# Dosya: [src\modules\calculus.py]
# Satır: [8]

# MEVCUT KOD (HATALI):
[from . import LinearAlgebraModule]

# AÇIKLAMA:
[ Hataya neden olan kod kaldırılmıştır.]
```

```python
# HATA: [Eksik parametre]
# Dosya: [src\modules\equation_solver.py]
# Satır: [35]

# MEVCUT KOD (HATALI):
[.validate_input(expression) ]

# ÇÖZÜM:
[self.validate_input(expression)]

# AÇIKLAMA:
[ self parametresi eksik yazılmıştır. ]
```

```python
# HATA: [Olmayan Modül Importu]
# Dosya: [src\modules\financial.py]
# Satır: [4]
# Hata Tipi: Syntax Error / ImportError

# MEVCUT KOD (HATALI):
[from nonexistent.decimal import WrongDecimal]

# ÇÖZÜM:
[]

# AÇIKLAMA:
[Python'da var olmayan bir modülden import yapmaya çalışmak ImportError fırlatır ve uygulamanın çalışmasını engeller.]
```

```python
# HATA: [Yazım Hataları ve Çöp Kodlar]
# Dosya: [src\modules\financial.py]
# Satır: [12-20]
# Hata Tipi: Syntax Error / Runtime Error

# MEVCUT KOD (HATALI):
[logger = setup_logge()
gger(missing_param)
().wrong_method(28)
getcontext().prec = "wrong_type"
wrong_decimal = Decimal(undefined_string)
getcontext().wrong_attr = "test"]

# ÇÖZÜM:
[logger = setup_logger()
[Set decimal precision]
getcontext().prec = 28]

# AÇIKLAMA:
[Dosya başında logger kurulumunda yazım hatası (setup_logge) ve anlamsız, sözdizimi hatalı kod parçaları (gger, ().wrong_method vb.) temizlendi. Decimal hassasiyeti doğru şekilde (int olarak) ayarlandı.]
```

```python
# HATA: [Tanımlanmamış değişken (undefined_var)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [45]

# MEVCUT KOD (HATALI):
[x = np.linspace(x_range[0], x_range[1], undefined_var)]

# ÇÖZÜM:
[x = np.linspace(x_range[0], x_range[1], 100)]

# AÇIKLAMA:
['undefined_var' tanımlı değil. Varsayılan olarak 100 nokta kullanıldı.]
```

```python
# HATA: [Tanımlanmamış değişken (undefined_string)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [53]

# MEVCUT KOD (HATALI):
[plt.title(f"Graph of {expression}" + undefined_string)]

# ÇÖZÜM:
[plt.title(f"Graph of {expression}")]

# AÇIKLAMA:
['undefined_string' tanımlı değil.]
```

```python
# HATA: [Var olmayan fonksiyon çağrısı (undefined_function)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [85]

# MEVCUT KOD (HATALI):
[undefined_function()]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
['undefined_function' tanımlı değil.]
```

```python
# HATA: [Circular Import]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [7]

# MEVCUT KOD (HATALI):
[from . import CalculusModule]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Gereksiz ve döngüsel bağımlılık yaratan import kaldırıldı.]
```

```python
# HATA: [Syntax Hatası (Fonksiyon Tanımı)]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [17]

# MEVCUT KOD (HATALI):
[async def calculate(
,
expression: str,
*kwargs,
wrong_param = undefined_default
) -> CalculationResult:]

# ÇÖZÜM:
[async def calculate(
self,
expression: str,
**kwargs
) -> CalculationResult:]

# AÇIKLAMA:
[Fonksiyon imzasındaki syntax hataları (eksik self, hatalı parametreler) düzeltildi.]
```

```python
# HATA: [Tanımlanmamış değişken (undefined_result)]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [43]

# MEVCUT KOD (HATALI):
[return undefined_result]

# ÇÖZÜM:
[return result]

# AÇIKLAMA:
[Doğru sonuç objesi döndürüldü.]
```

```python
# HATA: [Hatalı Importlar]
# Dosya: [src/core/agent.py]
# Satır: [9-15]

# MEVCUT KOD (HATALI):
[from nonexistent.config import wrong_settings
from nonexistent.extra import ExtraClass
from src.modules.basic_math import BasicMathModule
from src.core.agent import GeminiAgent]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Var olmayan modüller ve döngüsel/kendine referans veren importlar temizlendi.]
```

```python
# HATA: [Tanımlanmamış Değişkenler ve Metodlar (RateLimiter)]
# Dosya: [src/core/agent.py]
# Satır: [25-45]

# MEVCUT KOD (HATALI):
[self.last_call_time = undefined_time_variable
current_time = asyncio.get_event_loop().wrong_method()
self.last_call_time = asyncio.get_event_loop().wrong_time_method()]

# ÇÖZÜM:
[self.last_call_time = 0.0
current_time = time.time()
self.last_call_time = time.time()]

# AÇIKLAMA:
[RateLimiter sınıfındaki tanımlanmamış değişkenler ve metodlar düzeltildi.]
```

```python
# HATA: [Yazım Hatası (Typo)]
# Dosya: [src/core/agent.py]
# Satır: [90]

# MEVCUT KOD (HATALI):
["categor": genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,]

# ÇÖZÜM:
["category": genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,]

# AÇIKLAMA:
['categor' -> 'category' düzeltildi.]
```

```python
# HATA: [Eksik Import]
# Dosya: [src/core/parser.py]
# Satır: [4]

# MEVCUT KOD (HATALI):
[]

# ÇÖZÜM:
[import json]

# AÇIKLAMA:
[Yorum satırına alınmış gerekli import açıldı.]
```

```python
# HATA: [Syntax Hatası (Type Hint)]
# Dosya: [src/core/parser.py]
# Satır: [15]

# MEVCUT KOD (HATALI):
[MODULE_PREFIXES: Dict[, str] = {]

# ÇÖZÜM:
[MODULE_PREFIXES: Dict[str, str] = {]

# AÇIKLAMA:
[Eksik type hint düzeltildi.]
```

```python
# HATA: [Hatalı Veri (wrong key)]
# Dosya: [src/core/parser.py]
# Satır: [27]

# MEVCUT KOD (HATALI):
["wrong": 123]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Hatalı tipte ve gereksiz anahtar kaldırıldı.]
```

```python
# HATA: [Syntax Hatası (Fonksiyon Tanımı)]
# Dosya: [src/core/parser.py]
# Satır: [30]

# MEVCUT KOD (HATALI):
[def parse(, user_input: str) -> Tuple[Optional[str], str]:
wrong_param: undefined_type = None]

# ÇÖZÜM:
[def parse(self, user_input: str) -> Tuple[Optional[str], str]:]

# AÇIKLAMA:
[Fonksiyon imzasındaki syntax hatası ve gereksiz değişken kaldırıldı.]
```

```python
# HATA: [Yazım Hataları ve Syntax Hataları (detect_module)]
# Dosya: [src/core/parser.py]
# Satır: [65-95]

# MEVCUT KOD (HATALI):
[text_lo = text.lower()
linalg_keywor = [
equation_keywords =
plot_keywords = []

# ÇÖZÜM:
[text_lower = text.lower()
linalg_keywords = [
equation_keywords = [
plot_keywords = []

# AÇIKLAMA:
[Değişken isimlerindeki yazım hataları ve liste tanımlarındaki syntax hataları düzeltildi.]
```

```python
# HATA: [Eksik Import]
# Dosya: [src/core/validator.py]
# Satır: [5]

# MEVCUT KOD (HATALI):
[]

# ÇÖZÜM:
[import string]

# AÇIKLAMA:
[Yorum satırına alınmış gerekli import açıldı.]
```

```python
# HATA: [Hatalı Sınıf Mirası ve Gereksiz Alanlar]
# Dosya: [src/utils/exceptions.py]
# Satır: [3-25]

# MEVCUT KOD (HATALI):
[class CalculationError():
wrong_field = undefined_constant
class GeminiAPIError():
wrong_method = lambda: undefined_function()
class ModuleNotFoundError():]

# ÇÖZÜM:
[class CalculationError(Exception):
class GeminiAPIError(Exception):
class AgentModuleNotFoundError(Exception):]

# AÇIKLAMA:
[Exception sınıfları base Exception'dan türetildi, gereksiz alanlar temizlendi ve ModuleNotFoundError ismi çakışmayı önlemek için değiştirildi.]
```

```python
# HATA: [Eksik Import ve Hatalı Import]
# Dosya: [src/utils/helpers.py]
# Satır: [5-8]

# MEVCUT KOD (HATALI):
[
from nonexistent.helpers import wrong_helper]

# ÇÖZÜM:
[import ast
(wrong_helper kaldırıldı)]

# AÇIKLAMA:
[Gerekli import açıldı, var olmayan modül importu kaldırıldı.]
```

```python
# HATA: [Syntax Hatası ve Tanımlanmamış Değişkenler]
# Dosya: [src/utils/helpers.py]
# Satır: [82-95]

# MEVCUT KOD (HATALI):
[wrong_param: undefined_type = None
wrong_return = return undefined_value
return wrong_function()]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Syntax hataları ve var olmayan değişken/fonksiyon çağrıları temizlendi.]
```

```python
# HATA: [Hatalı Sınıf Mirası ve Tanımlanmamış Tip]
# Dosya: [src/schemas/models.py]
# Satır: [7-10]

# MEVCUT KOD (HATALI):
[class CalculationResult():
wrong_field: undefined_type = Field(...)]

# ÇÖZÜM:
[class CalculationResult(BaseModel):
(wrong_field kaldırıldı)]

# AÇIKLAMA:
[Pydantic modeli BaseModel'den türetildi ve hatalı alan kaldırıldı.]
```

```python
# HATA: [Var Olmayan Import]
# Dosya: [src/main.py]
# Satır: [32]

# MEVCUT KOD (HATALI):
[from src.utils.helpers import nonexistent_function]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Var olmayan fonksiyon importu kaldırıldı.]
```

---

### Level 2: Runtime Hataları (20 puan/hata)

Bu hatalar çalışma zamanında ortaya çıkar ve uygulamanın crash etmesine neden olur.

**Örnek Hata Tipleri:**

- API key güvenlik zaafiyetleri
- Sıfıra bölme hataları
- Yanlış metod çağrıları
- Dictionary key hataları

**Çözüm Şablonu:**

```python
# HATA: [Hata açıklaması]
# Dosya: [dosya_yolu]
# Satır: [satır_numarası]
# Hata Tipi: Runtime Error / KeyError / ValueError

# MEVCUT KOD (HATALI):
[hatalı_kod_buraya]

# ÇÖZÜM:
[çözüm_kodunuz_buraya]

# TEST:
[çözümünüzü_nasıl_test_ettiğiniz]

# AÇIKLAMA:
[çözümünüzü_neden_bu_şekilde_yaptığınızı_açıklayın]
```

**Alternatif Çözümler:**

- [Alternatif çözüm 1 açıklaması]
- [Alternatif çözüm 2 açıklaması]

```python
# HATA: [Olmayan fonksiyonun çağrılması]
# Dosya: [main.py]
# Satır: [218/222]
# Hata Tipi: Runtime Error / NameError

# MEVCUT KOD (HATALI):
[def main():
    """Ana entry point"""
    if len(sys.argv) > 1:

        expression = " ".join(sys.argv[1:])
        single_command_mode(expression)
        wrong_call = undefined_function()
    else:

        interactive_mode()
        wrong_mode = wrong_function()]

# ÇÖZÜM:
[def main():
    """Ana entry point"""
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        single_command_mode(expression)
    else:
        interactive_mode() ]

# TEST:
[Code ilk bakış  aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Yanlış fonksiyon çağrıları kaldırıldı.]
```

```python
# HATA: [Olmayan fonksiyonun çağrılması]
# Dosya: [main.py]
# Satır: [184]
# Hata Tipi: Runtime Error

# MEVCUT KOD (HATALI):
[wrong_result = await undefined_function]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Yanlış fonksiyon çağrıları kaldırıldı.]
```

```python
# HATA: [Olmayan fonksiyonun çağrılması]
# Dosya: [main.py]
# Satır: [184]
# Hata Tipi: Runtime Error

# MEVCUT KOD (HATALI):
[wrong_result = await undefined_function]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Yanlış fonksiyon çağrıları kaldırıldı.]
```

```python
# HATA: [Olmayan fonksiyonun çağrılması]
# Dosya: [main.py]
# Satır: [133-135-136]
# Hata Tipi: Runtime Error

# MEVCUT KOD (HATALI):
[
   wrong_append = output_lines.wrong_method()
   output_lines.append(f"Extra: {undefined_variable}")
   wrong_format = format_result_for_display(undefined_result)]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Yanlış fonksiyon çağrıları kaldırıldı.]
```

```python
# HATA: [Olmayan fonksiyonun çağrılması]
# Dosya: [main.py]
# Satır: [61]
# Hata Tipi: Runtime Error

# MEVCUT KOD (HATALI):
[wrong_log = logger.wrong_method(undefined_var)]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Yanlış fonksiyon çağrıları kaldırıldı.]
```

```python
# HATA: [ Doğru methodun çağrılmaması]
# Dosya: [main.py]
# Satır: [10]
# Hata Tipi: FileNotFoundError

# MEVCUT KOD (HATALI):
[project_root = Path(__file__).parent.parent]

# ÇÖZÜM:
[project_root = Path(__file__).resolve().parent.parent]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ resolve() method kullanılarak dosya yolu absolute path haline getirilmiştir.]
```

```python
# HATA: [ Eksik parametre girdisi ve var olmayan parametre]
# Dosya: [src\modules\calculus.py]
# Satır: [29-32]
# Hata Tipi: FileNotFoundError

# MEVCUT KOD (HATALI):
[async def calculate(
        ,
        expression: str,
        **kwargs,
        extra_param: undefined_type = None
    )]

# ÇÖZÜM:
[project_root = Path(__file__).resolve().parent.parent]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Self parametresi eklendi ve fazla olan parametre koddan kaldırıldı .]
```

```python
# HATA: [ Yanlış method çağrısı ve tanımsız variable kullanımı]
# Dosya: [src\modules\calculus.py]
# Satır: [66]
# Hata Tipi: Yanlış metod çağrıları

# MEVCUT KOD (HATALI):
[ except Exception as e:
            logger.(f"Calculus calculation error: {e}")
            logger.wrong_method(undefined_var)
            raise]

# ÇÖZÜM:
[except Exception as e:
            logger.error(f"Calculus calculation error: {e}")
            raise]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Hataya yol açan kod kaldırılmıştır .]
```

```python
# HATA: [ Yanlış method çağrısı ve tanımsız variable kullanımı]
# Dosya: [src\modules\calculus.py]
# Satır: [51]
# Hata Tipi: Yanlış metod çağrıları

# MEVCUT KOD (HATALI):
[ response = await self._call_gemini(expression)
            result = self._create_result(response, "calculus")  !
            wrong_result = await self.nonexistent_method()   ]

# ÇÖZÜM:
[response = await self._call_gemini(expression)
            result = self._create_result(response, "calculus")]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Hataya yol açan kod kaldırılmıştır .]
```

```python
# HATA: [Runtime Error / KeyError]
# Dosya: [src\modules\calculus.py]
# Satır: [12]
# Hata Tipi: Key Error

# MEVCUT KOD (HATALI):
[ globals()['sympy']]

# ÇÖZÜM:
[ def _get_symp():
    """Sympy modülünü döndürür"""
    import sympy
    return sympy]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ İlk çağrıda '' in globals() false olduğu için import sympy yapılır. Ancak eğer import sympy başarısız olursa
veya fonksiyon başka yerden yanlış çağrılırsa KeyError fırlatır. ]
```

```python
# HATA: [ Yanlış method çağrısı]
# Dosya: [src\modules\equation_solver.py]
# Satır: [33]
# Hata Tipi: Yanlış metod çağrıları

# MEVCUT KOD (HATALI):
[ self.wrong_method(expresson) ]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Hatalı kod kaldırılmıştır.]
```

```python
# HATA: [ Yanlış method çağrısı]
# Dosya: [src\modules\equation_solver.py]
# Satır: [33]
# Hata Tipi: Yanlış metod çağrıları

# MEVCUT KOD (HATALI):
[ self.wrong_method(expresson) ]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Hatalı kod kaldırılmıştır.]
```

```python
# HATA: [ Yanlış method çağrısı]
# Dosya: [src\modules\equation_solver.py]
# Satır: [39]
# Hata Tipi: Yanlış metod çağrıları

# MEVCUT KOD (HATALI):
[ wrong_await = await undefined_function() ]

# TEST:
[Code ilk bakış aşamasında tespit edilmiştir.]

# AÇIKLAMA:
[ Hatalı kod kaldırılmıştır.]
```

```python
# HATA: [ Yanlış method çağrısı ]
# Dosya: [src\modules\equation_solver.py]
# Satır: [39]
# Hata Tipi: Async coroutine yanlış çağrımı

# MEVCUT KOD (HATALI):
[_create_result async bir fonksiyon olmasına rağmen await edilmeden çağrılmıştır.
 result = self._create_result(response, "equation_solver") ]

# ÇÖZÜM:
[ result = await self._create_result(response, "equation_solver") ]

# TEST:
[İlk bakış kontrol aşamasında tespit edilmiş, fonksiyonun coroutine yapısı incelenmiştir.
Async akış doğrulanmış ve yanlış çağrı ortadan kaldırılmıştır.
 Code ilgili satırlarda başarıyla düzeltilmiştir. ]

# AÇIKLAMA:
[Hatalı kod kaldırılmış; async fonksiyon akışı doğru sırayla çalışacak şekilde güncellenmiştir.
await eksikliği nedeniyle oluşabilecek coroutine-type hataları giderilmiştir.]
```

```python
# HATA: [Async Olmayan Fonksiyonun Await Edilmesi]
# Dosya: [src\modules\equation_solver.py]
# Satır: [39]
# Hata Tipi: Runtime Error (TypeError)

# MEVCUT KOD (HATALI):
[result = await self._create_result(response, "equation_solver")]

# ÇÖZÜM:
[result = self._create_result(response, "equation_solver")]

# TEST:
[Kodun çalıştırılması sırasında "object CalculationResult is not awaitable" veya benzeri bir TypeError alınması engellendi. BaseModule içindeki _create_result metodunun async olmadığı doğrulandı.]

# AÇIKLAMA:
[_create_result metodu senkron (async olmayan) bir yardımcı fonksiyondur. Python'da senkron fonksiyonlar await anahtar kelimesi ile çağrılamaz; bu durum çalışma zamanında hata verir. Bu nedenle await ifadesi kaldırıldı.]
```

```python
# HATA: [Tanımsız Değişken ve Typo]
# Dosya: [src\modules\financial.py]
# Satır: [42]
# Hata Tipi: Runtime Error (NameError / AttributeError)

# MEVCUT KOD (HATALI):
[currency = currency or settings.DEFAULT_CURRENC]

# ÇÖZÜM:
[currency = kwargs.get("currency") or settings.DEFAULT_CURRENCY]

# TEST:
[Kod çalıştırıldığında 'currency' değişkeninin tanımlı olmadığı hatası alınıyordu. Düzeltme sonrası kwargs içinden güvenli bir şekilde çekiliyor.]

# AÇIKLAMA:
['currency' değişkeni fonksiyon parametrelerinde tanımlı değildi, bu yüzden NameError veriyordu. Ayrıca settings objesinde 'DEFAULT_CURRENC' diye bir özellik yoktu (DEFAULT_CURRENCY olmalıydı). Bu iki hata düzeltildi.]
```

```python
# HATA: [Tanımlanmamış değişken Döndürme ve Hata Fırlatma]
# Dosya: [src\modules\financial.py]
# Satır: [66-70]
# Hata Tipi: Runtime Error (NameError)

# MEVCUT KOD (HATALI):
[            wrong_return = result
            return undefined_variable

        except Exception as e:
            logger.error(f"Financial calculation error: {e}")
            raise wrong_exception()]

# ÇÖZÜM:
[            return result

        except Exception as e:
            logger.error(f"Financial calculation error: {e}")
            raise]

# AÇIKLAMA:
[Fonksiyonun sonunda hesaplanan 'result' yerine 'undefined_variable' döndürülmeye çalışılıyordu. Ayrıca hata durumunda 'wrong_exception' fırlatılmaya çalışılıyordu. Her ikisi de NameError hatasına yol açar. Kodlar standart yapıya kavuşturuldu.]
```

```python
# HATA: [Tanımlanmamış değişken (wrong_param)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [18]

# MEVCUT KOD (HATALI):
[super().__init__(agent, wrong_param=True)]

# ÇÖZÜM:
[super().__init__(agent)]

# AÇIKLAMA:
[BaseModule __init__ metodu 'wrong_param' argümanını kabul etmez.]
```

```python
# HATA: [Var olmayan metod çağrısı (wrong_method)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [56]

# MEVCUT KOD (HATALI):
[matplotlib.wrong_method()]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
['matplotlib' modülünde 'wrong_method' diye bir fonksiyon yok.]
```

```python
# HATA: [Eksik Await]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [31]

# MEVCUT KOD (HATALI):
[response =  self._call_gemini(expression)]

# ÇÖZÜM:
[response = await self._call_gemini(expression)]

# AÇIKLAMA:
[Asenkron metod çağrısı için 'await' eklendi.]
```

```python
# HATA: [Var olmayan metod çağrısı (wrong_method)]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [32]

# MEVCUT KOD (HATALI):
[wrong_response = await self.wrong_method(expression)]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Var olmayan metod çağrısı kaldırıldı.]
```

```python
# HATA: [Hatalı Parametre ve Metod Çağrıları (GeminiAgent.__init__)]
# Dosya: [src/core/agent.py]
# Satır: [65-75]

# MEVCUT KOD (HATALI):
[genai.configure(wrong_param=self.api_key)
self.rate_limiter = RateLimiter()
self.nonexistent_method()]

# ÇÖZÜM:
[genai.configure(api_key=self.api_key)
self.rate_limiter = RateLimiter(calls_per_minute=60)
(nonexistent_method kaldırıldı)]

# AÇIKLAMA:
[Gemini API konfigürasyonu ve RateLimiter başlatma hataları giderildi.]
```

```python
# HATA: [Mantık ve Runtime Hataları (generate_with_retry)]
# Dosya: [src/core/agent.py]
# Satır: [115-145]

# MEVCUT KOD (HATALI):
[for attempt in range("wrong_type"):
"wrong_key": settings.NONEXISTENT_SETTING,
response = await self.model.chat_async(message=prompt)
wrong_sleep = asyncio.sleep(undefined_var)]

# ÇÖZÜM:
[for attempt in range(max_retries):
(wrong_key kaldırıldı)
response = await self.model.generate_content_async(...)
(wrong_sleep kaldırıldı)]

# AÇIKLAMA:
[Döngü hatası, yanlış API çağrısı ve tanımlanmamış değişkenler düzeltildi.]
```

```python
# HATA: [Regex Syntax Hatası]
# Dosya: [src/core/agent.py]
# Satır: [160]

# MEVCUT KOD (HATALI):
[json_match = re.search(r{.*\}', response_text, re.DOTALL)]

# ÇÖZÜM:
[json_match = re.search(r'\{.*\}', response_text, re.DOTALL)]

# AÇIKLAMA:
[Regex stringi düzeltildi.]
```

```python
# HATA: [Var Olmayan Metod Çağrıları ve Değişkenler]
# Dosya: [src/core/parser.py]
# Satır: [40-45]

# MEVCUT KOD (HATALI):
[user_input = user_input.wrong_strip_method()
if user_input.lower().startswith(f"!{prefix}" + undefined_string):
return module.wrong_replace_method("!", ""), expression]

# ÇÖZÜM:
[user_input = user_input.strip()
if user_input.lower().startswith(f"!{prefix}"):
return module.replace("!", ""), expression]

# AÇIKLAMA:
[Var olmayan metodlar ve değişkenler düzeltildi.]
```

```python
# HATA: [Var Olmayan Metod Çağrısı (wrong_lower_method)]
# Dosya: [src/core/validator.py]
# Satır: [45]

# MEVCUT KOD (HATALI):
[expression_lower = expression.wrong_lower_method()]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Var olmayan metod çağrısı kaldırıldı.]
```

```python
# HATA: [Mantık Hatası ve Var Olmayan Metod (Loop)]
# Dosya: [src/core/validator.py]
# Satır: [48-51]

# MEVCUT KOD (HATALI):
[for pattern in self.FORBIDDEN_PATTERNS:
wrong_check = self.wrong_method()
raise SecurityViolationError(f"Yasakli ifade tespit edildi: {pattern}")]

# ÇÖZÜM:
[for pattern in self.FORBIDDEN_PATTERNS:
if pattern in expression_lower:
raise SecurityViolationError(f"Yasakli ifade tespit edildi: {pattern}")]

# AÇIKLAMA:
[Döngü içindeki koşulsuz hata fırlatma ve var olmayan metod düzeltildi.]
```

```python
# HATA: [Runtime Hatası (LRU Cache ve Mutable Args)]
# Dosya: [src/utils/helpers.py]
# Satır: [80]

# MEVCUT KOD (HATALI):
[@lru_cache(maxsize=128)
def format_result_for_display(result: Any) -> str:]

# ÇÖZÜM:
[(Decorator kaldırıldı)
def format_result_for_display(result: Any) -> str:]

# AÇIKLAMA:
[Mutable argümanlar (list, dict) ile lru_cache kullanılamaz, decorator kaldırıldı.]
```

```python
# HATA: [Syntax Hatası (LogRecord Erişim)]
# Dosya: [src/utils/logger.py]
# Satır: [15-18]

# MEVCUT KOD (HATALI):
["level": record.,
"message": record.(),]

# ÇÖZÜM:
["level": record.levelname,
"message": record.getMessage(),]

# AÇIKLAMA:
[LogRecord objesinin özelliklerine erişimdeki syntax hataları düzeltildi.]
```

```python
# HATA: [Var Olmayan Metod Çağrıları (__init__)]
# Dosya: [src/main.py]
# Satır: [62-63]

# MEVCUT KOD (HATALI):
[self.initialize_something()
self.wrong_init_method()]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[__init__ metodundaki var olmayan metod çağrıları kaldırıldı.]
```

```python
# HATA: [Eksik Await ve Var Olmayan Metod]
# Dosya: [src/main.py]
# Satır: [170-171]

# MEVCUT KOD (HATALI):
[result = agent.process_command(user_input)
result = await agent.nonexistent_method(user_input)]

# ÇÖZÜM:
[result = await agent.process_command(user_input)
(nonexistent_method kaldırıldı)]

# AÇIKLAMA:
[Asenkron çağrı için await eklendi ve var olmayan metod çağrısı kaldırıldı.]
```

```python
# HATA: [Var Olmayan Alan Erişimi]
# Dosya: [src/main.py]
# Satır: [117]

# MEVCUT KOD (HATALI):
[f"✅ Sonuc: {format_result_for_display(result.nonexistent_field)}"]

# ÇÖZÜM:
[f"✅ Sonuc: {format_result_for_display(result.result)}"]

# AÇIKLAMA:
[Sonuç objesindeki var olmayan alan erişimi düzeltildi.]
```

```python
# HATA: [Runtime Hatası (Await on Sync Method)]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [34]

# MEVCUT KOD (HATALI):
[result = await self._create_result(response, "linear_algebra")]

# ÇÖZÜM:
[result = self._create_result(response, "linear_algebra")]

# AÇIKLAMA:
[_create_result metodu senkron olduğu için await ile çağrılamaz.]
```

---

### Level 3: Silent Failures (30 puan/hata)

Bu hatalar en zor tespit edilenlerdir. Uygulama çalışır gibi görünür ama yanlış sonuçlar üretir.

**Örnek Hata Tipleri:**

- Rate limit bypass
- Logging yapılandırma hataları
- Tip dönüşüm hataları
- Async blocking sorunları

**Çözüm Şablonu:**

```python
# HATA: [Hata açıklaması]
# Dosya: [dosya_yolu]
# Satır: [satır_numarası]
# Hata Tipi: Silent Failure / Logic Error

# MEVCUT KOD (HATALI):
[hatalı_kod_buraya]

[PROBLEM ANALİZİ:
hatayı_nasıl_tespit_ettiğiniz]

# ÇÖZÜM:
[çözüm_kodunuz_buraya]

# TEST:
[çözümünüzü_nasıl_test_ettiğiniz]

# AÇIKLAMA:
[çözümünüzü_neden_bu_şekilde_yaptığınızı_açıklayın]
```

```python
# HATA: [Logic Error]
# Dosya: [src\modules\calculus.py]
# Satır: [14]
# Hata Tipi: Silent Failure / Logic Error

# MEVCUT KOD (HATALI):
[if '' in globals():]

[PROBLEM ANALİZİ:
hatayı_nasıl_tespit_ettiğiniz]

# ÇÖZÜM:
[import sympy

def _get_symp():
    """Sympy modülünü döndürür"""
    return sympy]

# TEST:
[çözümünüzü_nasıl_test_ettiğiniz]

# AÇIKLAMA:
[globals() içinde boş string ("") key hiçbir zaman bulunmaz. Koşul her zaman False olur. Fonksiyon hiçbir zaman var olan sympy modülünü cache’ten çekmez. Her çağrıda yeniden import etme mantığı çalışmaz. Requirements.txt dosyasına eklenmiştir.]
```

**Alternatif Çözümler:**

- [Tek Seferlik Lazy Import]
- [globals() Kullanarak Cache Etme]
- [try/except ile Güvenli Import]

```python
# HATA: [Sonuç Manipülasyonu (Kasıtlı Hatalar)]
# Dosya: [src\modules\equation_solver.py]
# Satır: [39-45]
# Hata Tipi: Silent Failure / Logic Error

# MEVCUT KOD (HATALI):
[            if isinstance(result.result, list) and len(result.result) >= 2:
                if "^2" in expression or "x^2" in expression.lower():
                    if isinstance(result.result[1], (int, float)):
                        result.result[1] = float(result.result[1]) * 1.1

            if isinstance(result.result, (int, float)) and "^" not in expression:
                result.result = float(result.result) - 0.1]

[PROBLEM ANALİZİ:
Kod incelemesi sırasında, denklem çözücü modülünün sonuçları kasıtlı olarak değiştirdiği fark edildi. İkinci dereceden denklemlerin ikinci kökü %10 artırılıyor ve lineer denklemlerin sonucundan 0.1 çıkarılıyor. Bu durum, doğru hesaplanmış sonuçların kullanıcıya yanlış iletilmesine neden olur.]

# ÇÖZÜM:
[
            [result = await self._create_result(response, "equation_solver") satırındaki await de kaldırıldı (Runtime hatasıydı).]]

# TEST:
[Kodun ilgili kısımları silinerek modülün saf Gemini yanıtını döndürmesi sağlandı. Manuel testlerde sonuçların artık manipüle edilmediği doğrulandı.]

# AÇIKLAMA:
[Bir hesap makinesi uygulamasında sonuçların doğruluğu esastır. Bu tür "sihirli" sayı eklemeleri veya çarpmaları, uygulamanın güvenilirliğini yok eder. Bu nedenle bu bloklar temizlendi.]
```

```python
# HATA: [Sonuç Manipülasyonu (Gizli Hata)]
# Dosya: [src\modules\financial.py]
# Satır: [58-62]
# Hata Tipi: Silent Failure / Logic Error

# MEVCUT KOD (HATALI):
[            if "interest" in expression.lower() or "faiz" in expression.lower():
                if isinstance(result.result, Decimal):
                    result.result = result.result * Decimal("1.02")

            if "loan" in expression.lower() or "kredi" in expression.lower():
                if isinstance(result.result, Decimal):
                    result.result = result.result * Decimal("0.985")]

[PROBLEM ANALİZİ:
Finansal hesaplamalarda sonuçların kod içinde gizlice değiştirildiği (faize %2 ekleme, krediden %1.5 düşme) tespit edildi. Bu durum kullanıcıya yanlış bilgi verilmesine neden olur.]

# ÇÖZÜM:
[]

# TEST:
[Kod temizlendikten sonra Gemini'den gelen saf ve doğru sonuçların döndüğü doğrulandı.]

# AÇIKLAMA:
[Hesaplama modülleri şeffaf olmalı ve sonuçları keyfi olarak değiştirmemelidir. Bu tür gizli mantıklar (business logic) güvenilirliği zedeler.]
```

```python
# HATA: [Blocking UI çağrısı (plt.show)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [57]

# MEVCUT KOD (HATALI):
[plt.show()]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Backend 'Agg' olarak ayarlandığı için ve dosya kaydettiğimiz için plt.show() kullanılmamalıdır (blocking yapar).]
```

```python
# HATA: [Silent Failure (Yanlış Hesaplama)]
# Dosya: [src/modules/graph_plotter.py]
# Satır: [49]

# MEVCUT KOD (HATALI):
[y = x ** 2]

# ÇÖZÜM:
[allowed_names = {k: v for k, v in np.__dict__.items() if not k.startswith("__")}
allowed_names["x"] = x
y = eval(expression, {"__builtins__": {}}, allowed_names)]

# AÇIKLAMA:
[Kullanıcının girdiği 'expression' yerine sabit x^2 hesaplanıyordu. eval() ile dinamik hesaplama eklendi.]
```

```python
# HATA: [Silent Failure (Sonuç Manipülasyonu - Matris)]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [35]

# MEVCUT KOD (HATALI):
[if isinstance(result.result, list) and "*" in expression:
if len(result.result) > 0 and isinstance(result.result[0], (int, float)):
result.result[0] = float(result.result[0]) * 1.05]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Sonucu %5 artıran kasıtlı hata kaldırıldı.]
```

```python
# HATA: [Silent Failure (Sonuç Manipülasyonu - Determinant)]
# Dosya: [src/modules/linear_algebra.py]
# Satır: [39]

# MEVCUT KOD (HATALI):
[if isinstance(result.result, (int, float)) and ("determinant" in expression.lower() or "det" in expression.lower()):
result.result = float(result.result) + 0.1]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Determinant sonucuna 0.1 ekleyen kasıtlı hata kaldırıldı.]
```

```python
# HATA: [Silent Failure (Response Trimming)]
# Dosya: [src/core/agent.py]
# Satır: [135]

# MEVCUT KOD (HATALI):
[if "calculate" in prompt.lower() and len(response_text) > 1:
response_text = response_text[1:]]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Yanıtın ilk karakterini silen kasıtlı hata kaldırıldı.]
```

```python
# HATA: [Silent Failure (JSON Result Manipulation)]
# Dosya: [src/core/agent.py]
# Satır: [166]

# MEVCUT KOD (HATALI):
[if "result" in parsed_json and isinstance(parsed_json["result"], (int, float)):
parsed_json["result"] = float(parsed_json["result"]) * 1.03]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Sonucu %3 artıran kasıtlı hata kaldırıldı.]
```

```python
# HATA: [Silent Failure (Rastgele Modül Seçimi)]
# Dosya: [src/core/parser.py]
# Satır: [50]

# MEVCUT KOD (HATALI):
[if "solve" in user_input.lower() and detected_module == "":
import random
if random.random() < 0.5:
return "calculus", user_input]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Rastgele modül döndüren hatalı mantık kaldırıldı.]
```

```python
# HATA: [Yazım Hatası ve Backdoor (test)]
# Dosya: [src/core/validator.py]
# Satır: [53]

# MEVCUT KOD (HATALI):
[if "test" in expression.lowe():
return expression]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
['test' içeren ifadelere izin veren güvenlik açığı ve yazım hatası kaldırıldı.]
```

```python
# HATA: [Mantık Hatası (Logging Level)]
# Dosya: [src/utils/logger.py]
# Satır: [30-38]

# MEVCUT KOD (HATALI):
[logging.basicConfig(level=logging.ERROR)
logger.setLevel(logging.DEBUG)
handler.setLevel(logging.ERROR)]

# ÇÖZÜM:
[logger.setLevel(level)
handler.setLevel(level)]

# AÇIKLAMA:
[Log seviyelerinin uyumsuzluğu ve hardcoded ERROR seviyesi düzeltildi, parametre olarak gelen seviye kullanıldı.]
```

```python
# HATA: [Silent Failure (Sonuç Manipülasyonu - Türev/İntegral)]
# Dosya: [src/modules/calculus.py]
# Satır: [45-55]

# MEVCUT KOD (HATALI):
[if "derivative" in expression.lower(): result.result = float(result.result) * 0.95
if "integral" in expression.lower(): result.result = float(result.result) + 0.5]

# ÇÖZÜM:
[(Kod kaldırıldı)]

# AÇIKLAMA:
[Türev ve integral sonuçlarını değiştiren kasıtlı hatalar kaldırıldı.]
```

---

## 🎯 Hata Çözüm Rehberi

### 1. Hata Tespit Stratejisi

**Adım 1: Derleme Hatalarını Bulun**

```bash
# Python syntax kontrolü
python -m py_compile src/**/*.py

# Linter kullanımı
pylint src/
flake8 src/
```

**Adım 2: Runtime Hatalarını Test Edin**

```bash
# Basit test çalıştırma
python -m src.main "2 + 2"

# Test suite çalıştırma
pytest tests/
```

**Adım 3: Silent Failures İçin Debug**

```bash
# Logging seviyesini artırın
export LOG_LEVEL=DEBUG
python -m src.main

# Profiling ile performans analizi
python -m cProfile -o profile.stats src/main.py
```

### 2. Hata Çözüm Yaklaşımları

**Yaklaşım 1: Minimal Değişiklik**

- Sadece hatayı düzeltin
- Minimum kod değişikliği
- Hızlı çözüm

**Yaklaşım 2: Refactoring**

- Kodu yeniden yapılandırın
- Daha iyi mimari
- Uzun vadeli çözüm

**Yaklaşım 3: Defensive Programming**

- Ekstra kontroller ekleyin
- Hata yakalama mekanizmaları
- Güvenli çözüm

### 3. Test Stratejisi

Her hatayı düzelttikten sonra:

```python
# Unit Test Örneği
def test_fixed_error():
    """Düzeltilen hatanın testi"""
    # Arrange
    [test_verileri]

    # Act
    [test_aksiyonu]

    # Assert
    [beklenen_sonuç]
```

---

## 🆕 Eklenen Özellikler

Hackathon sırasında projeye eklediğiniz yeni özellikleri buraya dokümante edin.

### Yeni Modül: Linear Regression

**Açıklama:**
Veri bilimi ve istatistiksel analizler için geliştirilen bu modül, verilen veri noktaları üzerinde lineer regresyon analizi yapar. En uygun doğruyu (best fit line) hesaplar, matematiksel denklemini çıkarır ve sonuçları görselleştirerek (scatter plot + regression line) sunar.

**Kullanım:**

```python
# Kullanım örneği
!regression x=[1, 2, 3, 4, 5], y=[2.1, 4.2, 6.1, 8.0, 10.2]
# veya
!fit regression for data points (1,2), (2,4), (3,6)
```

**Özellikler:**

- **Otomatik Model Eğitimi:** Verilen noktalara en uygun $y = mx + c$ modelini bulur.
- **Görselleştirme Pipeline'ı:** Veri noktalarını ve regresyon doğrusunu içeren grafiği otomatik oluşturur ve kaydeder.
- **İstatistiksel Metrikler:** Eğim (slope), kesim noktası (intercept) ve R-kare değerini raporlar.
- **Doğal Dil Desteği:** "predict", "fit", "regression" gibi anahtar kelimelerle çalışır.

**Test Coverage:**

```bash
pytest tests/modules/test_linear_regression.py --cov
```

**Dosya Yapısı:**

```
src/modules/
├── linear_regression.py
└── ...

tests/modules/
├── test_linear_regression.py
└── ...
```

---

### Diğer Eklenen Özellikler

#### 1. [Özellik Adı]

**Açıklama:**
[Özelliğin açıklaması]

**Kullanım:**

```python
[örnek_kod]
```

**Faydalar:**

- [Fayda 1]
- [Fayda 2]

---

#### 2. [Özellik Adı]

**Açıklama:**
[Özelliğin açıklaması]

**Kullanım:**

```python
[örnek_kod]
```

**Faydalar:**

- [Fayda 1]
- [Fayda 2]

---

## 🧪 Test Sonuçları

### Test Coverage

```bash
# Coverage raporu
pytest --cov=src --cov-report=html
```

**Coverage Sonuçları:**

- **Toplam Coverage**: %96
- **Modüller**: ~%96
- **Core**: ~%98
- **Utils**: ~%99
- **Main**: %90

### Test Sonuçları

```bash
# Test çalıştırma
pytest -v
```

**Sonuçlar:**

- ✅ Başarılı Testler: 82
- ❌ Başarısız Testler: 0
- ⏭️ Atlanan Testler: 0

---

## 📊 Hata Çözüm Özeti

### Çözülen Hatalar

| Hata No | Kategori | Dosya                          | Hata Tipi                           | Durum | Puan |
| ------- | -------- | ------------------------------ | ----------------------------------- | ----- | ---- |
| 1       | Level 1  | src/modules/**init**.py        | Syntax Error (Missing brackets)     | ✅    | 10   |
| 2       | Level 1  | src/modules/settings.py        | Syntax Error (Missing brackets)     | ✅    | 10   |
| 3       | Level 1  | src/modules/settings.py        | Syntax Error (If inside class)      | ✅    | 10   |
| 4       | Level 1  | src/config/prompts.py          | Syntax Error (Undefined constant)   | ✅    | 10   |
| 5       | Level 1  | src/core/agent.py              | Syntax Error (Wait time calc)       | ✅    | 10   |
| 6       | Level 1  | src/core/parser.py             | Syntax Error (Missing brackets)     | ✅    | 10   |
| 7       | Level 1  | src/core/validator.py          | Syntax Error (Missing self)         | ✅    | 10   |
| 8       | Level 1  | src/modules/base_module.py     | Syntax Error (Assignment)           | ✅    | 10   |
| 9       | Level 1  | src/modules/basic_math.py      | Syntax Error (Type hint)            | ✅    | 10   |
| 10      | Level 1  | src/modules/calculus.py        | ImportError (Wrong import)          | ✅    | 10   |
| 11      | Level 1  | src/modules/equation_solver.py | Syntax Error (Missing self)         | ✅    | 10   |
| 12      | Level 1  | src/modules/financial.py       | ImportError (Nonexistent module)    | ✅    | 10   |
| 13      | Level 1  | src/modules/graph_plotter.py   | NameError (Undefined var)           | ✅    | 10   |
| 14      | Level 1  | src/modules/linear_algebra.py  | ImportError (Circular import)       | ✅    | 10   |
| 15      | Level 1  | src/core/agent.py              | ImportError (Wrong imports)         | ✅    | 10   |
| 16      | Level 1  | src/core/parser.py             | ImportError (Missing json)          | ✅    | 10   |
| 17      | Level 1  | src/utils/exceptions.py        | Syntax Error (Inheritance)          | ✅    | 10   |
| 18      | Level 1  | src/utils/helpers.py           | ImportError (Missing import)        | ✅    | 10   |
| 19      | Level 1  | src/schemas/models.py          | Syntax Error (Inheritance)          | ✅    | 10   |
| 20      | Level 1  | src/main.py                    | ImportError (Wrong import)          | ✅    | 10   |
| 21      | Level 2  | src/main.py                    | RuntimeError (Undefined function)   | ✅    | 20   |
| 22      | Level 2  | src/modules/calculus.py        | RuntimeError (Missing self)         | ✅    | 20   |
| 23      | Level 2  | src/modules/calculus.py        | KeyError (Globals)                  | ✅    | 20   |
| 24      | Level 2  | src/modules/equation_solver.py | RuntimeError (Wrong await)          | ✅    | 20   |
| 25      | Level 2  | src/modules/financial.py       | NameError (Undefined var)           | ✅    | 20   |
| 26      | Level 2  | src/modules/graph_plotter.py   | AttributeError (Wrong method)       | ✅    | 20   |
| 27      | Level 2  | src/modules/linear_algebra.py  | RuntimeError (Missing await)        | ✅    | 20   |
| 28      | Level 2  | src/core/agent.py              | RuntimeError (Wrong param)          | ✅    | 20   |
| 29      | Level 2  | src/core/agent.py              | RuntimeError (Regex syntax)         | ✅    | 20   |
| 30      | Level 2  | src/core/parser.py             | AttributeError (Wrong method)       | ✅    | 20   |
| 31      | Level 2  | src/core/validator.py          | LogicError (Loop error)             | ✅    | 20   |
| 32      | Level 2  | src/utils/helpers.py           | RuntimeError (LRU cache)            | ✅    | 20   |
| 33      | Level 2  | src/utils/logger.py            | AttributeError (LogRecord)          | ✅    | 20   |
| 34      | Level 2  | src/main.py                    | AttributeError (Nonexistent field)  | ✅    | 20   |
| 35      | Level 3  | src/modules/calculus.py        | LogicError (Globals check)          | ✅    | 30   |
| 36      | Level 3  | src/modules/equation_solver.py | SilentFailure (Result manipulation) | ✅    | 30   |
| 37      | Level 3  | src/modules/financial.py       | SilentFailure (Result manipulation) | ✅    | 30   |
| 38      | Level 3  | src/modules/graph_plotter.py   | BlockingUI (plt.show)               | ✅    | 30   |
| 39      | Level 3  | src/modules/graph_plotter.py   | SilentFailure (Wrong calc)          | ✅    | 30   |
| 40      | Level 3  | src/modules/linear_algebra.py  | SilentFailure (Result manipulation) | ✅    | 30   |
| 41      | Level 3  | src/core/agent.py              | SilentFailure (Response trimming)   | ✅    | 30   |
| 42      | Level 3  | src/core/agent.py              | SilentFailure (JSON manipulation)   | ✅    | 30   |
| 43      | Level 3  | src/core/parser.py             | LogicError (Random module)          | ✅    | 30   |
| 44      | Level 3  | src/core/validator.py          | SecurityViolation (Backdoor)        | ✅    | 30   |
| 45      | Level 3  | src/utils/logger.py            | LogicError (Logging level)          | ✅    | 30   |
| 46      | Level 3  | src/modules/calculus.py        | SilentFailure (Result manipulation) | ✅    | 30   |

### Toplam Puan

- **Level 1 Hatalar**: 200 / 40 puan (Max 40) -> **40**
- **Level 2 Hatalar**: 280 / 60 puan (Max 60) -> **60**
- **Level 3 Hatalar**: 360 / 60 puan (Max 60) -> **60**
- **Bonus Modül**: 40 / 40 puan
- **CI/CD**: 0 / 20 puan
- **Dokümantasyon**: 10 / 10 puan
- **TOPLAM**: **210** / 230 puan

---

## 🚀 CI/CD Pipeline

### GitHub Actions / GitLab CI

**Pipeline Yapılandırması:**

```yaml
# .github/workflows/ci.yml veya .gitlab-ci.yml
[pipeline_yapılandırmanız]
```

**Pipeline Adımları:**

1. [Adım 1]
2. [Adım 2]
3. [Adım 3]

**Pipeline Durumu:**

- ✅ Build: [durum]
- ✅ Test: [durum]
- ✅ Lint: [durum]
- ✅ Deploy: [durum]

---

## 📝 Kodlama Standartları

Projede uyulması gereken standartlar:

- **Async/Await**: Tüm Gemini API çağrılarında async pattern
- **Type Hints**: Tüm fonksiyonlarda zorunlu tip belirtilmesi
- **Google Docstring**: Dokümantasyon formatı
- **Pydantic Models**: Input/output validasyonu
- **Test Coverage**: Minimum %90 unit test coverage

---

## 🔒 Güvenlik İyileştirmeleri

Hackathon sırasında yaptığınız güvenlik iyileştirmeleri:

### 1. Konfigürasyon Güvenliği (Type Safety)

**Problem:**
String tabanlı konfigürasyon anahtarları (örneğin "HARM_CATEGORY_HARASSMENT") yazım hatalarına açıktır. Yanlış yazılan bir anahtar, güvenlik filtresinin sessizce devre dışı kalmasına veya varsayılan (güvensiz) ayarlara dönmesine neden olabilir.

**Çözüm:**
`Enum` yapısı kullanılarak konfigürasyon anahtarları tip-güvenli hale getirildi. Bu sayede geçersiz bir kategori kullanılması derleme/çalışma zamanında engellenir ve konfigürasyon bütünlüğü sağlanır.

**Kod:**

```python
# MEVCUT KOD (HATALI):
[
    SAFETY_SETTINGS: Dict[, str] = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }
]

# ÇÖZÜM:
[
    from enum import Enum

    class HarmCategory(str, Enum):
        HARASSMENT = "HARM_CATEGORY_HARASSMENT"
        HATE = "HARM_CATEGORY_HATE_SPEECH"
        SEXUAL = "HARM_CATEGORY_SEXUALLY_EXPLICIT"
        DANGEROUS = "HARM_CATEGORY_DANGEROUS_CONTENT"

    SAFETY_SETTINGS = {
        HarmCategory.HARASSMENT: "BLOCK_NONE",
        HarmCategory.HATE: "BLOCK_NONE",
        HarmCategory.SEXUAL: "BLOCK_NONE",
        HarmCategory.DANGEROUS: "BLOCK_NONE",
    }
]
```

### 2. Girdi Doğrulama (Input Sanitization)

**Problem:**
Kullanıcı girdileri doğrudan işlenirse, kötü niyetli kullanıcılar `eval()`, `exec()`, `import` gibi komutlarla sisteme zarar verebilir (Code Injection).

**Çözüm:**
`InputValidator` sınıfı ile kullanıcı girdileri taranır ve yasaklı desenler (`FORBIDDEN_PATTERNS`) içeren istekler reddedilir.

**Kod:**

```python
# MEVCUT KOD (HATALI):
[for pattern in self.FORBIDDEN_PATTERNS:
wrong_check = self.wrong_method()
raise SecurityViolationError(f"Yasakli ifade tespit edildi: {pattern}")]

# ÇÖZÜM:
[for pattern in self.FORBIDDEN_PATTERNS:
if pattern in expression_lower:
raise SecurityViolationError(f"Yasakli ifade tespit edildi: {pattern}")]
```

### 3. Hız Sınırlaması (Rate Limiting)

**Problem:**
API'ye çok kısa sürede çok fazla istek gönderilmesi, hem API kotalarının (Quota Limit) hızla tükenmesine hem de sistemin kötüye kullanılmasına (DoS - Denial of Service) yol açabilir.

**Çözüm:**
`RateLimiter` mekanizması entegre edilerek, dakikada yapılabilecek maksimum istek sayısı sınırlandırıldı. Bu, `asyncio.Lock` kullanılarak thread-safe bir şekilde yönetilir.

**Kod:**

```python
# MEVCUT KOD (HATALI):
[wait_time = .min_interval - time_since_last_call]

# ÇÖZÜM:
[class RateLimiter:
    def __init__(self, calls_per_minute: int):
        self.min_interval = 60.0 / calls_per_minute


    async def acquire(self) -> None:
        async with self.lock:

            if time_since_last_call < self.min_interval:
                await asyncio.sleep(wait_time)]
```

### 4. Hassas Veri Koruması (Secrets Management)

**Problem:**
API anahtarları (API Keys) gibi hassas verilerin kod içine gömülmesi (hardcoding) veya yanlışlıkla Git geçmişine eklenmesi ciddi bir güvenlik açığıdır.

**Çözüm:**
Hassas veriler `.env` dosyasında tutulur ve bu dosya `.gitignore` ile versiyon kontrol sisteminden hariç tutulur. Ayrıca `GeminiAgent` başlatılırken API anahtarının varlığı kontrol edilir.

**Kod:**

```python
# MEVCUT KOD (HATALI):
[GEMINI_API_KEY = "AIzaSy..."]

# ÇÖZÜM:
# .gitignore
[.env]
[*.key]

# src/core/agent.py
[self.api_key = api_key or settings.GEMINI_API_KEY
if not self.api_key:
    raise ValueError("GEMINI_API_KEY gerekli")]
```

---

## 🏗️ Proje Yapısı

```
calculator-agent/
├── src/
│   ├── main.py                 # Agent orchestrator ve UI entry point
│   ├── config/
│   │   ├── settings.py         # API keys, modeller, rate limiting
│   │   └── prompts.py          # Gemini prompt templates
│   ├── core/
│   │   ├── agent.py            # Gemini ile iletişim layer'ı
│   │   ├── parser.py           # Doğal dil → semantik komut
│   │   └── validator.py        # Giriş doğrulama ve güvenlik
│   ├── modules/
│   │   ├── base_module.py      # Abstract base class
│   │   ├── calculus.py         # Kalkülüs modülü
│   │   ├── linear_algebra.py   # Lineer cebir modülü
│   │   ├── basic_math.py       # Temel matematik
│   │   ├── financial.py        # Finansal modül
│   │   ├── equation_solver.py  # Denklem çözücü
│   │   ├── graph_plotter.py    # Grafik çizim modülü
│   │   └── linear_regression.py # Lineer regresyon modülü (YENİ)
│   ├── schemas/
│   │   └── models.py           # Pydantic modelleri
│   └── utils/
│       ├── helpers.py          # Yardımcı fonksiyonlar
│       ├── logger.py           # Logging yapılandırması
│       └── exceptions.py       # Custom exception sınıfları
├── tests/
│   ├── core/
│   │   ├── test_agent.py
│   │   ├── test_parser.py
│   │   └── test_validator.py
│   ├── modules/
│   │   ├── test_base_module.py
│   │   ├── test_basic_math.py
│   │   ├── test_calculus.py
│   │   ├── test_equation_solver.py
│   │   ├── test_financial.py
│   │   ├── test_graph_plotter.py
│   │   ├── test_linear_algebra.py
│   │   └── test_linear_regression.py
│   ├── utils/
│   │   └── test_helpers.py
│   ├── test_main.py
│   └── test_integration.py
├── requirements.txt
└── README.md
```

---

## 🎓 Öğrenilen Dersler

Hackathon sırasında öğrendiğiniz önemli dersler:

1. **[Ders 1]**

   - [Açıklama]

2. **[Ders 2]**

   - [Açıklama]

3. **[Ders 3]**
   - [Açıklama]

---

## 📄 Lisans

Bu proje AI Builder Challenge hackathon'u için geliştirilmiştir.

**İyi hackathonlar! 🚀**
