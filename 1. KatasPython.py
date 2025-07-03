# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(texto):
    texto = texto.replace(" ", "").lower()

    frecuencias = {} # creación de un diccionario vacío donde vamos a guardar el número de veces que aparece cada letra.
    for letra in texto: # cadena de texto sin espacios y en minúsculas.
        if letra in frecuencias:
            frecuencias[letra] += 1 # Si la letra ya está en el diccionario, significa que ya la hemos visto antes.
        else:
            frecuencias[letra] = 1 # Si la letra no está en el diccionario, la agregamos con valor inicial de 1.
    return frecuencias # devuelve el diccionario completo con la frecuencia de cada letra.

cadena = "Esto es una prueba"
resultado = frecuencias_letras(cadena)
print(resultado)

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicar(lista_numeros):
    return lista_numeros * 2

lista_numeros = [1, 2, 3, 4, 5, 6]

dobles = list(map(duplicar, lista_numeros))

print(dobles)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabra(lista, objetivo): # en la función definimos la lista de palabras y la subcadena que estamos buscando dentro de cada palabra de la lista.
    return [palabra for palabra in lista if objetivo in palabra] # queremos que nos devuelva una lista con cada palabra de lista solo si la subcadena objetivo está dentro de esa palabra.

palabras = ["parabrisas", "paracoches", "ventana", "puerta", "paracetamol"]
objetivo = "para"

resultado = buscar_palabra(palabras, objetivo) 
print(resultado)

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
# No estoy segura de haber entendido bien si el enunciado indica restar los valores entre las dos listas o encontrar los valores diferentes entre las dos listas. Por lo tanto, he decidido añadir los dos ejemplos. 

def diferencia_listas(lista1, lista2): # definimos una función que recibe dos parámetros (lista1 y lista2).
    def restar(x, y): # dentro de la función, definimos otra función que toma dos argumentos (x e y).
        return x - y # nos devuelve la resta x - y.
    return list(map(restar, lista1, lista2)) # la función map toma el primer elemento de lista1 y de lista2, aplica la función "restar" y genera el resultado. Luego lo repite de manera sucesiva para los otros elementos. 
    
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 5, 6, 7, 8]

print(diferencia_listas(lista1, lista2))

def valores_diferentes(lista1, lista2): # queremos encontrar los valores diferentes en ambas listas. 
    def comparar (x, y):
        return x if x != y else None # Si x es distinto de y, devuelve x. Si x es igual a y, no devuelve nada. 
    diferencia = list(map(comparar, lista1, lista2))
    return [x for x in diferencia if x is not None]
    
lista1 = [1, 2, 3, 4]
lista2 = [1, 5, 3, 0]

print(valores_diferentes(lista1, lista2))

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado. 

def evaluar_nota (lista_numeros, nota_aprobado=5): # definimos la función con la lista de notas y el valor de la nota_aprobado que es 5. 
    media = sum(lista_numeros)/ len(lista_numeros) # calculamos la media de los números en la lista. Dividimos la suma entre la cantidad para obtener la media. 
    estado = "aprobado" if media >= nota_aprobado else "suspenso" # Si la media es mayor o igual a 5, entonces es un "aprobado". Si no, es un "suspenso". 
    return (media, estado) # la función devuelve una tupla con dos elementos: "la media" y "el estado".

notas = [4, 6, 7, 5]
resultado = evaluar_nota(notas) # llamamos la función para aplicarla con nuestra lista de notas. El resultado se guarda en la variable "resultado".

print(resultado)
print(type(resultado))

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

numero = 5

def factorial(n):
    if n == 0: # si n es 0, devuelve 1 (porque 0! = 1).
        return 1
    else:
        print (f"El número ahora es {n}")
        return n * factorial(n-1) # para calcular el factorial de n, primero quiere calcular el factorial de n-1. Luego lo multiplica por n. 
factorial(numero)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_strings (lista_tuplas):
    lista_strings = list(map(str, lista_tuplas)) # aplicamos la función str a cada elemento de lista_tuplas.
    if all(isinstance(elemento, str) for elemento in lista_strings): # añadimos una condicional para verificar que todos los elementos de la lista_tuplas se han convertido en strings. 
        print("Todos los elementos son strings")
    else:
        print("Hay elementos que no son strings")
    return lista_strings # devolvemos la lista_strings que contiene las tuplas convertidas en strings. 

