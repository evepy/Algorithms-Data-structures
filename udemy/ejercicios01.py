#Ejercicios de diferentes cursos de UDEMY
#########################################################################
"""
            (01)
En un juego de rol, el personaje principal debe recolectar diferentes tipos de recursos para avanzar en la historia. 
Algunos de estos recursos son pociones y gemas. Cada poción tiene un peso de 85 g y cada gema pesa 112 g. 
Un jugador ha recolectado 15 pociones y 8 gemas. 
Escribe un programa que calcule el peso total de todos los recursos recolectados por el jugador """

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



            (02)
Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,);
 e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0. """

separado="Evelyn"
caracter=","
#replace(usa todos los caracteres de la variable, valor que reemplazará)
#1:-1 inicio,fin "slicing"
cadenaseparada=separado.replace("",caracter)[1:-1]
print("La cadena separada es:", cadenaseparada)

"""
            (03)
Calcula el puntaje promedio de un jugador en un juego. Dado el puntaje de tres partidas: 85, 92 y 78,
 encuentra el promedio de los puntajes. """

def puntaje_promedio(p1,p2,p3):
  promedio_total=(p1+p2+p3)/3
  return promedio_total

jugador1=puntaje_promedio(85,92,78)
print(jugador1)
print("=================")

# otra forma

class Jugador:
  def __init__(self, nombre, puntajes):
    self.nombre= nombre
    self.puntajes= puntajes

  def puntaje_promedio(self):
    return sum(self.puntajes) / len(self.puntajes)


#Creando instancia de jugador
jugador2= Jugador("Ahri",[84,78,15])
promedio2=jugador2.puntaje_promedio()
print(f"El puntaje promedio de {jugador2.nombre} es {promedio2}")


"""
            (04) """

class EstadisticasJugador:
    def __init__(self, nombre, stats):
        self.nombre = nombre
        self.stats = stats

    def calcular_kda(self):
        kda = (self.stats['asesinatos'] + self.stats['asistencias']) / self.stats['muertes']
        return round(kda, 2)

    def calcular_porcentaje_partidas_ganadas(self):
        porcentaje_ganadas = (self.stats['victorias'] / self.stats['partidas_jugadas']) * 100
        return round(porcentaje_ganadas, 2)

    def calcular_promedio_minions(self):
        promedio_minions = self.stats['minions_asesinados'] / self.stats['partidas_jugadas']
        return round(promedio_minions, 2)


# Crear instancia de EstadisticasJugador usando un diccionario de estadísticas
jugador1_stats = {
    'partidas_jugadas': 100,
    'asesinatos': 150,
    'muertes': 80,
    'asistencias': 100,
    'minions_asesinados': 2000,
    'victorias': 60
}

jugador1 = EstadisticasJugador("Carlos", jugador1_stats)

# Calcular el KDA
kda = jugador1.calcular_kda()

# Calcular el porcentaje de partidas ganadas
porcentaje_ganadas = jugador1.calcular_porcentaje_partidas_ganadas()

# Calcular el promedio de minions asesinados por partida
promedio_minions = jugador1.calcular_promedio_minions()

# Imprimir los resultados
print(f"Estadísticas de {jugador1.nombre} en League of Legends:")
print(f"KDA: {kda}")
print(f"Porcentaje de partidas ganadas: {porcentaje_ganadas}%")
print(f"Promedio de minions asesinados por partida: {promedio_minions}")


"""


            (05)
Dada una lista de nombres de personajes de anime, ordena la lista en orden alfabético. """
            
class Personaje:
  def __init__(self, nombres):
    self.nombres = nombres

  def lista_ordenada(self):
    nombres_f = sorted(self.nombres)
    return ", ".join(nombres_f)

lista1=Personaje(['Goku','Luffy', 'Yona', 'Lein'])
lista_o=lista1.lista_ordenada()
print(f"El orden de los personajes es{lista_o}")

"""

            (06)
 Crea una clase Jugador con atributos como nombre, puntaje y nivel. 
 Implementa métodos para actualizar el puntaje y mostrar la información del jugador. """

class Jugador:
  def __init__(self,nombre, puntaje, nivel):
    self.nombre=nombre
    self.puntaje=puntaje
    self.nivel=nivel

  def actualizar_p(self,nuevo_puntaje):
    self.puntaje=nuevo_puntaje

  def mostrar_info(self):
    print(f"Nombre: {self.nombre}")
    print(f"Puntaje: {self.puntaje}")
    print(f"Nivel: {self.nivel}")

j1=Jugador("jugadorvol","1250","110")
j1.actualizar_p(2150)
print(f"El jugador {j1.nombre}, tiene un puntaje de {j1.puntaje} con nivel {j1.nivel}")

