from typing import List
from .nave import Nave

class EstiloVentana:
    def __init__(self, nombre: str, naves: List[Nave]):
        self.nombre = nombre  # O, XO, OXXO, OXO
        self.naves = naves

    def distribuir_naves(self, ancho: float, alto: float) -> List[Nave]:
        """Distribuye las naves según el estilo de la ventana"""
        if self.nombre == "XO":
            return [Nave(tipo="O", ancho=ancho/2, alto=alto, vidrio=self.naves[0].vidrio, acabado=self.naves[0].acabado),
                    Nave(tipo="X", ancho=ancho/2, alto=alto, vidrio=self.naves[1].vidrio, acabado=self.naves[1].acabado)]
        elif self.nombre == "OXXO":
            return [Nave(tipo="O", ancho=ancho/2, alto=alto, vidrio=self.naves[0].vidrio, acabado=self.naves[0].acabado),
                    Nave(tipo="X", ancho=ancho/2, alto=alto, vidrio=self.naves[1].vidrio, acabado=self.naves[1].acabado),
                    Nave(tipo="X", ancho=ancho/2, alto=alto, vidrio=self.naves[2].vidrio, acabado=self.naves[2].acabado),
                    Nave(tipo="O", ancho=ancho/2, alto=alto, vidrio=self.naves[3].vidrio, acabado=self.naves[3].acabado)]
        elif self.nombre == "OXO":
            return [Nave(tipo="O", ancho=ancho/3, alto=alto, vidrio=self.naves[0].vidrio, acabado=self.naves[0].acabado),
                    Nave(tipo="X", ancho=ancho/3, alto=alto, vidrio=self.naves[1].vidrio, acabado=self.naves[1].acabado),
                    Nave(tipo="O", ancho=ancho/3, alto=alto, vidrio=self.naves[2].vidrio, acabado=self.naves[2].acabado)]
        else:
            return self.naves  # Por defecto, devolver las naves sin distribución.