lista = [("cielo", "azul"), ("desayuno", "manzana"), ("animal", "gato")]
resultado = tuplas_strings(lista)

print(resultado)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def division_numeros():
    try: # usamos "try" porque las operaciones pueden fallar si el usuario ingresa un valor no númerico o un 0. 
        numero1 = float(input("Ingresa el primer número: ")) # muestra un mensaje y espera que el usuario ingrese algo. Intenta convertir el valor ingresado a un número decimal tipo float. 
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 / numero2 # división del número1 y número2
    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"La división fue exitosa. Resultado: {resultado}.")

division_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

def mascotas_permitidas_ES(mascota):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"] # definimos la lista de mascotas prohibidas en España. 
    return mascota not in mascotas_prohibidas # permitimos pasar solo las mascotas que no están prohibidas. 

def filtrar_mascotas(lista_mascotas):
    return list(filter(mascotas_permitidas_ES, lista_mascotas)) # filtramos los elementos de la lista_mascotas con las mascotas_permitidas_ES para quedarnos con los animales permitidos en ES. 

mascotas = ["Perro", "Gato", "Tigre", "Conejo", "Mapache", "Caballo"]
resultado = filtrar_mascotas(mascotas)

print(resultado)

def filtrar_mascotas(lista_mascotas): # añado una segunda opción usando una función lambda para que sea más óptimo. 
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)) # filter(función, iterable) recorre todos los elementos de iterable y solo mantiene aquellos para los que la función devuelve True. Se queda solo con las mascotas permitidas. 

mascotas = ["Perro", "Gato", "Tigre", "Conejo", "Mapache", "Caballo"]
resultado = filtrar_mascotas(mascotas)

print(resultado)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(lista):
    if len(lista) == 0: # significa que si la lista está vacía, queremos lanzar una excepción "ValueError" con un mensaje personalizado. 
        raise ValueError("La lista está vacía. No se puede calcular el promedio.") # "raise" detiene la función y lanza el error. 
    return sum(lista) / len(lista) # si la lista no está vacía, se calcula el promedio. 

lista_numeros = []

try:
    promedio = calcular_promedio(lista_numeros)
except ValueError as error: # cuando ocurre la excepción, este bloque captura el error y muestra el mensaje. 
    print(f"Error: {error}")
else: # este bloque solo se ejecuta si no ocurre ningún error. 
    print(f"El promedio es: {promedio}")
    
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def edad_usuario():
    try:
        edad = int(input("Introduce tu edad"))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
    except ValueError as error:
        print("Error: no es un valor numérico.")
    else:
        print(f"Edad válida: {edad}.")

edad_usuario()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabra(frase):
    palabras = frase.split() # separa la frase en palabras usando los espacios.
    return list(map(len, palabras)) # aplica len() a cada palabra con map()

frase = "Me voy pronto de vacaciones"
resultado = longitud_palabra(frase)

print(resultado)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def convertir_mayus_minus(letra):
    return (letra.upper(), letra.lower()) # nos sirve para generar pares de letras con sus dos formas (mayúscula y minúscula).

def letras_mayus_minus(cadena):
    letras_unicas = set(filter(str.isalpha, cadena)) # filtramos solo letras y eliminamos duplicados.
    return list(map(convertir_mayus_minus, letras_unicas))

texto = "El zorro rápido salta sobre el perro perezoso"
resultado = letras_mayus_minus(texto)

print(resultado)

for tupla in resultado: # mostramos el resultado tupla por tupla
    print(tupla)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def letra_inicial(lista, letra_objetivo):
    letra_objetivo = letra_objetivo.lower() # normalizamos la letra para que la comparación no distingua entre mayúsculas y minúsculas. 
    
    def empieza_por_letra(palabra):
        return palabra.lower().startswith(letra_objetivo) # convertimos la palabra a minúsculas y comprobamos que comienza con la letra_objetivo. 
    
    return list(filter(empieza_por_letra, lista)) # recorre cada palabra en la lista y aplica empieza_por_letra. Convertimos el resultado a lista. 

