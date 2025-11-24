from moduloDeFunciones import *

def PrincipalMenu():
    while True:
        print("\n========== PRINCIPAL MENU ==========\n")
        print("¿What do you want to do today? Select one of the following options:\n")

        print("1. Inventory Management")
        print("2. Sales registration and inquiry")
        print("3. Validate available stock")
        print("4. Sales history (view only)")
        print("5. Types and checks sales")
        print("6. Reporting module")
        print("7. Get out")

        process = input("Please enter the number of the activity you want to do today.: ").strip()

        if process == "1":
            modulo_inventory()   
        elif process == "2":
            modulo_sales()    
        elif process == "3":
            validateStock()
        elif process == "4":
            show_sales_history()
        elif process == "5":
            types_and_checks_sales()
        elif process == "6":
            modulo_reports()     
        elif process == "7":
            print("Getting out the program..")
            break
        else:
            print("ERROR: Invalid option. Please try again..")

# ESTA LÍNEA ES CLAVE:
PrincipalMenu()