from funciones import inicio,limpiar,menu,printM,printR,mostrar_asientos,vender_asiento,listar,generar_csv
inicio()
while True:
    menu()
    seleccion=input("SELECCIONE: ")
    if seleccion=="0":
        limpiar()
        printM("CHAO KMT")
        break
    elif seleccion=="1":
        limpiar()
        printM("MOSTRAR ASIENTOS DISPONIBLES")
        printM("════════════════════════════")
        mostrar_asientos()
    elif seleccion=="2":
        limpiar()
        printM("     VENDER ASIENTO")
        printM("     ══════════════")
        mostrar_asientos()
        nombre=input("INGRESE SU NOMBRE: ").upper()
        edad=int(input("INGRESE SU EDAD: "))
        telefono=int(input("INGRESE NUMERO DE TELEFONO: "))
        fila=int(input("INGRESE FILA: "))
        columna=input("INGRESE COLUMNA: ").upper()
        vender_asiento(nombre,edad,telefono,fila,columna)
    elif seleccion=="3":
        limpiar()
        printM("LISTAR VENTAS")
        printM("═════════════")
        listar()
    elif seleccion=="4":
        limpiar()
        printM("GENERAR CSV")
        printM("═══════════")
        nombre=input("INGRESE NOMBRE PARA EL ARCHIVO CSV: ").upper()
        generar_csv(nombre)
    else:
        printR("OPCION NO VALIDA")
    