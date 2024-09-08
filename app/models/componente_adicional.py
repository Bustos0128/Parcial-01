class ComponenteAdicional:
    def __init__(self, nombre: str, precio_unitario: float):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def calcular_costo_total(self, cantidad: int) -> float:
        return self.precio_unitario * cantidad
