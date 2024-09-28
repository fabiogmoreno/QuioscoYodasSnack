
from code import interact
import os
from mostrar import mostrar_productos as mostrar_stock
from validacion import solicitar_cadena as string,solicitar_entero as integer
 
 
def vender_productos(inventario:list[list])->list[list]:
    '''
    descripcion:recibe el inventario por parametro 
                se utilizara mostrar en tiempo real por pantalla mientra que se le preguntara
                al usuario que desea vender de lo que esta disponible y si esta disponible se vendera
                entonce con la lista de inventario la cantidad disponible y se modificara descontado la cantidad
                , se preguntara si se desea seguir vendiendo hasta que diga que no y se retornara la lista
                inventario modificada o no
    argumento:recibe inventario:list[list] lista de lista
    return: retorna inventario:list[list]
    '''

    entrar = True
    while entrar: 


        mostrar_stock(inventario)  



        producto = input('Ingrese el producto que sea vender: ')
    
         
        se_encontro_el_producto = False

        for i in range(len(inventario)):
            if inventario[i][0].lower() == producto:
            
                se_encontro_el_producto = True

                if inventario[i][1] > 0:    
                    cantidad = integer('Ingrese la cantidad vas a vender: ',1,100)
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

        pregunta_para_salir = string('Para continuar vendiendo apretar c(continuar) o s(para salir de este menu)',1)
        while pregunta_para_salir != 's' and pregunta_para_salir != 'c':
            pregunta_para_salir = string('Para continuar vendiendo apretar c(continuar) o s(para salir de este menu)',1)
        if pregunta_para_salir == 'c':
            input('Presione un Boton para continuar...')
            os.system('cls')
        elif pregunta_para_salir == 's':
            entrar = False
            break

    return inventario