class Vidrio:
    def __init__(self, tipo: str, esmerilado: bool = False):
        self.tipo = tipo  # Transparente, Bronce, Azul
        self.esmerilado = esmerilado

    def calcular_precio_cm2(self) -> float:
        """Calcula el costo del vidrio por cm², incluyendo el esmerilado si es necesario"""
        precios_base = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        precio = precios_base.get(self.tipo, 0)
        if self.esmerilado:
            precio += 5.20
        return precio
