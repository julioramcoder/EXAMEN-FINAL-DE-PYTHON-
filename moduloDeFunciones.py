
# =================================== IMPORTS ==========================================#

import json #TREAMOS EL MODULO JSON DE PYTHON QUE NOS PERMITE CONVERTIR LOS DATOS DE JSON A ALGO LEGIBLE PARA PYTHON 
from datetime import datetime # ESTE MODULO NOS PERMITE TRABAJAR CON FECHAS Y HORAS NOS DEJA TRABJAR CON ESE FORMATO 

#============================== JSON (CARGAR // GUARDAR) ==================================#

#DEBEMOS CREAR UNA FUNCION PARA COMENZAR

VENTAS_FILE = "ventas.json"

def load_sales_json(): 
    
    try: #USAREMOS TRY PARA EVITAR QUE EL CODIGO SE ROMPA SI HAY ARCHIVOS 
        with open (VENTAS_FILE, "r", encoding="utf-8") as f: #AQUI YA LA SABEMOS PEDIMOS ABRIR EL ARCHIVO VENTAS JSON EN MODO LECTURA COMO UN ARCHIVO LEJIBLE PARA PYTHON 
            sales = json.load(f) #LO QUE HACEMOS ES LEER CON JSONLOAD EL CONTENDIO DEL ARCHVIO F Y GUARDARLOS EN UNA LISTA LLAMADA VENTAS 
            return sales #Y LO MOSTRAMOS 
    except FileNotFoundError: #DADO EL CASO EL ARCHIVO JSON QUE SE ESTA INTENTANTO ABRIR NO SIRVA ENTONCES SE GENERA ESTA ALARTE 
        return[]   #DEVOLVEMOS UN DICCIONARIO VACIO PARA QUE NO SE ROMPA EL CODIGO 
    
salesregistration= load_sales_json() #Aqui decimos los datos que hayas sacado de .json guardalos en mi lista de registro de ventas 
   

#AHORA VAMOS A CREAR UNA FUNCION PARA GUARDAR Y ESCIRBIR EN ARCHIVOS JSON, ASI VAMOS ACTUALIZANDO EL HISTORIAL 
def save_in_json(VENTAS_FILE, salesregistration):
    try:
        with open (VENTAS_FILE, "w", encoding="utf-8") as f:
            json.dump(salesregistration, f, indent = 4, ensure_ascii= False) # JSON.DUMP BASICAMENTE SE USA PARA CONVERTIR INFORMACION TIPO PYTHON A FORMATO LEGFIBLE EN JSON PORQUE YA ESTAMOS GUARDANDO LA INFORMACION DE NUEVO EN JSON 
            #QUE SUCEDE, ENTRE LOS PARENTECIS DEBEMOS PONER EL NOMBRE DE LA LISTA DE DONDE SACAREMOS LA INFORMACION  QUE SE VA A GAURDAR EN (F) QUE SERIA EL ARCHIVO QUE CONVERTIMOS ANTERIORMENTE PARA ESCRIBIR 
            # INDENT=4 ES PARA QUE SE VEA MAS BONITO
            #ENSURE_ASCII ES PARA QUE LOS CARACTERES ESPECIALES SE LEAN TAN CUAL SON.
    except:
        print("Error saving the json file")

# =============================== INVENTARIO ================================================#
#LIBRERIA NACIONAL 
#TITULO, AUTOR, CATEGORIA,PRECIO, CANTIDAD EN STOCK
products = [{"titleofbook":"Cien años de soledad","author":"Gabriel garcia","category":"Realismo magico","unitprice":"125","stock":54},
            {"titleofbook":"Los juegos del hambre","author":"Suzanne Collins","category":"Ciencia ficcion","unitprice":"235","stock":45},
            {"titleofbook":"Don quijote","author":"Miguel de cervantez","category":"Fantasia","unitprice":"","stock":74},
            {"titleofbook":"Orgullo y prejuicio","author":"Jane austen.","category":"Romance","unitprice":"758","stock":52},
            {"titleofbook":"El principito","author":"Antoine de Saint-Exupéry","category":"Filosofia","unitprice":"256","stock":25}
            ]

salesregistration = [] #EN ESTE ESPACIO SE GUARDA LA INFORMACION DE LAS VENTAS REGISTRADAS EN FORMA DE DICCIONARIO 

