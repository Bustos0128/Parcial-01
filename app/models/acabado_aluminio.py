class AcabadoAluminio:
    def __init__(self, tipo: str):
        self.tipo = tipo  # Pulido, Lacado Brillante, Lacado Mate, Anodizado

    def calcular_precio_cm_lineal(self) -> float:
        precios_acabado = {
            "Pulido": 50700 / 100,  # Convertido a precio por cm lineal
            "Lacado Brillante": 54200 / 100,
            "Lacado Mate": 53600 / 100,
            "Anodizado": 57300 / 100
        }
        return precios_acabado.get(self.tipo, 0)