animales = ["Perro", "Gato", "Pez", "Paloma", "Caballo", "Pantera"]
letra = "p"

resultado = (letra_inicial(animales, letra))
print(resultado)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista)) # la función lambda toma el parámetro "lista", que es una lista de números. map() aplica una función a cada elemento de una lista. En concreto, le va a sumar 3 a cada número de nuestra lista. Tenemos otra función lambda que toma un número x y le suma 3.

lista_numeros = [1, 4, 7, 10]
resultado = sumar_tres(lista_numeros)
print(resultado)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(texto, n):
    lista_palabras = texto.split() # separamos el texto en palabras.
    
    def mas_larga_n(palabra):
        return len(palabra) > n # devuelve True si la palabra es más larga que n.
    
    return list(filter(mas_larga_n, lista_palabras)) # filtramos las palabras más largas que n y lo convertimos a lista. 

frase = "El zorro rápido salta sobre el perro perezoso"
resultado = palabras_mas_largas(frase, 4)
print(resultado)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def combinar_digitos(x, y): # toma dos números y los combina ( 5 y 7 -> 5 * 10 + 7 = 57)
    return x * 10 + y

def unir_digitos(lista_digitos):
    return reduce(combinar_digitos, lista_digitos) # reduce() aplica la función combinar_digitos repetidamente a los elementos de la lista (luego 57 * 10 + 2 = 572).

digitos = [5, 7, 2]
numero = unir_digitos(digitos)
print(numero)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

# Lista de dicionarios con datos de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Jessica", "edad": 22, "calificacion": 85},
    {"nombre": "Gloria", "edad": 21, "calificacion": 91},
    {"nombre": "Carlos", "edad": 23, "calificacion": 84},
    {"nombre": "Jorge", "edad": 20, "calificacion": 90}
]

def calificacion_estudiante(estudiante):
    return estudiante["calificacion"] >= 90 # la función verifica si un estudiante tiene un calificación mayor o igual a 90.

estudiantes_destacados = list(filter(calificacion_estudiante, estudiantes)) # filtramos los estudiantes que tienen esa calificación. 

print("Estudiantes con calificación mayor o igual a 90:")
for estudiante in estudiantes_destacados:
    print(f"{estudiante['nombre']} - Edad: {estudiante['edad']} - Calificación: {estudiante['calificacion']}")

# 19. Crea una función lambda que filtre los números impares de una lista dada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_impares = list(filter(lambda x: x % 2 != 0, numeros)) # Si el residuo de dividir entre 2 no es cero, entonces el número es impar. 

print("Números impares:", numeros_impares)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista_elementos = [10, "hola", 25, "gato", 40, "perro", 55]

def elemento_integer(elemento):
    return isinstance(elemento, int) # con esta función verificamos si el elemento en la lista es un integer.

solo_elemento_integer = list(filter(elemento_integer, lista_elementos)) 

print("Elementos enteros:", solo_elemento_integer)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3 # la expresión x ** 3 multiplica x por sí mismo tres veces. 

numero = 4
resultado = cubo(numero)
print (f"El cubo de {numero} es {resultado}.")

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

#Si aún no hemos importado la función reduce() de functools:
from functools import reduce

numeros = [2, 3, 4, 5]

def multiplicar(x, y):
    return x * y # definimos la función que mulitiplica dos números.

producto_total = reduce(multiplicar, numeros) # la función reduce() nos sirve para aplicarlo a la lista entera.

print("Producto total:", producto_total)

# 23. Concatena una lista de palabras.Usa la función reduce()

lista_palabras = ["Hoy", "es", "Viernes"]

def concatenar(x, y):
    return x + " " + y # definimos la función que concatena dos palabras con un espacio. 

frase = reduce(concatenar, lista_palabras)

print(frase)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()

numeros = [100, 20, 10, 5]

def resta(x, y):
    return x - y

diferencia_total = reduce(resta, numeros)

print("Diferencia total:", diferencia_total)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def numero_caracteres(cadena):
    return len(cadena) # la función len() devuelve la cantidad de caracteres en una cadena. 

frase = "Hoy es Viernes."
cantidad = numero_caracteres(frase)

