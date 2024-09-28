def mostrar_productos(inventario:list[list])->None:
    '''
    descripcion: Muestra por pantalla todos los inventario del momento
                 producto , cantidad y precio
    argumento: recibe lista de lista inventario tipo list[list]
    return : retorna None 
    '''
    print(f"{' ':>10}*{'-'*51}*")
    print(f"{' ':>10}| {'Producto':<25}  {'Cantidad':>10}  {'Precio':>10} |")
    print(f"{' ':>10}*{'-'*51}*")
    for i in range(len(inventario)):
        nombre = inventario[i][0]
        cantidad = inventario[i][1]
        precio = inventario[i][2]
        print(f"{' ':>10}| {nombre:<25}  {cantidad:>10}  {precio:>10} |")
    print(f"{' ':>10}*{'-'*51}*")