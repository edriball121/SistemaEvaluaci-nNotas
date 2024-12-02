import csv
from colorama import Fore, Style

# Diccionario para almacenar las notas de las asignaturas
notas = {}


def solicitar_notas_basicas():
    """
    Permite ingresar notas para las asignaturas básicas: Matemáticas, Ciencia y Lenguaje.
    """
    asignaturas_basicas = ["Matemáticas", "Ciencia", "Lenguaje"]
    for asignatura in asignaturas_basicas:
        if asignatura not in notas:
            notas[asignatura] = ingresar_nota(asignatura)
    print(Fore.GREEN + "Notas básicas ingresadas correctamente." + Style.RESET_ALL)


def ingresar_nota(asignatura):
    """
    Solicita la nota para una asignatura específica.
    """
    while True:
        try:
            nota = float(input(f"Ingrese la nota para {asignatura} (0.0 - 5.0): "))
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print(Fore.RED + "Nota fuera de rango. Intenta nuevamente." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, ingresa un número." + Style.RESET_ALL)


def agregar_asignaturas():
    """
    Permite al usuario agregar nuevas asignaturas al sistema.
    """
    while True:
        nueva_asignatura = input("Ingrese el nombre de la nueva asignatura (o 'salir' para terminar): ").strip()
        if nueva_asignatura.lower() == 'salir':
            break
        if nueva_asignatura not in notas:
            notas[nueva_asignatura] = None
            print(Fore.GREEN + f"Asignatura '{nueva_asignatura}' agregada correctamente." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "La asignatura ya existe. Intenta con otro nombre." + Style.RESET_ALL)


def ingresar_notas_asignaturas_nuevas():
    """
    Permite ingresar notas para las asignaturas creadas previamente.
    """
    nuevas_asignaturas = [asignatura for asignatura, nota in notas.items() if nota is None]
    if not nuevas_asignaturas:
        print(Fore.YELLOW + "No hay nuevas asignaturas pendientes de notas." + Style.RESET_ALL)
        return
    for asignatura in nuevas_asignaturas:
        notas[asignatura] = ingresar_nota(asignatura)
    print(Fore.GREEN + "Notas de nuevas asignaturas ingresadas correctamente." + Style.RESET_ALL)


def mostrar_notas():
    """
    Muestra todas las asignaturas y sus notas en la consola.
    """
    if not notas:
        print(Fore.RED + "No hay notas registradas aún." + Style.RESET_ALL)
    else:
        print(Fore.CYAN + "\n--- Notas Registradas ---" + Style.RESET_ALL)
        for asignatura, nota in notas.items():
            estado = "Pendiente" if nota is None else f"{nota:.2f}"
            print(f"{Fore.YELLOW}{asignatura}: {estado}{Style.RESET_ALL}")

def generar_reporte_csv():
    """
    Genera un reporte en formato CSV con las asignaturas y las notas.
    """
    if not notas:
        print(Fore.RED + "No hay notas registradas aún." + Style.RESET_ALL)
    else:
        with open("reporte_notas.csv", mode="w", newline="") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(["Asignatura", "Nota"])
            for asignatura, nota in notas.items():
                escritor.writerow([asignatura, nota])
        print(Fore.MAGENTA + "Reporte generado en 'reporte_notas.csv'." + Style.RESET_ALL)


def calcular_promedio():
    """
    Calcula el promedio de todas las notas ingresadas.
    """
    notas_validas = [nota for nota in notas.values() if nota is not None]
    if not notas_validas:
        return 0.0
    return sum(notas_validas) / len(notas_validas)


def evaluar_rendimiento(promedio):
    """
    Evalúa el rendimiento del estudiante con base en el promedio.
    """
    if promedio == 0.0:
        return Fore.RED + "No hay notas ingresadas."
    elif promedio >= 4.5:
        return Fore.MAGENTA + "Excelente, aprobado con honores."
    elif 3.0 <= promedio < 4.5:
        return Fore.GREEN + "Aprobado."
    elif 2.0 <= promedio < 3.0:
        return Fore.CYAN + "En recuperación, necesitas mejorar."
    else:
        return Fore.RED + "Reprobado."


def mostrar_menu():
    """
    Muestra el menú principal y gestiona las opciones del programa.
    """
    while True:
        print(Fore.CYAN + "\n--- Menú Principal ---" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Ingresar notas de asignaturas básicas")
        print(Fore.GREEN + "2. Agregar nuevas asignaturas")
        print(Fore.GREEN + "3. Ingresar notas de asignaturas nuevas")
        print(Fore.GREEN + "4. Generar reporte en CSV")
        print(Fore.GREEN + "5. Ver promedio y evaluación")
        print(Fore.GREEN + "6. Ver notas en la consola")
        print(Fore.GREEN + "7. Salir")

        opcion = input(Fore.YELLOW + "\nSeleccione una opción: " + Style.RESET_ALL).strip()

        if opcion == "1":
            solicitar_notas_basicas()
        elif opcion == "2":
            agregar_asignaturas()
        elif opcion == "3":
            ingresar_notas_asignaturas_nuevas()
        elif opcion == "4":
            generar_reporte_csv()
        elif opcion == "5":
            promedio = calcular_promedio()
            evaluacion = evaluar_rendimiento(promedio)
            print(Fore.CYAN + "\n--- Resultados ---" + Style.RESET_ALL)
            print(f"{Fore.YELLOW}Promedio: {promedio:.2f}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}Evaluación: {evaluacion}{Style.RESET_ALL}")
        elif opcion == "6":
            mostrar_notas()
        elif opcion == "7":
            print(Fore.CYAN + "Gracias por usar el sistema. ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente." + Style.RESET_ALL)

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