def Inventory_Managment(): #FUNCION PARA AGREGAR INFORMACION AL INVENTARIO
    
    while True: #TODOS LOS WHILE DEL CODIGO GENERAN UN BUCLE PARA PODER REALIZAR LA MISMA ACCION UNA Y OTRA VEZ HASTA EL USUARIO DECIDA PARAR
        print ("\n================ INVENTORY MANAGMENT ============\n")
        print("Now we are gonna make a good system inventory to types important dates of the national library \n")

        titleofbook = input("please type the title of book: ").lower() #CON LOS COMANDOS INPUT PEDIMOS INFORMACION RELEVANTE PARA EL CODIGO 
        author = input("please type the author of book: ").lower()
        category= input("please type the category of the book: ").lower()


        while True:
            try: # DEBIDO A QUE INFORMACION COMO PRECIO, FECHA Y CANTIDAD SON VALORES NUEMERICOS QUE TAMBIEN REEPRESENTAN INFORMACION, ES IMPERATIVO
                unitprice = float(input("please type the price of the book: ")) #EVITAR QUE LOS VALORES NO CORRESPONDAN A LOS SOLICITADO
                if unitprice <= 0: # PARA ESO USAMOS TRY QUE BASICAMENTE DICE, INTENTEMOS CONVERTIR A NUMERO LO QUE EL USURIO DIGITO 
                    print("the price nust be higher than 0")
                    continue
                break
            except: # SI NO PUEDES NO TE ROMPAS, SOLO IMPRIME UN MENSAJE
                print("that number it's not accepted, please try again")
                    
        while True: # MISMO PROCESOS PARA TODAS LAS PARTES EN QUE SE PIDEN NUMEROS COMO INFORMACION 
            try:
                stock = int(input("please type the stock: "))
                if stock <= 0:
                    print("the valor must be higher than 0")
                    continue
                break
            except:
                print("that number it's not accepted, please try again")
                    
        
        inventory = { # EN ESTA DICCIONARIO GUARDAMOS TODA LA INFORMACION QUE SE RECOPILE Y SE VA GUARDANDO EN UNA LISTA 

                "titleofbook" : titleofbook,
                "author" : author,
                "category" : category,
                "unitprice" : unitprice,
                "stock" : stock
        }
            
        products.append(inventory) # CON EL COMANDO APPEND DAMOS LA ORDEN PARA QUE SE GUARDE EN PRODUCTS
        print(f"product add in:",inventory)
            
        out = input("do you want continue type information (yes/not)").lower() #AQUI LE DAMOS LA OPCION AL USUARIO DE SALIRSE CUANDO QUIERA 
        if out == "yes":
            continue
        else:
            break
#--------------------------------------------------------------------------------------------
def show_inventory(): # CON LA FUNCION CREAMOS UN ORDEN DE MOSTRAR EL INVENTARIO SIEMPRE QUE SEA SOLICITADO 
    print("\n========== CURRENT INVENTORY ==========\n")

    if len(products) == 0: #PARA QUE NO HAYAN ERRORES SIEMPRE VALIDAMOS QUE EXISTAN VALORES DENTRO DE LA LSITA CON EL COMANDO LEN
        print("there are not products at the inventory.")
        return

    for p in products: #CON FOR LO QUE HACEMOS ES DARLE LA ORDEN A UN ITERADOR DE QUE NOS TRAIGA LA NFORMACION Y NOS LA MUESTRE USANDO PRINT
        print("----------------------------")
        print(f"Title of book: {p['titleofbook']}")
        print(f"Author: {p['author']}")
        print(f"Category: {p['category']}")
        print(f"Unitprice: {p['unitprice']}")
        print(f"Stock: {p['stock']}")
        print() # ESTO ES PARA DEJAR UN ESPACIO AL FINAL DE ESTA INFORMACION 
