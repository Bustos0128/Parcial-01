from .vidrio import Vidrio
from .acabado_aluminio import AcabadoAluminio

class Nave:
    def __init__(self, tipo: str, ancho: float, alto: float, vidrio: Vidrio, acabado: AcabadoAluminio):
        self.tipo = tipo  # 'X' o 'O'
        self.ancho = ancho
        self.alto = alto
        self.vidrio = vidrio
        self.acabado = acabado

    def calcular_costo_aluminio(self) -> float:
        """Calcula el costo del aluminio de acuerdo al perímetro de la nave"""
        perimetro = 2 * (self.ancho + self.alto)
        esquinas = 4 * 4310  # Cada esquina cuesta 4310 y se usan 4
        return perimetro * self.acabado.calcular_precio_cm_lineal() + esquinas

    def calcular_costo_vidrio(self) -> float:
        """Calcula el costo del vidrio, ajustando el tamaño por la inserción en el marco"""
        area_vidrio = (self.ancho - 1.5) * (self.alto - 1.5)
        return area_vidrio * self.vidrio.calcular_precio_cm2()

    def calcular_costo_total(self) -> float:
        """Calcula el costo total de la nave (aluminio + vidrio + chapa si es tipo X)"""
        costo_total = self.calcular_costo_aluminio() + self.calcular_costo_vidrio()
        if self.tipo == 'X':
            costo_total += 16200  # Costo de la chapa
        return costo_total
