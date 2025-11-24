from moduloDeFunciones import *

def menu_principal():
    while True:
        print("\n========== MENU PRINCIPAL ==========\n")
        print("¿Que quieres hacer hoy?, selecciona una las siguientes opciones:\n")

        print("1. Gestion del inventario")
        print("2. Registro y consulta de ventas")
        print("3. Validar stock disponible")
        print("4. Historial de ventas (solo ver)")
        print("5. Types and checks sales")
        print("6. Modulo de reportes")
        print("7. Salir")

        procesos = input("Por favor ingresa el numero de la actividad que quieres hacer hoy: ").strip()

        if procesos == "1":
            modulo_inventory()   
        elif procesos == "2":
            modulo_sales()    
        elif procesos == "3":
            validateStock()
        elif procesos == "4":
            show_sales_history()
        elif procesos == "5":
            types_and_checks_sales()
        elif procesos == "6":
            modulo_reports()     
        elif procesos == "7":
            print("Saliendo del programa...")
            break
        else:
            print("ERROR: opción invalida. Intenta otra vez.")

# ESTA LÍNEA ES CLAVE:
menu_principal()