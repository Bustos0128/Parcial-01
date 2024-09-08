from .estilo_ventana import EstiloVentana

class Ventana:
    def __init__(self, ancho: float, alto: float, estilo: EstiloVentana):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.naves = estilo.distribuir_naves(ancho, alto)

    def calcular_costo(self) -> float:
        """Calcula el costo total de la ventana sumando el costo de sus naves"""
        return sum(nave.calcular_costo_total() for nave in self.naves)