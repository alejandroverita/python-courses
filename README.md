# CURSO BASICO DE PYTHON

## INTRODUCCION A LA PROGRAMACION CON PYTHON

### PORQUE APRENDER DE PYTHON?

- Frontend: Se encarga de llevar el diseño de una aplicación o sitio web a código
- IoT: Se encarga de darle la capacidad de conectarse a internet a elementos que pueden estar a nuestro alrededor.
- IA: Se encarga de enseñarle a la computadora a resolver un determinado problema sin la necesidad de estar involucrados constantemente.
- Backend: Se encarga de crear la lógica con la cual va a funcionar una determinada aplicación y que va a ser almacenada en un servidor.
- DevOps: Se encarga de manejar la información almacenada en la nube de una determinada aplicación.
- Data Science: Se encarga de tomar la información relevante de un determinado ambiente y poder sacar conclusiones al respecto.
- Video juegos: Se encarga de combinar la programación, el diseño y la música para generar grandes experiencias a los usuarios.
- Desarrollo móvil: Se encarga de crear aplicaciones que serán almacenadas en la PlayStore o AppStore, y que podremos hacer uso de ellas desde nuestros smartphones.

[![Resumen](https://static.platzi.com/media/user_upload/IMG_E74D79FA33BE-1-166c16b7-5207-4648-a271-159fd8a887f8.jpg "Resumen")](https://static.platzi.com/media/user_upload/IMG_E74D79FA33BE-1-166c16b7-5207-4648-a271-159fd8a887f8.jpg "Resumen")

### Los algoritmos

[![Algoritmos](https://static.platzi.com/media/user_upload/2a73a2054d9cb530cbfe3f0ef5dbf51e-06645aaa-b621-4a07-8e1e-7c1336cb4457.jpg "Algoritmos")](https://static.platzi.com/media/user_upload/2a73a2054d9cb530cbfe3f0ef5dbf51e-06645aaa-b621-4a07-8e1e-7c1336cb4457.jpg "Algoritmos")

### Herramientas

- [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code")
- [Python](https://www.python.org/ "Python")
- [Consola](https://cmder.net/ "Consola")

### Básicos para usar la consola:

- Ctrl + L = Limpiar pantalla
- CD = Change Directory
- … = Carpeta padre
- CD… = Cambiar de directorio a la carpeta padre
- ls = list
- mkdir = Make directory
- touch = para crear archivos

## CONCEPTOS BASICOS DE PYTHON

### Operadores aritmeticos

[![Operadores python](https://static.platzi.com/media/user_upload/referencia_python-08967f82-4367-4e5c-b532-da74f02bada5.jpg "Operadores python")](https://static.platzi.com/media/user_upload/referencia_python-08967f82-4367-4e5c-b532-da74f02bada5.jpg "Operadores python")

### Que es una variable

Reglas para la creación de variables,

1. Nunca comenzar con un número.
2. Siempre poner las palabras en minúsculas
3. Separación de palabras con guión bajo.

### Los primitivos: tipos de datos sencillos

[![Tipos de datos](https://www.researchgate.net/profile/Pedro-Gomis/publication/325387232/figure/fig4/AS:630680337793025@1527377318263/Figura-8-Tipos-de-datos-El-tipo-de-dato-caracter-no-existe-en-Python-un-caracter.png "Tipos de datos")](https://www.researchgate.net/profile/Pedro-Gomis/publication/325387232/figure/fig4/AS:630680337793025@1527377318263/Figura-8-Tipos-de-datos-El-tipo-de-dato-caracter-no-existe-en-Python-un-caracter.png "Tipos de datos")

### Convertir un dato a un tipo diferente

- Input("") para pedirle al usuario que introduzca datos.

- int() con datos o variables dentro de parentesis para convertirlo en número entero.

- str() para convertir números tanto decimales como enteros a strings.

### Operadores lógicos y de comparación

**Operadores Lógicos**

- and ( y ) -> compara dos valores, y si ambos son verdaderos, devuelve True.
- or ( ó ) -> si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo devuelve falso cuando los dos valores no se complen.
- not ( no) -> invierte el valor de una variable, dando el valor contrario al de la variable evaluada.

**Operadores de Comparación**

- == ( igual qué ) -> Determina si dos valores son iguales o no.
- != (distinto de) -> Determina si dos valores son distintos o no. Si los valores son diferentes devuelve True, si son iguales devuelve False.
- (mayor que) -> Compara dos valores, y determina si es mayor que el otro.

- < (menor que) -> Compara dos valores y determina si es menor que el otro.
- = (mayor o igual) -> compara dos valores y determinas si es mayor o igual que el otro.

- <= (menor o igual) -> compara dos valores y determinas si es menor o igual que el otro.

### Trabajando con texto: cadenas de caracteres

**METODOS:**

- variable.upper() = 'todos los caracteres en MAYÚSCULAS'
- variable.capitalize() = 'solo la primera en MAYÚSCULA'
- variable.lower() = 'todos los caracteres en minúscula'
- variable.strip() = 'eliminar espacios basura del string'
- variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter

**FUNCIONES BILT IN**
Aquellas que son propias del lenguaje y que no tenemos que crearlas, solo invocarlas.

- len()
- print()
- input()

![Functions](https://static.platzi.com/media/user_upload/Build-int%20functions-e1b3d053-5c76-4ffe-b6b3-5a61e062d77c.jpg "Functions")

### Trabajando con texto: slices

Los slices, traducidos al español como “rebanadas”, nos permiten dividir los caracteres de un string de múltiples formas. A continuación, un ejemplo de estos:

    nombre = "Francisco"
    nombre
    "Francisco"
    nombre[0 : 3) //Arranca desde el primer índice hasta llegar antes del 3° índice.
    "Fra"
    nombre[:3] //Va desde el principio hasta antes de llegar del 3° índice. Cómo no hay ningún parámetro en el primer lugar, se interpreta que arranca desde el principio.
    "Fra"
    nombre[1:7] //Arranca desde el índice 1 hasta llegar antes del 7.
    "rancis"
    nombre[1:7:2] //Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2, ya que eso es lo que nos indica el 3! parámetro, el cual es 2.
    nombre[1::3] //Arranca desde el índice 1 hasta el final del string (al no haber ningún 2° parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
    "rcc"
    nombre[::-1]  //Al no haber parámetro en los 2 primeros lugares, se interpreta que se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la palabra al revés, porque es -1.
    "ocsicnarF"

### Bucles

![Bucles](https://static.platzi.com/media/user_upload/Bucles-254e8951-2dd6-40d3-b656-c8c7af03ecb4.jpg "Bucles")

### Almacenar varios valores en una variable: listas

Las listas vendrían siendo un Array

    numbers = [1, 3, 5, 7]
    oBjects = ['Holas', 3, 4.6, True]

    objects[3]

Los métodos delos array vendrían siendo:

- append() → Agrega elementos a las listas

      numbers = [1, 3, 5, 7]

      numbers.append(1)
      #numbers=[1,3,5,7,1]

- pop() → Elimina un elemento de la lista pasándole el numero de la posición de ese objeto.

      numbers = [1, 3, 5, 7]

      numbers.pop(1)
      # numbers = [1, 5, 7]

### Tuplas

Listas = dinamicas
Tuplas = estaticas
.
Ventajas?

- Iteraciones mas rapidas con tuplas que con listas
- Inmutables

### ¿Qué son los diccionarios?

Diccionarios: Son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

Operaciones:

.keys() —> Retorna la clave de nuestro elemento

.values()—> Retorna una lista de elementos (valores del diccionario)

.items() —> Devuelve lista de tuplas (primero la clave y luego el valor)

.clear() —> Elimina todos los items del diccionario

.pop(“n”) —> Elimina el elemento ingresado

### List Comprehension

### List Comprehension

![First Explanation](https://static.platzi.com/media/user_upload/List_comprehensions1-bacd6262-4bc3-40c8-8c71-3da952e30b41.jpg "First Explanation")

![Second explanation](https://static.platzi.com/media/user_upload/List_comprehensions2-665fd48c-97a6-4ddb-939f-a0afcf5b8eda.jpg "Second explanation")'

![List comprehensions](https://miro.medium.com/max/2980/1*zJ0XfN1fkWSvll2Bg8o46g.png "List comprehensions")

### Dictionary Comprehension

![Dictionaty and list comprehensions](https://static.platzi.com/media/user_upload/List_Dict_Comprehensions-478137d2-d3b8-4509-be4d-29eb0e455e8a.jpg "Dictionaty and list comprehensions")

### Funciones Lambda

Son funciones sin nombre. `lamba argumentos:expresión`

Lambda solamente puede tener 1 expresión.

    palindrome = lambda string: string == string[::-1] #Variable stores the function value

`print(palindrome('ana')) # returns True`

código de arriba es equivalente a:

    def palindrome(string):
        return string == string[::-1]

    print(palindrome('ana'))

![Lambda](https://i1.faceprep.in/Companies-1/python-lambda-functions-new.png "Lambda")

![Lambda](https://runestone.academy/runestone/books/published/fopp/_images/lambda.gif "Lambda")

### Los errores en el codigo

Los errores son parte de nuestra vida como programadores y hay que saber lidiar con ellos.

Errores:

- Syntax Error -> Errores de escritura, Python no ejecuta el programa.
- Exception -> Python se detiene en una línea en específica
- KeyboardInterrupt -> Ctrl + C
- KeyError -> Cuando tratamos de acceder a una llave que no existe
- IndexError -> Cuando tratamos de acceder a un índice que no existe
- FileNotFoundError -> Archivo que no existe
- ZeroDivisionError -> Dividir entre 0
- ImportError -> Intentamos importar un módulo que tiene un error

Estos son solo algunos ejemplos, hay más de 50 excepciones.
`“Elevar”`, quiere decir que Python crea un objeto de tipo excepción.

`Traceback` son los errores que muestran en las consolas. Lo correcto es leer desde el final hasta el principio. En el final nos dirá cuál es la excepción que ocurrió.

![Errores](https://static.platzi.com/media/user_upload/Errores-c04a8c09-8040-466b-ab54-9b257e1aa1ac.jpg "Errores")

### Debugging

![Debugging](https://static.platzi.com/media/user_upload/debugging_hero-bcf16cb6-b986-4469-94c7-a2b00a112637.jpg "Debugging")

### Manejo de excepciones

TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

![Exceptions](https://static.platzi.com/media/user_upload/python-a0d427c5-4e5b-49cd-8e69-3e3b118f37ce.jpg "Exceptions")

### Assert statements

- Es una manera poco usual de manejar los errores en python
- Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.

Su sintaxis es:

    assert <condicion>, <"mensaje">
    <código>

### Modos de Apertura

r -> Solo lectura
r+ -> Lectura y escritura
w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
a -> Añadido (agregar contenido). Crea el archivo si éste no existe
a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

Para abrir un archivo seguimos las siguiente estructura

`with open(<ruta>, <modo_apertura>) as <nombre>`

`with` Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

`open(ruta,modo_apertura): ` es una función que necesita de dos parámetros

`ruta:` es donde se encuentra nuestro archivo en nuestro equipo

`modo_de_apertura:` como vamos a abrir el archivo, los modificadores son:

- r → modo de lectura
- w → modo de escritura (sobreescribe el archivo)
- a → modo append (añade información al final del archivo)

`as <nombre>` nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer

# Curso Profesional Python

# Como funciona Python

![python works](https://static.platzi.com/media/user_upload/20210727_191553-e308f826-0f99-4c5a-96a3-a6ff3be2217b.jpg "python works")

### Cómo organizar las carpetas de tus proyectos

Un módulo es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar.

Un paquete es un conjunto de módulos. Siempre posee el archivo `__init__.py`.

Una ejemplo de organizar los archivos de 🐍Python es de la siguiente manera.

![Organize folder](https://static.platzi.com/media/user_upload/paquettes-5a4095f3-0811-4e56-8f06-296b42b2e497.jpg "Organize folder")

### ¿Qué son los tipados?

💻 Los tipados es una clasificación de los lenguajes de programación, tenemos cuatro tipos:

- Estático
- Dinámico
- Débil
- Fuerte

El tipado del lenguaje depende de cómo trata a los tipos de datos.

El tipado estático es el que levanta un error en el tiempo de compilación, ejemplo en JAVA:

    String str = "Hello" // Variable tipo String
    str = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.

El tipado dinámico levantan el error en tiempo de ejecución, ejemplo en Python:

    str = "Hello" # Variable tipo String
    str = 5 # La variable ahora es de tipo Entero, no hay error

**TIPADO FUERTE**

    x = 1
    y = "2"
    z = x + y # ERROR: no podemos hacer estas operaciones con tipos de datos distintos entre sí

El tipado débil es el que hace un cambio en un tipo de dato para poder operar con el, como lo hace JavaScript y PHP.

🐍 Python es un lenguaje de tipado 👾 Dinámico y 💪 Fuerte.

### Tipado estático en Python

[Documentación oficial del tipado estático en Python](https://docs.python.org/3/library/typing.html "Documentación oficial del tipado estático en Python")

El tipado estático nos hará evitar errores de tipado antes de que el programa se ejecute.

    a: int = 5
    print(a) # 5

    b: str = 'Hola'
    print(b) # Hola

    c: bool = True
    print(c) # True

Esta sintaxís está disponible desde la versión 3.6 de Python.

    def suma(a: int, b: int) -> int:
      return a + b

    print(suma(1,2)) # 3

.

    def suma(a: int, b: int) -> int:
      return a + b

    print(suma('1','2')) # 12 😅

Usando tipado en estructuras de datos. Desde la versión 3.6 debemos importar librerias.

    from typing import Dict, List

    positives: List[int] = [1,2,3,4,5]

    users: Dict[str, int] = {
      'argentina': 1,
      'mexico': 34,
      'colombia': 45,
    }

    countries: List[Dict[str,str]] = [
      {
    	'name': 'Argentina',
    	'people': '450000', # Cuatrocientos cincuenta mil
      },
      {
    	'name': 'México',
    	'people': '90000000', # Noventa millones
      },
      {
    	'name': 'Colombia',
    	'people': '99999999999', #novecientos noventa y nueve mil millones novecientos mil novecientos noventa y nueve
      }
    ]

.

    from typing import Tuple

    numbers: Tuple[int, float, int] = (1, 0.5, 1)

.

    from typing import Tuple, Dict, List

    CoordinatesType = List[Dict[str, Tuple[int, int]]]

    #Una variable que es de tipo CoordinatesType 🤯
    coordinates: CoordinatesType = [
      {
    	'coord1': (1,2),
    	'coord2': (3,5),
      },
      {
    	'coord1': (0,1),
    	'coord2': (2,5),
      },
    ]

Ventajas de esto: claridad del código.

### Tipado Estatico

El modulo `mypy` se complementa con el modulo typing ya que permitirá mostrar los errores de tipado débil en Python.

Para revisar si algún archivo contiene errores de tipado ejecutamos en la línea de comandos lo siguiente:

`mypy archivo.py --check-untyped-defs`
Como resultado nos mostrará si existe algún error de compatibilidad de tipos.

1. mkdir new_folder
2. git init
3. py -m venv venv
4. touch .gitignore
5. type in .gitignore file
6. Ignore the enviroment files when you push to github.

`venv`

1. avenv (alias to activate venv: .\venv\Scripts\activate)
2. pip install mypy
3. pip list (to check mypy)
4. touch palindrome-py
5. code palindrome-py
6. Make your code!!!
7. `mypy palindrome-py --check-untyped-defs`

### El scope

Es el alcance que tienen las variables.

Depende de donde declares o inicialices una variable para saber si tienes acceso. Regla de oro:

> una variable solo esta disponible dentro de la region donde fue creada

**Local Scope**
Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones

**Global Scope**
Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.

### Closures

Reglas para encontrar uno

- Tener una nested function
- La nested function debe referenciar un valor de un scope superior
- La función que envuelve la nested debe retornarla también

**La usamos cuando:**

- Tenemos una clase que tiene solo un método
- Trabajamos con decoradores
  .

      	def make_multiplier(x):

      	  def multiplier(n):
      		return x * n

      	  return multiplier

      	times10 = make_multiplier(10)
      	times4 = make_multiplier(4)

      	print(times10(3)) # => 10 * 3 = 30
      	print(times4(5)) # => 4 * 5 = 20
      	print(times10(times4(2))) # => 4 * 2 * 10 = 80

### Iteradores

Son una estructura de datos para guardar datos infinitos.

Los iterables son los objetos que podemos recorrer a través de un ciclo dicho de otra manera, son estructuras de datos divisibles en elementos que puedo recorrer en un ciclo.

Todos los iterables pueden convertirse en iteradores. De esta manera es que internamente Python los puede recorrer realmente, esto mediante parsing usando el comando iter.

    # Creando un iterador
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    # Iterando un iterador
    print(next(my_iter)) # Next nos permite acceder al siguiente elemento del iterador por cada llamada

    # Cuando no quedan datos, la excepción StopIteration es elevada

Si queremos crear un código que nos permita recorrer todos los elementos de nuestra lista usando la función next para como aparece en el ejemplo anterior, tendríamos que realizar un bloque try-except:

    # Creando un iterador
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    # Iterando un iterador
    while True:
    	try:
    		element = next(my_iter)
    		print(next(my_iter)) # Next nos permite acceder al siguiente elemento del iterador por cada llamada
    	except StopIteration:
    		break                # Salimos del ciclo una vez que obtenemos el último valor iterable

Lo anterior es posible hacerlo de una manera mucho más sencilla, mediante el ciclo `for` el cual es azúcar sintáctica pues facilita y realiza de una manera mas estética y sencilla una operación:

    my_list = [1, 2, 3, 4, 5]

    for element in my_list
    	print ("element")

Es posible crear un iterador personalizado (directamente, sin castear/casting) el cual nos permita recorrer un infinito número de elementos de acuerdo a una función dada, utiliza dos métodos internos importantes: “iter” y “next”.

El uso de una función que determina los valores a iterar nos permite ahorrar memoria y trabajar más rápido, pues no tenemos que almacenar cada uno de los valores, sino solo una función para extraer cada uno de los elementos.

El siguiente ejemplo crea un iterador que recorre todos los números pares:

    class EvenNumbers:
      """Clase que implementa un iterador de todos los números pares,
      o los números pares hasta un máximo que definimos
      """

      # Constructor
      def __init__(self, max = None): # self = objeto futuro creado con esta clase
    	self.max = max

      # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
      def __iter__(self):
    	self.num = 0            # Primer número par
    	return self

      # Método para tener la función "next" del ciclo for, es decir, recorrer cada valor.
      def __next__(self):
    	if not self.max or self.num <= self.max:
    	  result = self.num
    	  self.num += 2
    	  return result
    	else:
    	  raise StopIteration

### Generadores

Sugar syntax de los iteradores. Los generadores son funciones que guardan un estado. Es un iterador escrito de forma más simple.

    def my_gen():

      """un ejemplo de generadores"""

      print('Hello world!')
      n = 0
      yield n # es exactamente lo mismo que return pero detiene la función, cuando se vuelva a llamar a la función, seguirá desde donde se quedó

      print('Hello heaven!')
      n = 1
      yield n

      print('Hello hell!')
      n = 2
      yield n


    a = my_gen()
    print(next(a)) # Hello world!
    print(next(a)) # Hello heaven!
    print(next(a)) # Hello hell!
    print(next(a)) StopIteration

Ahora veremos un generator expression (es como list comprehension pero mucho mejor, porque podemos manejar mucha cantidad
de información sin tener problemas de rendimiento):

    #Generator expression

    my_list = [0,1,4,7,9,10]

    my_second_list = [x*2 for x in my_list] #List comprehension
    my_second_gen = (x*2 for x in my_list]) #Generator expression

### Sets

Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:

> Los sets son inmutables

Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento

> los sets guardan los elementos en desorden

Para declararlos se utilizan los {} parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}

    # set de enteros
    my_set = {1, 3, 5}
    print(my_set)

    # set de diferentes tipos de datos
    my_set = {1.0, "Hi", (1, 4, 7)}
    print(my_set)

Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar o eliminar items de los sets utilizando métodos:

- add(): nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara
- update(): nos permite agregar múltiples elementos al set
- remove(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error
- discard(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
- pop(): permite eliminar un elemento del set, pero lo hará de forma aleatoria.
- clear(): Limpia completamente el set, dejándolo vació.

  #ejemplo de operaciones sobre sets
  my_set = {1, 2, 3}
  print(my_set) #Output {1, 2, 3}

  #añadiendo un elemento al set
  my_set.add(4)
  print(my_set) #Output {1, 2, 3, 4}

  #añadiendo varios elementos al set, python ignorará elementos repetidos
  my_set.update([1, 5, 6])
  print(my_set) #Output {1, 2, 3, 4, 5, 6}

  # eliminado elementos del set

  my_set.discard(1)
  print(my_set) #Output {2, 3, 4, 5, 6}

  # borrando un elemento aleatorio

  my_set.pop()
  print(my_set) #Output el set menos un elemento aleatorio

  #limpiar el set
  my_set.clear()
  print(my_set) # Output set()

Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set:

    #usando listas para crear sets
    my_list = [1, 2, 3, 3, 4, 5]
    my_set = set(my_list)
    print(my_set)  #output {1, 2, 3, 4, 5}

    #usando tuplas para crear sets
    my_tuple: ('hola', 'hola', 1, 2)
    my_set2: set(my_tuple)
    print(my_set2) #Output {'hola', 1}
