from typing import List, Dict
from .ventana import Ventana

class Cotizacion:
    def __init__(self, ventanas: List[Ventana], descuento: float = 0.0):
        self.ventanas = ventanas
        self.descuento = descuento

    def calcular_total_sin_descuento(self) -> float:
        return sum(ventana.calcular_costo() for ventana in self.ventanas)

    def aplicar_descuento(self) -> float:
        total = self.calcular_total_sin_descuento()
        if len(self.ventanas) > 100:
            return total * 0.9  # Aplica un 10% de descuento
        return total

    def generar_resumen(self) -> Dict:
        resumen = {
            "cantidad_ventanas": len(self.ventanas),
            "total_sin_descuento": self.calcular_total_sin_descuento(),
            "total_con_descuento": self.aplicar_descuento(),
        }
        return resumen