print(f"La cadena tiene {cantidad} caracteres.")

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y # x % y devuelve el resto de dividir x entre y. 

a = 17
b = 5
resultado = resto(a, b)

print(f"El resto de dividir {a} entre {b} es {resultado}.")

# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0 # para evitar que se divida por 0.
    return sum(lista) / len(lista)

lista_numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(lista_numeros)

print(f"El promedio es: {promedio}.")

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    elementos_vistos = set() # creamos un conjunto vacío llamado elementos_vistos. Usamos esto para guardar los elementos  que ya han aparecido sin repetirlos. 
    for elemento in lista: # empezamos un bucle que recorre cada elemento de la lista uno por uno. 
        if elemento in elementos_vistos: # verificamos si el elemento ya está. Si sí, entonces es un duplicado. 
            return elemento # esto hace que la función se detenga en cuanto encuentra el primer duplicado. 
        elementos_vistos.add(elemento) # agregamos el elemento al conjunto. 
    return None # si el bucle termina y no hay ningun duplicado, la función devuelve None. 

mi_lista = [4, 7, 2, 9, 7, 5, 4]

resultado = primer_duplicado(mi_lista)

if resultado is not None:
    print(f"Primer duplicado encontrado: {resultado}.")
else:
    print("No hay duplicados en la lista.")
    
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    cadena = str(variable) # convertir la variable a cadena de texto.
    longitud = len(cadena) # calcula la cantidad de caracteres que tiene la cadena. 
    if longitud <= 4:
        return cadena # no se enmascara si tiene 4 o menos caracteres. 
    return '#' * (longitud -4) + cadena[-4:] # creamos una cadena de # con la cantidad necesaria para ocultar todos menos los últimos 4 caracteres. Con cadena[-4], usamos el indexado negativo para obtener los últimos 4 caracteres de la cadena. 

print(enmascarar_variable(123456789))

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace("", "").lower() # eliminamos los espacios y convertimos todo a minúscula para tener un texto uniforme. 
    palabra2 = palabra2.replace(" ", "").lower()
    
    letras1 = sorted(palabra1) # convertimos la cadena en una lista de letras ordenadas alfabéticamente para comparar si las dos palabras tienen exactamente las mismas letras. 
    letras2 = sorted(palabra2)
    
    return letras1 == letras2 # Si las listas son idénticas, significa que las palabras son anagramas. 

print(anagramas("Roma", "Amor"))
print(anagramas("Hola", "Hello"))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    try:
        entrada = input("Ingresa una lista de nombres, separados por comas: ")
        lista_nombres = [nombre.strip().lower() for nombre in entrada.split(",")] # convertimos la entrada en una lista, quitando espacios extra
        nombre_buscar = input("Ingresa el nombre que deseas buscar: ").strip().lower()
        
        if nombre_buscar in lista_nombres:
            print(f"✅ El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else: 
            raise ValueError(f"❌ El nombre '{nombre_buscar}' no se encuentra en la lista.")
    except ValueError as error:
        print("Error:", error)
        
buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def obtener_puesto(nombre_completo, empleados):
    for empleado in empleados: # recorremos uno a uno todos los elementos de la lista empleados.
        if empleado['nombre'].lower() == nombre_completo.lower(): # aquí comparamos el nombre del empleado actual con el nombre_completo que estamos buscando. Convertimos ambos nombres a minúsculas. 
            return f"{empleado['nombre']} trabaja como {empleado['puesto']}." # Si la condición se cumple, la función devuelve una cadena con el nombre y el puesto del empleado. 
    return f"{nombre_completo} no trabaja aquí." # Si no encontramos coincidencia, el return nos indica que el empleado no trabaja aquí. 

lista_empleados = [
    {'nombre': 'Ana Pérez', 'puesto': 'Gerente de Ventas'},
    {'nombre': 'Luis Gómez', 'puesto': 'Desarrollador Backend'},
    {'nombre': 'Marta Rodríguez', 'puesto': 'Diseñadora Gráfica'}
]

print(obtener_puesto('Luis Gómez', lista_empleados))
print(obtener_puesto('Carlos Torres', lista_empleados))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = sumar_listas(lista1, lista2)
print(resultado)

''' 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.

Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.

Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
'''

class Arbol:
    def __init__(self):
        self.tronco = 1 # el tronco tiene un valor inicial de 1. Empezamos con una longitud de 1 unidad.
        self.ramas = [] # asignamos al atributo ramas una lista vacía []. El árbol comienza sin ramas. 
    
    def crecer_tronco(self):
        self.tronco += 1 # abreviacón en Python para decir self.tronco = self.tronco + 1.
    
    def nueva_rama(self):
        self.ramas.append(1) # añadimos una nueva rama a la lista de ramas. 
    
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas] # recorremos cada elemento de la lista self.ramas y le sumamos 1 a los valores actuales. Se reemplaza la lista original por la nueva lista con las longitudes actualizadas. 
    
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas): # nos aseguramos que la posición que se quiere eliminar no es negativa. Verificamos que la posición existe dentro de la lista. Si ambas condiciones se cumplen, se puede eliminar la rama. 
            del self.ramas[posicion] # elimina la rama ubicada en la posición indicada. 
        else:
            print("Posición inválida. No se puede quitar la rama.")
    
    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