#-------------------------------------------------------------------------------------------
def update_products(): #CON ESTA FUCION LO QUE HACEMOS ES DAR UNA INSTRUCCION LA CUAL ES ACTUALIZAR LA INFORMACION QUE YA TENEMOS 
    print("\n========== UPDATE PRODUCTS ==========\n")

    serch_title = input("product name to be update: ").lower() #LE PREGUNTAMOS AL USARIO QUE QUIERE ACTUALIZAR, EN ESTE CASO LA INFORMACION DE LOS LIBROS 

    for p in products:
        if p["titleofbook"].lower() == serch_title: # VALIDAMOS QUE SI LO TENGAMOS EN STOCK 

            print("\nfound product:")
            print(p)

            print("\n what do you want to update?")
            print("1. Price") #ACA PREGUNTAMOS QUE QUIERE ACTUALIZAR EL USUARIO 
            print("2. Stock")
    
            option = input("select one opction: ") # CUALQUIERA OPCION LA PUEDE HACER SIN NINGUN PROBLEMA 

            if option == "1":
                new_price = float(input("New price: "))
                p["uniteprice"] = new_price

            elif option == "2":
                new_stock = int(input("New stock: "))
                p["stock"] = new_stock

            else:
                print("invalidate opcion.") # VALIDAMOS QUE ESCRIBA UNA OPCION VALIDA PARA QUE EL CODIGO NO SE ROMPA
                return

            print("\nUpdated product:")
            print(p)
            return

    print("We couldn't to found the book.") # DADO EL CASO NO HAYA INFORMACION IMPRIMAMOS UN MENSAJE
#--------------------------------------------------------------------------------------------
def delate_product(): #CREAMOS UNA FUNCION PARA BORRAR CUALQUIERA DE LOS DICCIONARIOS QUE TENGAMOS 
    print("\n========== DELATE PRODUCT ==========\n")
    search_title = input("Title of the product that do you want to delate: ").lower() # VALIDAMOS QUE ESTE LIBRO SI EXISTA Y TODA LA INFORMACION QUE TRAE

    for p in products: # CON FOR NUEVAMENTE LO ITERAMOS
        if p["titleofthebook"].lower() == search_title:
            products.remove(p) # EL LIBRO SE ENCUENTRA Y SE BORRA
            print("product delated currectly")
            return

    print("We couldn't to found the book.")
#--------------------------------------------------------------------------------------------
def modulo_inventory(): # CON LA FUNCION MODULO DE INVENTARIO BASICAMENTE RECOPILAMOS LAS FUCNIONES PARA QUE DESDE MENU SEA MAS FACIL ACCEDER
    while True:
        print("\n=========== MODULO INVENTORY===========")
        print("1. Add new book")
        print("2. Watch the inventory")
        print("3. Update product")
        print("4. Delate product")
        print("5. Come back to the principal menu")

        op = input("Select one opction: ").strip()

        if op == "1":
            Inventory_Managment()
        elif op == "2":
            show_inventory()
        elif op == "3":
            update_products()
        elif op == "4":
            delate_product()
        elif op == "5":
            break
        else:
            print("Invalidate option.")
#--------------------------------------------------------------------------------------------

# Para validar la disponibilidad del stock primero es neesario ver que producto quieres validar por ende 

def validateStock (): # ES IMPORTANTE QUE PODAMOS IDENTIFICAR SI EN EFECTO TENEMOS PRODUCTOS GUARDADOS EN NUESTRAS LISTAS 
    found = False # AQUI PARTIMOS PENSANDO QUE NO TENEMOS 
    while True:
        titleofbook = input("Please type the title of the book for which you want to check availability: ").capitalize() # SE PIDE EL NOMBRE DEL LIBRO 

        for p in products: # Y CON EL COMANDO FOR LO QUE HACEMOS ES BUSCARLO CON UN ITERADOR 
            if p["titleofbook"] == titleofbook:
                found=True #AL ENCONTRARLO ENTONCES LA CONDICION CAMBIA 
                print(f"the availability on stock is: {p['stock']}") #

            else:
                print("We sorry sir, actually we don't have stock availability") # DADO EL CASO NO SE ENCUNTRE IMPRIMIMOS UN MENSAJE 
                found = False 
                break 

        out = input("Do you want continue with this option? yes/not: ").lower() # NUEVAMENTE LE DAMOS LA FACILIDAD DE SALIR AL USUARIO CUANDO QUIERA 
            
        if out == "yes":
            continue
            
        elif out == "not":
            break
            
        else:
            print("Invalidate option, try again")     

