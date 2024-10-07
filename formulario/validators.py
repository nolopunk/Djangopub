# mi_app/validators.py
import re
from django.core.exceptions import ValidationError

def validar_rut(value):
    """
    Valida un RUT chileno.
    
    El RUT puede estar en el formato '12345678-9' o '12345678K'.
    """
    rut_pattern = re.compile(r'^\d{7,8}-[0-9kK]$')
    
    if not rut_pattern.match(value):
        raise ValidationError('El formato del RUT es inválido. Debe ser 12345678-9 o 12345678-K.')

    rut, dv = value.split('-')
    rut = rut.zfill(8)  # Completa con ceros a la izquierda si es necesario

    # Cálculo del dígito verificador
    suma = 0
    multiplicador = 2

    for digit in reversed(rut):
        suma += int(digit) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    dv_calculado = 11 - (suma % 11)

    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)

    if dv_calculado != dv.upper():
        raise ValidationError('El RUT ingresado es inválido.')
