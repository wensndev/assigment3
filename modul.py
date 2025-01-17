from typing import Optional, Any
import math

def power(base: float, exponent: float) -> float:
    # üs alma fonksiyonu
    try:
        # isNaN mecvut olsa da yine de tür kontrolü yapmak istedim
        if not all(isinstance(x, float) for x in (base, exponent)):
            raise ValueError("Faktöriyel sadece sayılar için hesaplanabilir")
        # kompleks sayı kontrolü
        if isinstance(base, complex) or isinstance(exponent, complex):
            raise ValueError("Kompleks sayılar desteklenmez")
        result = base ** exponent
        if math.isinf(result) or math.isnan(result):
            raise OverflowError
        return result
    except OverflowError:
        raise ValueError("Çok büyük bir sayının üssü hesaplanamaz")

def factorial(n: int) -> int:
    # faktöriyel hesaplama fonksiyonu
    if not isinstance(n, int):
        raise ValueError("Faktöriyel sadece tam sayılar için hesaplanabilir")
    if n < 0:
        raise ValueError("Negatif sayıların faktöriyeli hesaplanamaz")
    # cpu'yu seviyoruz
    if n > 500:
        raise ValueError("500'den büyük sayıların faktöriyeli hesaplanamaz")
    return math.factorial(n)

def gcd(a: int, b: int) -> int:
    # EBOB hesaplama fonksiyonu
    if not all(isinstance(x, int) for x in (a, b)):
        raise ValueError("EBOB sadece tam sayılar için hesaplanabilir")
    if a == 0 and b == 0:
        raise ValueError("İki sayı da sıfır olamaz")
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    # EKOK hesaplama fonksiyonu
    if not all(isinstance(x, int) for x in (a, b)):
        raise ValueError("EKOK sadece tam sayılar için hesaplanabilir")
    if a == 0 or b == 0:
        raise ValueError("Sıfır için EKOK hesaplanamaz")
    try:
        return abs(a * b) // gcd(a, b)
    except OverflowError:
        raise ValueError("Sayılar çok büyük")

def is_prime(n: int) -> bool:
    # asal sayı kontrolü fonksiyonu
    if not isinstance(n, int):
        raise ValueError("Asal sayı kontrolü sadece tam sayılar için yapılabilir")
    if n < 0:
        raise ValueError("Negatif sayılar asal olamaz")
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

def isNaN(value: Any, inter: Optional[str] = None) -> bool:
    # isNaN ama bu sefer isinstance kullanmayı öğrendim
    if value is None:
        return True
    if inter:
        return not (isinstance(value, int) or (isinstance(value, str) and value.strip('-').isdigit()))
    return not (isinstance(value, float) or (isinstance(value, str) and value.replace('.','',1).strip('-').isdigit()))