#============================================ SALES ==================================================#
def types_and_checks_sales ():  # CON LA FUNCION LO QUE PRETENDMEOS ES LLEVAR UN CONTROL DE VENTAS Y DE INVENTARIOS 
    while True:
        print ("\n================ TYPES AND CHECKS'S SALES ============\n")
        print("Next, you will be able to manage the entry of the data required for proper sales registration and inquiry. \n")
        costumer= input("Please type the name of costumer: ")
        typeofcostumer= input("Please type the type of costumer: ") #LO QUE HACEMOS AQUI ES PEDIRLE AL CLIENTE INFORMACION COMO SU NOMBRE, EL TIPO DE CLIENTES Y EL LIBRO QUE SE LLEVARA 
        soldbook= input("Please type the sold title of book: ")
    
        while True:
            try: 
                soldquantity= int(input("Please type the sold books quatity: ")) # NECESITAMOS SABER LAS CANTIDADES DE LIBROS QUE SE LLEVARA 
                if soldquantity <= 0:
                    print("The valor must be gihher than 0") 
                    continue
                break
            except:
                print("The number it's not validate, try again") 
                    
        while True:
            try:
                solddate= input("Please type the date (dd/mm/yyyy): ") # LA FECHA EN LA QUE SE LLEVARA EL LIBRO TAMBIEN ES IMPORTANTE, PARA LOS REGISTROS Y PARA LOS INFORMES DE VENTAS 
                solddate = datetime.strptime(solddate,"%d/%m/%Y")
                solddate = solddate.strftime("%d/%m/%Y") #LO CONVERTIMOS A TEXTO PARA PODER GUARDARLO
                break  # si llego aqui es porque la fecha existe y esta bien escrita
            except:
                print("The date it's not validate, try again")

                
        while True: 
            try: 
                discount_applied= float(input("Please type the discount applied: ")) # VALIDAMOS LOS DESCUENTOS, QUE ESTEN ENTRE UN RANGO PERMITIDO Y QUE TENGA SENTIDO 
                if discount_applied < 0 or discount_applied> 100:
                    print("discount invalidate, must be into 0 and 100")
                    continue
                break
            except:
                print("That it's not a number validate, try agaian")
                    
#Actualizacion de nuestro registro de ventas y de nuestro inventario para eso debemos validar si existe inventario para esa venta
# AH0RA, LA RAZON POR LA QUE NECESITABAMOS TODA ESA INFORMACION ES PORQUE NUESTRO STOK DEBE SER ACTUALIZABLE, Y VALIDAR QUE SI TEMGAMOS EL STOCK SUFICIENTE PARA SOLVENTAR LA DEMANDA 
        for p in products:
            if p["titleofbook"] ==soldbook.lower():
                if p["stock"] >= soldquantity:
                    p["stock"] -= soldquantity #REALIZAMOS LA RESTA DE EL STOCK QUE TENIAMOS CON LO QUE SE LLEVA EL CLIENTE 
                else:
                    print("We sorry sir, actually we don't have stock availability")
                    break
                             
        registration = { # LA INFORMACION DE NUEVO, SE GUARDA EN UN DICCIONARIO QUE TERMINA EN UNA LISTA 
                
            "costumer": costumer,
            "typeofcostumer": typeofcostumer,
            "soldbook": soldbook,
            "soldquantity": soldquantity,
            "solddate":solddate,
            "discount_applied":discount_applied
            }
            
        salesregistration.append(registration) # UNA VEZ MAS CON EL COMANDP APPPEND DAMOS LA ORDEN 
        print(salesregistration)
            
        out = input("Do you want continue type information in the lista? (yes/not)").lower()
        if out == "yes":
            continue
        else:
            break
#------------------------------------------------------------------------------------------------------------------
       
def show_sales_history(): #CREAMOS UNA FUNCION LLAMADA HISTORIAL DE VENTAS
    
    sales= load_sales_json() # QUE PASA AQUI? COMO YA CON LA FUNCION CARGAR VENTAS JSON HEMOS EXTRAIDO LA INFORMACION QUE TENIA DICHO ARCHIVO LO QUE VAMOS A HACER ES 
    #EXTRAERLA Y LA VAMOS A GUARDAR EN VENTAS PARA QUE ASI SEA MAS COMODO MOVERNOS DENTRO DE LA INFORMACION.
    
    print("\n========================= SALES HISTORY ==========================\n")
    
