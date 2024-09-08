from .vidrio import Vidrio
from .acabado_aluminio import AcabadoAluminio
from .componente_adicional import ComponenteAdicional

componente_esquinas = ComponenteAdicional(nombre="Esquinas", precio_unitario=4310)
componente_chapa = ComponenteAdicional(nombre="Chapa", precio_unitario=16200)

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
        esquinas = componente_esquinas.calcular_costo_total(cantidad=4)  # 4 esquinas
        return perimetro * self.acabado.calcular_precio_cm_lineal() + esquinas
    
    def calcular_costo_vidrio(self) -> float:
        """Calcula el costo del vidrio, ajustando el tamaño por la inserción en el marco"""
        area_vidrio = (self.ancho - 1.5) * (self.alto - 1.5)  # Ajuste de 1.5cm en cada lado
        return area_vidrio * self.vidrio.calcular_precio_cm2()

    def calcular_costo_total(self) -> float:
        """Calcula el costo total de la nave (aluminio + vidrio + chapa si es tipo X)"""
        costo_total = self.calcular_costo_aluminio() + self.calcular_costo_vidrio()
        if self.tipo == 'X':
            costo_total += componente_chapa.calcular_costo_total(cantidad=1)  # 1 chapa
        return costo_total