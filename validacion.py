def solicitar_entero(mensaje: str, min_rango: int, max_rango: int) -> int:
    '''
    descripcion: recibe strings mensaje para personificar a la pregunta al usuario
               y el minimo y maximo del entero para darle un rango especifico a la validacion
               que se le permite ingresar
    argumento: rebive mensaje: str, min_rango:int , max_rango:int
    return : entero:int
    '''
    while True:
        entero = input(mensaje)
        if entero.isdigit():
            if int(entero) < min_rango or int(entero) > max_rango:
                print(f"Error: el número debe estar entre {min_rango} y {max_rango}")
            else:
                return int(entero)
        else:
            print("Error: ingrese un número entero.")

def solicitar_flotante(mensaje: str, min_rango: float, max_rango: float) -> float:
    '''
    descripcion: recibe mensaje strings para personificar a la pregunta al usuario
                 el rango para validar hasta donde puede ingresar y se verificara que sea
                 numero o flotante 
    argumento: recibe mensaje:str,min_rango:float,max_rango:float
    return: retorna flotante:float
    '''
    while True:
        flotante = input(mensaje)
        if flotante.isdigit():
            #if '.' in flotante:
            numero = float(flotante)

            if numero < min_rango or numero > max_rango:
                print(f"Error: el número debe estar entre {min_rango} y {max_rango}")
            else:
                return float(flotante)
        else:
            print("Error: ingrese un número.")

def solicitar_cadena(mensaje: str, max_letras: int) -> str:
    '''
    descripcion:recibe el mensaje para personificar a la pregunta al usuario 
                y un entero para el maximo de palabra que quiero que se ingrese
                se validara que sea letras y el maximo que se le permitira 
    argumento:recibe mesnaje:str,max_letras:int
    return: retorna cadena:str
    '''
    while True:
        cadena = input(mensaje)
        if cadena.isalpha():
            if len(cadena) <= max_letras:
                return cadena
            else:
                print(f'no mas de {max_letras} caracteres')
        else:
            print("Error: ingrese solo letras")