# Requerimientos del Sistema de Cotización de Ventanas para PQR

## 1. Generalidades del Sistema
- Desarrollar un programa para automatizar el proceso de cotización de ventanas.
- El sistema debe permitir la actualización de estilos, precios y tamaños de las ventanas.
- Calcular el costo total de la ventana basado en los parámetros definidos: estilo, tipo de vidrio, acabado del aluminio, etc.

## 2. Estilos de Ventana
- Estilos de ventana a manejar:
  - O: Nave fija (no deslizante).
  - XO: Dos naves, una fija y una deslizante.
  - OXXO: Cuatro naves, dos fijas y dos deslizantes.
  - OXO: Tres naves, una fija y dos deslizantes.
- Nuevos estilos deben ser autorizados por la gerencia.

## 3. Dimensiones de la Ventana
- El ancho y el alto de la ventana deben ingresarse para calcular el costo.
- Cada estilo de ventana tiene una disposición específica de naves.
  - Ejemplo: Para una ventana XOX de 120cm x 90cm, cada nave mide 40cm x 90cm.
  
## 4. Materiales y Costos
### Acabados del Aluminio:
- Tipos de acabado:
  - Pulido: $50,700 por metro lineal.
  - Lacado Brillante: $54,200 por metro lineal.
  - Lacado Mate: $53,600 por metro lineal.
  - Anodizado: $57,300 por metro lineal.

### Tipos de Vidrio:
- Vidrios disponibles:
  - Transparente: $8.25 por cm².
  - Bronce: $9.15 por cm².
  - Azul: $12.75 por cm².
- Opción de vidrio esmerilado con costo adicional de $5.20 por cm².

### Componentes Adicionales:
- **Esquinas**: $4,310 por cada esquina (se usan 4 por ventana).
- **Chapa**: $16,200 por cada nave deslizante (nave tipo X).

## 5. Cálculos Requeridos
### Cálculo del Costo del Aluminio:
- Basado en la suma de los lados de cada nave.
- Los perfiles se insertan 1cm en las esquinas, que tienen 4cm de alto y ancho.

### Cálculo del Costo del Vidrio:
- Basado en el área de cada nave (ancho x alto), con un ajuste de 1.5cm menos por lado para permitir la inserción en el marco.

### Cálculo del Costo Total:
- Costo total = (Costo del aluminio + Costo del vidrio + Costo de las esquinas + Costo de la chapa).
- Aplicar descuento del 10% si la cantidad de ventanas es mayor a 100.

## 6. Descuentos
- Descuento del 10% si se compran más de 100 ventanas.

## 7. Actualizaciones y Mantenimiento
- El sistema debe permitir la actualización de precios, estilos de ventanas, y otros parámetros con facilidad.