#LO PRIMERO QUE DEBEMOS HACER ES VALIDAR QUE EL ARCHIVO TENGA INFORMACION, PORQUE SI NO TIENE, PUES NADA SE MOSTRARA, ENTONCES
    if len(sales)==0:
        print("We don't have sales registration yet")
        return

    for p in sales: 
        
        print("------------------SALES------------------")
        print(F"Costumer:{p['costumer']}")
        print(F"Type of costumer:{p['typeofcostumer']}")
        print(F"Sold book:{p['soldbook']}")
        print(F"Sold quantity:{p['soldquantity']}")
        print(F"Solddate:{p['solddate']}")
        print(F"Discount applied:{p['discount_applied']}")
        print()
        
#EN EL CASO QUE SI TENGAMOS INFORMACION DENTRO DEL ARCHIVO ENTONCES COMENZAMOS A ITERAR

#AHORA VAMOS A CREAR UNA FUNCION QUE RECOJA TODAS LAS FUNCIONES QUE NECESITAMOS PARA TRABJAR EN ESTA PARTE 

def modulo_sales (): # CON  LA FUNCION PODEMOS CREAR UN PQUEÑO MENU, PARA QUE DE NUEVO NOS PERMITA ACCEDER MAS FACIL DESDE EL DICICIONARIO PRINCIPAL  
    global salesregistration # DEJMAOS CLARIDAD DE QUE LA VARIABLE DONDE SE REGISTRAN LAS VENTAS ES GLOBAL PYTHON LO ENTENDERA Y SE PODRA USAR SIEMPRE
    salesregistration= load_sales_json()  # cargamos historial viejo en la lista real
    while True:
        print("=========== MODULO SALES ===========")
        print("1. Register a sale")
        print("2. Watch history from sales")
        print("3. Out, come back the principal menu")

        opctios = input("Select one previous opctions").strip()
        
        if opctios =="1":
            types_and_checks_sales()
            
            save_in_json(VENTAS_FILE,salesregistration)
        elif opctios == "2":
            show_sales_history()
        elif opctios== "3":
            break
        else:
            print("That it's not a number validate, try agaian")

#===================================== REPORTES =============================================#

#VAMOS A CREAR UNA FUNCION PARA VALIDAR LOS 3 PRODUCTOS MAS VENDIDOS 

