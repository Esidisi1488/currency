from decimal import Decimal, ROUND_DOWN


def to_2_places_decimal_privat(value: str) -> Decimal:
    return Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN)


def to_2_places_decimal_mono(value):
    return Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
