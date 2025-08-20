from typing import Union, List

# Tasas porcentuales sobre el precio base
TAX_RATES = {
    "exento": 0.00,
    "iva19":  0.19,
    "iva5":   0.05,
    "inc8":   0.08,
    "licor25": 0.25,
}

# Valor fijo por bolsa
BOLSA_FIJA = 50


class CalculadoraImpuestos:
    """
    Calcula el total a pagar aplicando impuestos.

    Reglas:
    - Si el tipo de impuesto es str: aplica un solo impuesto (porcentaje sobre base o 'bolsa' fija).
    - Si es list[str]: aplica cada impuesto de la lista (porcentajes sobre base + 'bolsa' fija si aparece).
    - Redondea el total al entero más cercano.

    Validaciones (estilo TDD):
    - precio_base debe ser numérico (int/float) y >= 0.
    - tipo_impuesto debe ser str no vacío o list[str] no vacía de strings no vacíos.
    - tipos desconocidos -> ValueError.
    - precio no numérico -> TypeError.
    """

    def __init__(self, precio_base: Union[int, float], tipo_impuesto: Union[str, List[str]]):
        self.precio_base = precio_base
        self.tipo_impuesto = tipo_impuesto

    # -------- Validaciones --------
    def _validar(self) -> None:
        # precio_base numérico
        if not isinstance(self.precio_base, (int, float)):
            raise TypeError("El precio base debe ser numérico (int o float).")

        # precio_base no negativo
        if self.precio_base < 0:
            raise ValueError("El precio base no puede ser negativo.")

        # tipo_impuesto válido
        if isinstance(self.tipo_impuesto, str):
            if self.tipo_impuesto.strip() == "":
                raise ValueError("El tipo de impuesto no puede ser vacío.")
        elif isinstance(self.tipo_impuesto, list):
            if len(self.tipo_impuesto) == 0:
                raise ValueError("La lista de impuestos no puede estar vacía.")
            # Todos los elementos deben ser strings no vacíos
            for t in self.tipo_impuesto:
                if not isinstance(t, str) or t.strip() == "":
                    raise ValueError("Todos los impuestos deben ser cadenas no vacías.")
        else:
            raise TypeError("El tipo de impuesto debe ser una cadena o una lista de cadenas.")

    # -------- Aplicación de impuestos --------
    def _aplicar_un_impuesto(self, acumulado: float, tipo: str) -> float:
        tipo = tipo.strip().lower()

        if tipo == "bolsa":
            return acumulado + BOLSA_FIJA

        if tipo in TAX_RATES:
            return acumulado + (self.precio_base * TAX_RATES[tipo])

        # Impuesto desconocido
        raise ValueError(f"Tipo de impuesto desconocido: {tipo}")

    def calcular(self) -> int:
        self._validar()

        total = float(self.precio_base)

        # Un solo impuesto
        if isinstance(self.tipo_impuesto, str):
            total = self._aplicar_un_impuesto(total, self.tipo_impuesto)
            return round(total)

        # Varios impuestos
        for t in self.tipo_impuesto:
            total = self._aplicar_un_impuesto(total, t)

        return round(total)

