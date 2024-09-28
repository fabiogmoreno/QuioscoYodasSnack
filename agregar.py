from validacion import solicitar_cadena,solicitar_flotante,solicitar_entero

def agregar_productos(inventario:list[list])->list[list]:
    '''
    descripcion: en la lista de inventario se le agregar una nueva lista 
                 con su respectivo el prducto , cantidad y precio y se 
                 retornara el inventario con una nueva lista o no
    argumento: recibe una lista de lista de inventario tipo list[list]
    return: retorna lista de lista de inventario
    '''   
 
    producto = solicitar_cadena('Ingrese el producto: ',20)
    cantidad_producto = solicitar_entero('Ingrese la cantidad de producto: ')
    precio_producto = solicitar_flotante('Ingrese el precion del producto: ',1,1000)


 
    lista_a_agregar = [producto,cantidad_producto,precio_producto]
 
    inventario +=  [lista_a_agregar]
 

    return inventario