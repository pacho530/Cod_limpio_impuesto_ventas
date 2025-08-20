from typing import Union, List

class TipoImpuestoDesconocidoError(ValueError):
    pass

class TipoImpuestoInvalidoError(TypeError):
    pass

class PrecioInvalidoError(ValueError):
    pass


TAX_RATES = {
    "exento": 0.00,   # sin impuesto
    "iva19":  0.19,   # IVA 19%
    "iva5":   0.05,   # IVA 5%
    "inc8":   0.08,   # Impuesto al consumo 8%
    "licor25": 0.25,  # Licores 25%
}

BOLSA_FIJA = 50  # valor fijo por bolsa


class CalculadoraImpuestos:
    """
    Calcula el total a pagar aplicando impuestos.
    - tipo_impuesto puede ser str (un solo impuesto) o list[str] (varios).
    - Porcentuales se aplican sobre el precio_base.
    - 'bolsa' suma un valor fijo (BOLSA_FIJA).
    Validaciones:
    - precio_base numérico y >= 0
    - tipo_impuesto str no vacío o lista no vacía de strings no vacíos
    - tipos desconocidos -> TipoImpuestoDesconocidoError
    """

    def __init__(self, precio_base: Union[int, float], tipo_impuesto: Union[str, List[str]]):
        self.precio_base = precio_base
        self.tipo_impuesto = tipo_impuesto

    def _validar(self) -> None:
        # precio_base
        if not isinstance(self.precio_base, (int, float)):
            raise TipoImpuestoInvalidoError("El precio base debe ser numérico (int o float).")
        if self.precio_base < 0:
            raise PrecioInvalidoError("El precio base no puede ser negativo.")

        # tipo_impuesto
        if isinstance(self.tipo_impuesto, str):
            if self.tipo_impuesto.strip() == "":
                raise TipoImpuestoDesconocidoError("El tipo de impuesto no puede ser vacío.")
        elif isinstance(self.tipo_impuesto, list):
            if len(self.tipo_impuesto) == 0:
                raise TipoImpuestoDesconocidoError("La lista de impuestos no puede estar vacía.")
            for t in self.tipo_impuesto:
                if not isinstance(t, str) or t.strip() == "":
                    raise TipoImpuestoDesconocidoError("Todos los impuestos deben ser cadenas no vacías.")
        else:
            raise TipoImpuestoInvalidoError("tipo_impuesto debe ser str o list[str].")

    def _aplicar_un_impuesto(self, acumulado: float, tipo: str) -> float:
        tipo = tipo.strip().lower()

        if tipo == "bolsa":
            return acumulado + BOLSA_FIJA

        if tipo in TAX_RATES:
            return acumulado + (self.precio_base * TAX_RATES[tipo])

        raise TipoImpuestoDesconocidoError(f"Tipo de impuesto desconocido: {tipo}")

    def calcular(self) -> int:
        """
        Devuelve el total a pagar (entero redondeado).
        """
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
