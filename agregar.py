def agregar_productos(inventario:list[list])->list[list]:
    '''
    descripcion: en la lista de inventario se le agregar una nueva lista 
                 con su respectivo el prducto , cantidad y precio y se 
                 retornara el inventario con una nueva lista o no
    argumento: recibe una lista de lista de inventario
    return: retorna lista de lista de inventario
    '''   
 
    producto = input('Ingrese el producto: ')
    cantidad_producto = int(input('Ingrese la cantidad de producto: '))
    precio_producto = float(input('Ingrese el precion del producto: '))


 
    lista_a_agregar = [producto,cantidad_producto,precio_producto]
 
    inventario +=  [lista_a_agregar]
 

    return inventario