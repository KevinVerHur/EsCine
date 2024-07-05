import os,csv,msvcrt
ventas=[]
entrada=5000

def inicio():
    print("<<PRESS ANY KEY>>")
    msvcrt.getch()
    os.system("cls")

def limpiar():
    os.system("cls")

def printR(texto):
    print(f"\033[31m{texto}\033[0m")

def printV(texto):
    print(f"\033[32m{texto}\033[0m")

def printM(texto):
    print(f"\033[35m{texto}\033[0m")

def menu():
    printM("══════════════════════════════")
    printM("  SISTEMA DE VENTAS CINEPLOP  ")
    printM("══════════════════════════════")
    print("1) MOSTRAR ASIENTOS DISPONIBLES")
    print("2) COMPRAR ENTRADA")
    print("3) MOSTRAR VENTAS REALIZADAS")
    print("4) GENERAR CSV DE VENTAS")
    print("0) SALIR")
    printM("══════════════════════════════")

asientos=[
    ["O","O","O","O","O"],
    ["O","O","O","O","O"],
    ["O","O","O","O","O"],
    ["O","O","O","O","O"],
    ["O","O","O","O","O"]
]
def mostrar_asientos():
    printR("        PANTALLA     ")
    printR("   ══════════════════")
    printM("   A   B   C   D   E")
    for i in range(len(asientos)):
        print(f"\033[35m{i+1}\033[0m  {asientos[i][0]}   {asientos[i][1]}   {asientos[i][2]}   {asientos[i][3]}   {asientos[i][4]}")

col=("A","B","C","D","E")
def vender_asiento(nombre,edad,telefono,fila,columna):
    if len(nombre)>=3:
        if edad>=5:
            if len(str(telefono))==9:
                fila=fila-1 #VALIDAR FILA
                if fila>=0 and fila<=(len(asientos)):
                    if columna in col: #VALIDAR COLUMNA
                        columna=col.index(columna)
                        if asientos[fila][columna]=="O":
                            total=entrada
                            if edad>=5 and edad<18:
                                total=round(entrada*0.80)
                            elif edad>65:
                                total=round(entrada*0.85)
                            ventas.append([nombre,edad,telefono,fila+1,col[columna],total])
                            asientos[fila][columna]="X"
                            printV("ASIENTO VENDIDO")
                        else:
                            printR("ASIENTO OCUPADO")
                    else:
                        printR("COLUMNA NO VALIDA")
                else:
                    printR("FILA NO VALIDA")
            else:
                printR("NUMERO DE TELEFONO NO VALIDO")
        else:
            printR("DEBE TENER 5 AÑOS O MAS")
    else:
        printR("NOMBRE NO VALIDO")

def listar():
    if len(ventas)>0:
        printM("HISTORIAL DE VENTAS")
        printM("═══════════════════")
        for i in range(len(ventas)):
            print(f"CLIENTE: {ventas[i][0]}\nEDAD: {ventas[i][1]}\nTELEFONO: +56{ventas[i][2]}\nASIENTO: {ventas[i][3]}{ventas[i][4]}\nTOTAL: ${ventas[i][5]}")
            printM("═════════════")   
    else:
        printR("NO HAY VENTAS HECHAS")

def generar_csv(nombre):
    if len(ventas)>0:
        with open(f'{nombre}.csv','w',newline='',encoding='utf-8') as a:
            escribir=csv.writer(a,delimiter=',')
            ventas.insert(0,["CLIENTE","EDAD","TELEFONO","FILA","ASIENTO","TOTAL"])
            escribir.writerows(ventas)
            ventas.pop(0)
            printV("REPORTE GENERADO CON EXITO")
    else:
        printR("NO HAY VENTAS HECHAS")
