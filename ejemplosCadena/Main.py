from xml.sax.saxutils import prepare_input_source

text1 = "Fundamentos con "
text2 = "Python"
#text = 5 (da error porque es tipo numerico, por lo tanto no se puede mezclar
result = text1 + text2
print(result)
print()

#para agregar espacios entre cadenas
name = "Julián"
lastName = "Campo"
fullName = name + " " + lastName
print(fullName)
print()

#Se utiliza (Format String) para mostrar el precio de un producto con dos decimales
price = 97
text3 = f"The price es {price:.2f} dollars"
print(text3)
print()

#Math operation (Para hacer todo en una linea
text4 = f"La multiplicacion es {20*59}"
print(text4)
print()

#para cocolocar la primera letra en mayuscula con la funcion (capitalize
text5 = "python es un lenguaje de alto nivl de programacion"
result1 = text5.capitalize()
print(result1)
print()

#La funcion casefold sirve para convertir
# todo a minuscula y es mas fuerte que lower
title = "cien Años de Soledad"
titleConvert = title.casefold()
print(titleConvert)
print()

# funcion center sirve para estblecer un centrado de la cadena
fruit = "banana"
textCenter = fruit.center(20, "-")
print(textCenter)
print()

#funcion count para contar el numero de veces que se repite un valor en la cadena
title1 = "I love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)
print()

#funcion count sirve para saber la longitud de la cadena y el

#funcion endswith sirve para saber si termina en un siggo de puntuacion
text6 = "Curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result3)
print()

#secuencia de escape expandtabs nos sirve para dar
# un espacio en entre cada caracter de la cadena
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2) # el 2 nos indica el numero de
# espacio que queremos despues de tabular
print(letterSpaces)
print()

#funcion find para encontrar la aparicion de un valor especifico
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)
print()

#funcion title para convertir la primera etra en matuscula
text8 = "welcome to my world"
result5 = text8.title()
print(result5)
print()

#funcion isalnum para comprobar si todos los caracteres con alfanumericos
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)
print()

#funcion isalpha para ver si todos los valores de la cadena estan el alfabeto
letters = "Space X"
result7 = letters.isalpha()
print(result7)
print()