def top_3_the_best_sellers ():
    #LLAMAMOS A LA FUNCION QUE ES CAPAZ DE SUMINISTRARNOS TODA LA INFORMACION DEL HISTORIAL Y ESA ES CARGAR VENTAS JSON QUIEN ES LA FUNCION QUE TRADUCE LOS ARCHIVOS JSON    
    sales = load_sales_json()
    
    
    print("\n=========================TOP 3 THE BEST SELLERS================================\n")
    
    #DEBEMOS VALIDAR QUE SI EXISTAN ARCHIVOS DENTRO DE MI LISTA DE ARCHIVO EXTRAIDO DE JSON
    if len(sales) == 0:
        print("There are currently no sales recorded; they are going bankrupt")
        return
    
    #COMO LAS ESPERANZAS DE QUE SI HAYAN VENTAS NO SE HAN PERDIDO ENTONCES, SOMOS OPTIMISTAS Y CREAMOS UN DICCIONARIO VACIO 
    totals ={}
    
    #VAMOS A COMENZAR A ITERAR TODAS LA VENTAS QUE HEMOS TENIDO, LAS VAMOS A SACAR DE CARGAR VENTAS JSON Y PARA SER MAS ESPECIFICOS SI QUEREMOS SABER CUAL PRODUCTO FUE EL QUE SE VENDIO MAS, CLARAMENTE NECESITAMOS UNICANTE EL NOMBRE DEL PRODUCTO Y LA CANTIDAD 
    for s in sales:
        products = s["soldbook"]
        quantity = s["soldquantity"]
    #CON PYTHON PASA ALGO CURIOSO Y ES QUE UNA VEZ QUE COMIENZA A ITERAR NO SE DETIENE, ME REFIERO A QUE PASARA POR TODOS LOS DICCIONARIOS BUSCANDO UN NOMBRE EN ESPECIFICO, Y SI NO LO ENCUENTRA PUEDE QUE SE VUELVA LOCO POR ENDE VAMOS A ENGAÑARLO 
    # BASICAMENTE CREAMOS UN FALSO PRODUCTO DICIENDO QUE SI 
    
        if products not in totals:
            totals[products] = 0 #ASI PYTHON CREERA QUE SIMPLEMNTE NO HAY VENTAS DE UN PRODUCTO Y NO QUE NO EXSISTE EN ESE DICCIONARIO EN ESPECIFICO 
        
        
        totals[products] += quantity #AQUI BASICAMENTE DECIMOS, HEY SI TENEMOS UN PRODUCTO X, BUSCALO EN TOTOALES Y SUMALE LA CANTIDAD DE ESA VENTA 
    #CADA VEZ QUE HACES UNA VENTA EL REGISTRO DEL VALOR QUE GAANSTE DE ESA VENTA SOLO IRA AL NOMBRE DEL PRODUCTO VENDIDO
    
    #AHORA DEBEMOS ORGANIZAR LOS VALORES QUE HEMOS FILTRADO SOLAMENTE Y SON PRODUCTO Y CANTIDAD
    organize = sorted(totals.items(), key = lambda x: x[1], reverse = True)
    #AQUI, TOTALES ES EL DICCIONARIO QUE YA TENEMOS, CUANDO LE AGG EL .ITEMS ES COMO UNA ORDEN, Y ES CONVIERTE EL DICCIONARIO EN UNA TUPLA ("PRODUCTO",VALOR)
    #SORTED DA LA ORDEN DE ORDENAR UNA LISTA, PERO NECESITA SABER COMO LA VAMOS A ORDENAR Y ES AHI CUANDO ENTRA
    #KEY = LAMBDA X: X[1]
    # AQUI X SERIA LA TUPLA, LA PAREJA DE PRODUCTO Y VALOR 
    # Y SI LO MIRAMOS MAS A FONDO X0 SERIA EL PRODUCTO Y X1 EL VALOR 
    # AHORA TODO JUNTO SIGNIFICA, ORDENA LOS TOTALES USANDO EL VALOR DEL NUMERO COMO REFERENCIA 
    # Y REVERSE = true ES SI VAMOS A ORDENARLOS POR VALORES PERO SOLO DE MAYOR A MENOR 
    
    Top3 = organize[:3] #Aqui damos la orden de tomar los 3 primeros valores 
    
    for prod, total in Top3: #AQUI BASICAMENTE DECIMOS SACA LA INFORMACION DEL TOP 3 E IMPRIMEMELO 
        print(prod, "->", total, "SOLDS UNITS")
        
    #---------------------------------------------------------------------------------------------------------------------------

def modulo_reports():# CREAMOS OTRA FUNCION CON UN PEQUEÑO MENU PARA PODER ACCEDER LAS FUNCIONES DE FORMA MAS LIMPIA Y ORDENADA 
    while True:
        print("\n=========== MODULO OF REPORTS ===========")
        print("1. Top 3 productos mas vendidos")
        print("2. Back to the principal menu")
        op = input("Select one option: ").strip()

        if op == "1":
            top_3_the_best_sellers () #LLAMAMOS A LA FUNCION DESPUES QUE EL USUARIO HAYA DECIDIDO SU OPCION 
        elif op == "2":
            break
        else:
            print("Invalidate opction.")

#================================= VALIDACION DE ENTRADAS DE USUARIOS =============================

def validate_text_input():
    """
    Esta función sirve para pedir un texto al usuario
    y asegurarse de que no esté vacío.

    Si está vacío, no deja avanzar y vuelve a preguntar.
    """
    while True:
        text = input().strip()  # quitamos espacios antes y después
        if text == "":
            print("It can't be empty. Try again.")
            # vuelve al inicio del while y pregunta otra vez
        else:
            return text # texto correcto, salimos de la función
            
#-----------------------------------------------------------------------------------------------------------------------
def validate_valid_product(soldbook):
    """
    Esta función busca un producto dentro de la lista 'productos'.

    - Si lo encuentra, devuelve el diccionario del producto.
    - Si NO lo encuentra, devuelve None.
    """
    soldbook= soldbook.lower()

    for p in products:
        if p["titleofbook"].lower() == soldbook:
            return p  #producto encontrado

    print("That book it's not in stock.")
    return None  # producto no encontrado                    

#---------------------------------------------------------------------------------------------------------------------------

