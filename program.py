from pathlib import Path

def establecer_nombre():
    """
    Establece el nombre del usuario.
    Si el nombre ya aparece en el archivo de ranking.txt pregunta si quiere sobreescribir o cambiar el nombre.
    """
    nombre = input("Escriba su nombre: ")
    archivo_ranking = Path(r'PI primer millon\ranking.txt') # Representa al archivo ranking.txt

    if nombre in archivo_ranking.read_text(): 
        respuesta = input("Ese nombre ya está tomado. Si quieres sobreescribir escribe S. Si quieres cambiar el nombre escribe N: ")

        if respuesta.upper() == 'S':
            return nombre
        elif respuesta.upper() == 'N':
            nombre = establecer_nombre()
    
    return nombre

def separar_personas(archivo):
    """Retorna un diccionario con los nombres de las personas como clave y la puntuación como valor."""
    lista_personas = archivo.split('\n')
    if lista_personas[-1] == '':
        lista_personas.pop()

    diccionario_personas = {}

    for persona in lista_personas:
        nombre, puntuacion = persona.split(": ")
        diccionario_personas[nombre] = int(puntuacion)
    
    return diccionario_personas

def ordenar_ranking(diccionario):
    """Ordena el diccionario de mayor puntuación a la menor."""
    return dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))

def guardar_archivo(archivo, diccionario):
    """Guarda el archivo en formato 'Persona: valor'"""
    nuevo_contenido = ""

    for persona, puntuacion in diccionario.items():
        nuevo_contenido += f"{persona}: {puntuacion}\n"

    archivo.write_text(nuevo_contenido)

def guardar_ranking(nombre, num_apariciones):
    """Guarda el archivo agregando una nueva persona al ranking."""
    archivo_ranking = Path(r'PI primer millon\ranking.txt')
    nuevo_ranking = archivo_ranking.read_text() + f"{nombre}: {num_apariciones}\n"
    ranking_ordenado = ordenar_ranking(separar_personas(nuevo_ranking))

    guardar_archivo(archivo_ranking, ranking_ordenado)

archivo_pi = Path(r'PI primer millon\pi.txt') # Representa al archivo ranking.txt
pi = archivo_pi.read_text() # Se lee el pi.txt que está en la misma carpeta que program.py

print("\n¿Mi fecha de nacimiento aparece en el primer millón de decimales de PI?")
nombre = establecer_nombre()

fecha = input("Escriba su fecha de nacimiento en formato ddmmaa: ")
num_apariciones = pi.count(fecha)

#Si la fecha no es un número entero o si la fecha no tiene 6 caracteres
if not fecha.isdigit() or len(fecha) != 6:
    print("Esa no es una fecha válida. Escriba la fecha en formato ddmmaa")
elif fecha in pi:
    if num_apariciones == 1:
        print(f"Felicidades! Tu fecha de nacimiento aparece {num_apariciones} vez.")
    else:
        print(f"Felicidades! Tu fecha de nacimiento aparece {num_apariciones} veces.")
    
    guardar_ranking(nombre, num_apariciones)
else:
    print("Su fecha de nacimiento no aparece.")

    guardar_ranking(nombre, num_apariciones)