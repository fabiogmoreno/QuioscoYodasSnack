
import os
from mostrar import mostrar_productos as mostrar_stock
 
 
def vender_productos(inventario:list[list])->list[list]:

    entrar = True
    while entrar: 


        mostrar_stock(inventario)  



        producto = input('Ingrese el producto que sea vender: ')
    
        #            nombre  cantidad   precio
        #
        se_encontro_el_producto = False

        for i in range(len(inventario)):
            if inventario[i][0].lower() == producto:
            
                se_encontro_el_producto = True

                if inventario[i][1] > 0:    
                    cantidad = int(input('La cantida que desea: '))
                    total_pagar = round(inventario[i][2] * cantidad)
            
                if  inventario[i][1] >= cantidad:
                    inventario[i][1] -= cantidad
                    print('_'*35)
                    print(f' \n Compraste {cantidad} {inventario[i][0] }. \n En total a pagar es : $ {total_pagar}')
                    print('-'*35)
                elif inventario[i][1] == 0:
                    print('Te quedaste sin stock, no podes realizar la venta')
                else:
                    print('No hay cantidad cantidad que solicita')
         
                break 

        if se_encontro_el_producto == False:
            print('El producto solicitado no existe o esta mal escrito ')

        pregunta_para_salir = input('Para continuar vendiendo apretar c(continuar) o s(para salir de este menu)')
        while pregunta_para_salir != 's' and pregunta_para_salir != 'c':
            pregunta_para_salir = input('Para continuar vendiendo apretar c(continuar) o s(para salir de este menu)')
        if pregunta_para_salir == 'c':
            input('Presione un Boton para continuar...')
            os.system('cls')
        elif pregunta_para_salir == 's':
            entrar = False
            break

    return inventario