# 1.Crear un árbol
mi_arbol = Arbol()

# 2.Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# 3.Añadir una nueva rama al árbol
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = mi_arbol.info_arbol()
print(info)

''' 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.

Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
'''

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, cantidad): # cantidad es el monto de dinero que el usuario quiere retirar. 
        if cantidad <= 0: # tenemos que verificar que la cantidad a retirar es mayor que cero. 
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > self.saldo: # revisamos si el usuario tiene suficiente dinero para retirar esa cantidad. 
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad # restamos el valor de cantidad al valor actual de self.saldo
    
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > otro_usuario.saldo: # verificamos si el usuarion que envia dinero tiene suficiente saldo. 
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        otro_usuario.saldo -= cantidad # descontamos dinero al usuario que envía la transferencia. 
        self.saldo += cantidad # el usuario actual recibe el dinero. Se le suma esa cantidad a su saldo.
    
    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que 0.")
        self.saldo += cantidad
        
    def __str__(self):
        return f"{self.nombre}: Saldo = {self.saldo}, Cuenta corriente = {self.cuenta_corriente}"
    
alicia = UsuarioBanco("Alicia", 100, True)
roberto = UsuarioBanco("Roberto", 50, True)

roberto.agregar_dinero(20)
try:
    alicia.transferir_dinero(roberto, 80)
except ValueError as e:
    print("Error en la transferencia:", e)
try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print("Error al retirar dinero:", e)

print(alicia)
print(roberto)

''' 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto.

Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
'''

def contar_palabras(texto):
    palabras = texto.split() # dividimos el texto en palabras para poder contarlo
    contador = {} # usamos un diccionario para contar las repeticiones de cada palabra. 
    for palabra in palabras:
        palabra_limpia = palabra.strip(".,;:!?()").lower() # limpiamos los signos de puntuación y convertimos todo a minúsculas. 
        if palabra_limpia in contador: # verificamos si la palabra ya está en el diccionario contador. 
            contador[palabra_limpia] += 1 # Si ya está, aumenta su cuenta en 1. 
        else:
            contador[palabra_limpia] = 1 # Si no está, la agrega al diccionario con valor 1. 
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva): # reemplazamos todas las apariciones de una palabra por otra. 
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split() # dividimos el texto en palabras. 
    resultado = [p for p in palabras if p != palabra_a_eliminar] # recorremos cada palabra p en la lista palabras. Solo incluye p en la nueva lista si no es igual a palabra_eliminar.
    return ' '.join(resultado) # unimos las palabras de nuevo con .join()

