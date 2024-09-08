from rich.console import Console
from rich.table import Table
from models.ventana import Ventana
from models.estilo_ventana import EstiloVentana
from models.nave import Nave
from models.vidrio import Vidrio
from models.acabado_aluminio import AcabadoAluminio
from models.cotizacion import Cotizacion
from models.componente_adicional import ComponenteAdicional

# Crear una instancia de Console para Rich
console = Console()

def solicitar_datos_usuario():
    """Solicita datos al usuario para crear una ventana y cotización"""
    
    # Solicitar estilo de ventana
    estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ").strip().upper()
    if estilo not in ["O", "XO", "OXXO", "OXO"]:
        console.print("[red]Estilo inválido. Debe ser O, XO, OXXO o OXO.[/red]")
        return None

    # Solicitar dimensiones de la ventana
    while True:
        try:
            ancho = float(input("Ingrese el ancho de la ventana en cm: "))
            alto = float(input("Ingrese el alto de la ventana en cm: "))
            if ancho <= 0 or alto <= 0:
                console.print("[red]Las dimensiones deben ser números positivos.[/red]")
                continue
            break
        except ValueError:
            console.print("[red]Entrada inválida. Debe ingresar un número.[/red]")

    # Solicitar tipo de acabado del aluminio
    print("Seleccione el tipo de acabado del aluminio:")
    print("1. Pulido")
    print("2. Lacado Brillante")
    print("3. Lacado Mate")
    print("4. Anodizado")
    
    while True:
        try:
            opcion_acabado = int(input("Ingrese el número correspondiente al tipo de acabado: "))
            if opcion_acabado not in [1, 2, 3, 4]:
                console.print("[red]Opción inválida. Debe ingresar un número entre 1 y 4.[/red]")
                continue
            # Mapear opción numérica a tipo de acabado
            tipos_acabado = {
                1: "Pulido",
                2: "Lacado Brillante",
                3: "Lacado Mate",
                4: "Anodizado"
            }
            tipo_acabado = tipos_acabado[opcion_acabado]
            break
        except ValueError:
            console.print("[red]Entrada inválida. Debe ingresar un número entero.[/red]")

    acabado = AcabadoAluminio(tipo=tipo_acabado)
    
    
    # Solicitar tipo de vidrio
    print("Seleccione el tipo de vidrio:")
    print("1. Transparente")
    print("2. Bronce")
    print("3. Azul")
    
    while True:
        try:
            opcion_vidrio = int(input("Ingrese el número correspondiente al tipo de vidrio: "))
            if opcion_vidrio not in [1, 2, 3]:
                console.print("[red]Opción inválida. Debe ingresar un número entre 1 y 3.[/red]")
                continue
            # Mapear opción numérica a tipo de vidrio
            tipos_vidrio = {
                1: "Transparente",
                2: "Bronce",
                3: "Azul"
            }
            tipo_vidrio = tipos_vidrio[opcion_vidrio]
            break
        except ValueError:
            console.print("[red]Entrada inválida. Debe ingresar un número entero.[/red]")

# Solicitar opción de esmerilado
    while True:
        try:
            esmerilado_input = int(input("¿Desea vidrio esmerilado? (0 = No, 1 = Sí): "))
            if esmerilado_input not in [0, 1]:
                console.print("[red]Opción inválida. Debe ingresar 0 para No o 1 para Sí.[/red]")
                continue
            esmerilado = esmerilado_input == 1
            break
        except ValueError:
            console.print("[red]Entrada inválida. Debe ingresar un número entero.[/red]")

    
    vidrio = Vidrio(tipo=tipo_vidrio, esmerilado=esmerilado)

    # Crear naves basadas en el estilo
    naves = []
    if estilo == "O":
        nave = Nave(tipo="O", ancho=ancho, alto=alto, vidrio=vidrio, acabado=acabado)
        naves.append(nave)
    elif estilo == "XO":
        nave_fija = Nave(tipo="O", ancho=ancho/2, alto=alto, vidrio=vidrio, acabado=acabado)
        nave_deslizante = Nave(tipo="X", ancho=ancho/2, alto=alto, vidrio=vidrio, acabado=acabado)
        naves.extend([nave_fija, nave_deslizante])
    elif estilo == "OXXO":
        nave_fija1 = Nave(tipo="O", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        nave_deslizante1 = Nave(tipo="X", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        nave_deslizante2 = Nave(tipo="X", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        nave_fija2 = Nave(tipo="O", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        naves.extend([nave_fija1, nave_deslizante1, nave_deslizante2, nave_fija2])
    elif estilo == "OXO":
        nave_fija = Nave(tipo="O", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        nave_deslizante1 = Nave(tipo="X", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        nave_deslizante2 = Nave(tipo="X", ancho=ancho/3, alto=alto, vidrio=vidrio, acabado=acabado)
        naves.extend([nave_fija, nave_deslizante1, nave_deslizante2])

    estilo_ventana = EstiloVentana(nombre=estilo, naves=naves)
    ventana = Ventana(ancho=ancho, alto=alto, estilo=estilo_ventana)

    # Solicitar componentes adicionales
    esquina = ComponenteAdicional(nombre="Esquina", precio_unitario=4310)
    chapa = ComponenteAdicional(nombre="Chapa", precio_unitario=16200)

    cantidad_ventanas = int(input("Ingrese la cantidad de ventanas: "))
    cotizacion = Cotizacion(ventanas=[ventana]*cantidad_ventanas, descuento=0.1 if cantidad_ventanas > 100 else 0)

    return cotizacion

def mostrar_resumen_cotizacion(cotizacion):
    """Muestra un resumen detallado de la cotización usando Rich"""
    resumen = cotizacion.generar_resumen()

    # Crear una tabla con Rich
    table = Table(title="Resumen de Cotización")

    table.add_column("Descripción", justify="left", style="cyan", no_wrap=True)
    table.add_column("Valor", justify="right", style="magenta")

    # Agregar filas con los datos del resumen
    table.add_row("Cantidad de Ventanas", str(resumen["cantidad_ventanas"]))
    table.add_row("Total sin Descuento", f"${resumen['total_sin_descuento']:.2f}")
    table.add_row("Total con Descuento", f"${resumen['total_con_descuento']:.2f}")

    # Imprimir la tabla
    console.print(table)

def main():
    console.print("[bold green]Sistema de Cotización de Ventanas para PQR[/bold green]\n")

    # Solicitar datos al usuario
    cotizacion = solicitar_datos_usuario()
    if cotizacion is None:
        return

    # Mostrar el costo de una ventana individual
    ventana = cotizacion.ventanas[0]
    costo_ventana = ventana.calcular_costo()
    console.print(f"[bold yellow]El costo total de una ventana es:[/bold yellow] ${costo_ventana:.2f}\n")

    # Mostrar el resumen de la cotización
    mostrar_resumen_cotizacion(cotizacion)

if __name__ == "__main__":
    main()
