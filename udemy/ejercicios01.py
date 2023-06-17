#Ejercicios de diferentes cursos de UDEMY
#########################################################################
"""
            (01)
En un juego de rol, el personaje principal debe recolectar diferentes tipos de recursos para avanzar en la historia. 
Algunos de estos recursos son pociones y gemas. Cada poción tiene un peso de 85 g y cada gema pesa 112 g. 
Un jugador ha recolectado 15 pociones y 8 gemas. 
Escribe un programa que calcule el peso total de todos los recursos recolectados por el jugador
""
def calcular_peso_total(cantidad_pocion,cantidad_gema):
    peso_pocion=85
    peso_gema=112

    peso_total=((cantidad_pocion*peso_pocion)+(cantidad_gema*peso_gema))

    return peso_total

#ejemplo de uso
cantidad_pocion=15
cantidad_gema=8
resultado = calcular_peso_total(cantidad_pocion, cantidad_gema)
print("El peso total de los recursos recolectados es:", resultado, "g")  

"""


"""
            (02)
Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,);
 e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0. 

separado="Evelyn"
caracter=","
#replace(usa todos los caracteres de la variable, valor que reemplazará)
#1:-1 inicio,fin "slicing"
cadenaseparada=separado.replace("",caracter)[1:-1]
print("La cadena separada es:", cadenaseparada)

"""

"""
            (03)


"""