def procesar_texto(texto, opcion, *args): # tenemos una función principal que toma texto, una opción ("contar", "reemplazar" o "eliminar") y luego ejecuta la función correspondiente dependiendo de esa opción.
    if opcion == "contar": # Si el usuario elige "contar", se llama directamente a la función "contar_palabras(texto).
        return contar_palabras(texto)
    elif opcion == "reemplazar": # Si el usuario elige esta opción, se esperan dos argumentos adicionales (palabra_original, palabra_nueva). Si no se pasan exactamente 2, lanza un error con raise ValueError(...).
        if len(args) != 2:
            raise ValueError("Se requiern dos argumentos: palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1]) # Si están bien, llama a reemplazar_palabras(texto, palabra_original, palabra_nueva) usando args[0] y args[1].
    elif opcion == "eliminar":
        if len(args) != 1: 
            raise ValueError("Se requiere un argumento: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")
    
texto = "Hoy es martes y hace mucho calor."

resultado1 = procesar_texto(texto, "contar")
print("Contar palabras:", resultado1)

resultado2 = procesar_texto(texto, "reemplazar", "martes", "miércoles")
print("Reemplazo:", resultado2)

resultado3 = procesar_texto(texto, "eliminar", "Hoy")
print("Eliminado:", resultado3)

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def clasificar_momento_dia(hora):
    if 6 <= hora < 12: # Si la hora está entre 6 (incluido) y 12 (no incluido), es de mañana.
        return "Es de día (mañana)"
    elif 12 <= hora < 18: # Si la hora está entre 12 (incluido) y 18 (no incluido), es tarde.
        return "Es de tarde"
    elif 18 <= hora <= 23 or 0 <= hora < 6: # Si la hora está entre 18 (inluido) a 23:59 o entre 00:00 a 5:59. 
        return "Es de noche"
    else:
        return "Hora no válida. Debe estar entre 0 y 23."

try:
    hora = int(input("Introduce la hora (entre 0 y 23): "))
    mensaje = clasificar_momento_dia(hora)
    print(mensaje)
except ValueError:
    print("Error: Por favor, introduce un número entero válido entre 0 y 23.")
    
''' 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
'''

def clasificar_calificacion(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación no válida. Debe estar entre 0 y 100."
    
try:
    entrada = input("Introduce la calificación del alumno (0 a 100): ")
    nota = float(entrada) # aceptamos también valors como 75.5 al convertirlo a float. 
    resultado = clasificar_calificacion(nota)
    print(f"Clasificación en texto: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido entre 0 y 100.")

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math # importamos el módulo math

def calcular_area(figura, datos):
    figura = figura.lower() # permite que el usuario pueda escribir en mayúsculas y minúsculas.
    
    if figura == "rectangulo":
        if len(datos) != 2: # verificamos que datos tenga exactamente 2 elementos: base y altura. 
            return "Error: El réctangulo necesita base y altura."
        base, altura = datos
        return base * altura
    
    elif figura == "circulo":
        if len(datos) != 1: # esperamos solo un dato, el radio. 
            return "Error: El círculo necesita solo el radio."
        radio = datos[0]
        return math.pi * radio**2 # usamos math.pi para obtener el valor de π.
    
    elif figura == "triangulo":
        if len(datos) != 2:
            return "Error: El triángulo necesita base y altura."
        base, altura = datos
        return (base * altura) / 2
    
    else:
        return "Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'."
    
print(calcular_area("rectangulo",(10, 5)))
print(calcular_area("circulo", (3,)))
print(calcular_area("triangulo", (6, 4)))
print(calcular_area("cuadrado", (5,)))
print(calcular_area("circulo", ()))

''' 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.
'''

precio_original = float(input("Ingresa el precio original del artículo (Euros): ")) # convertimos la entrada del usuario (texto) a un número decimal.

tiene_cupon = input("¿Tienes un cupón de descuento? (sí o no): ").strip().lower() # eliminamos espacios en blanco al principio y al final. Convertimos el texto a minúsculas. 

if tiene_cupon == "sí" or tiene_cupon == "si": # aceptamos tanto sí como si. 
    valor_cupon = float(input("Ingresa el valor del cupón (Euros): "))
    if valor_cupon > 0:
        precio_final = precio_original - valor_cupon
        if precio_final < 0:
            precio_final = 0 # para evitar precios negativos.
        print(f"Se ha aplicado un descuento de {valor_cupon} Euros. El precio final es: {precio_final:.2f} Euros") # :.2f muestra el precio con dos decimales.
    else:
        print("El valor del cupón no es válido. Ne se aplicará descuento.")
        print(f"El precio final es: {precio_original:.2f} Euros")
else:
    print(f"No se ha aplicado ningún descuento. El precio final es: {precio_original:.2f} Euros")