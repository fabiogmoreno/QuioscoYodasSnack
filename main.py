from agregar import agregar_productos
from inventario import inventario as productos
from mostrar import mostrar_productos
import os

from vender import vender_productos

entrar = True
while entrar:
    print('''
        Quisco Yoda's Snack
        *******************
        Menu principal:
            1) Agregar producto al inventario
            2) Realizar una venta
            3) Mostrar productos disponibles
            4) Salir del sistema ''')
    
    opcion = int(input('Ingrese una onpcion correspondiente: '))
    
    if opcion == 1:
        productos = agregar_productos(productos)
    elif opcion == 2:
        productos = vender_productos(productos)
    elif opcion == 3:
        mostrar_productos(productos)
    elif opcion == 4:
        print('Esta es la opcion 4 en salir')
        entrar = False
    input('Apretar un boton para volver al menu principal')   
    os.system('cls')