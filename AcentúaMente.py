
import random

palabras_con_acento = [
    "árbol", "ámbar", "ámico", "ángulo", "ánimo", "ántico", "año", "aúpa", "aúllo", "aúreo",
    "bélico", "cámara", "cántaro", "débil", "dólar", "época", "índigo", "móvil", "nórdico", "órgano",
    "público", "récord", "tórax", "último", "válvula", "ágil", "béisbol", "césped", "día", "éxtasis",
    "gótico", "héroe", "íntimo", "jóven", "médico", "nácar", "óptico", "plástico", "récipe", "túnel",
    "útil", "vívido", "ángel", "bólido", "cárcel", "déficit", "épico", "gárgola", "hígado", "íntegro",
    "límite", "músculo", "náusea", "óvulo", "pócima", "rábano", "tórax", "último", "víbora", "ávido",
    "bóveda", "célebre", "dócil", "écija", "fácil", "góndola", "hábil", "índice", "júbilo", "lápiz",
    "máximo", "náufrago", "óxido", "póliza", "rémora", "túnel", "útil", "vómito", "ázoe", "búho",
    "céntimo", "dócil", "ébano", "fénix", "gárgola", "hélice", "íntegro", "júbilo", "límite", "mártir",
    "nítido", "óvalo", "plátano", "récipe", "sátiro", "témpano", "último", "vórtice", "zéjel", "árabe",
    "bóveda", "célebre", "dócil", "ébano", "fénix", "gárgola", "hélice", "íntegro", "júbilo", "límite",
    "mártir", "nítido", "óvalo", "plátano", "récipe", "sátiro", "témpano", "último", "vórtice", "zéjel",
    "ábaco", "ábrego", "ácaro", "ácido", "ácoro", "ácrata", "áfrica", "ágape", "águila", "álbum",
    "álcali", "álef", "álgido", "álgebra", "álibi", "álveo", "ámago", "ámbito", "ámico", "ámola",
    "ánade", "áncora", "ándito", "ángelus", "ánglico", "ánima", "ánsar", "ántico", "ántrax", "ápex",
    "áptero", "ápice", "árbol", "área", "árido", "árnica", "ártico", "ártico", "ártico", "ártico",
]

palabras_sin_acento = [
    "arbol", "ambar", "amico", "angulo", "animo", "antico", "ano", "aupa", "aullo", "aureo",
    "belico", "camara", "cantaro", "debil", "dolar", "epoca", "indigo", "movil", "nordico", "organo",
    "publico", "record", "torax", "ultimo", "valvula", "agil", "beisbol", "cesped", "dia", "extasis",
    "gotico", "heroe", "intimo", "joven", "medico", "nacar", "optico", "plastico", "recipe", "tunel",
    "util", "vivido", "angel", "bolido", "carcel", "deficit", "epico", "gargola", "higado", "integro",
    "limite", "musculo", "nausea", "ovulo", "pocima", "rabano", "torax", "ultimo", "vibora", "avido",
    "boveda", "celebre", "docil", "ecija", "facil", "gondola", "habil", "indice", "jubilo", "lapiz",
    "maximo", "naufrago", "oxido", "poliza", "remora", "tunel", "util", "vomito", "azoe", "buho",
    "centimo", "docil", "ebano", "fenix", "gargola", "helice", "integro", "jubilo", "limite", "martir",
    "nitido", "ovalo", "platano", "recipe", "satiro", "tempano", "ultimo", "vortice", "zejel", "arabe",
    "boveda", "celebre", "docil", "ebano", "fenix", "gargola", "helice", "integro", "jubilo", "limite",
    "martir", "nitido", "ovalo", "platano", "recipe", "satiro", "tempano", "ultimo", "vortice", "zejel",
    "abaco", "abrego", "acaro", "acido", "acoro", "acrata", "africa", "agape", "aguila", "album",
    "alcali", "alef", "algido", "algebra", "alibi", "alveo", "amago", "ambito", "amico", "amola",
    "anade", "ancora", "andito", "angelus", "anglico", "anima", "ansar", "antico", "antrax", "apex",
    "aptero", "apice", "arbol", "area", "arido", "arnica", "artico", "artico", "artico", "artico",
    ]

def generar_ejercicio():
    """
    Genera un ejercicio de acentuación al azar.
    """
    palabra_sin_acento = random.choice(palabras_sin_acento)
    return palabra_sin_acento

def corregir_palabra(palabra_sin_acento, respuesta):
    """
    Compara la respuesta del usuario con la palabra correcta acentuada y 
    devuelve True si es correcta, False si es incorrecta.
    """
    palabra_con_acento = palabras_con_acento[palabras_sin_acento.index(palabra_sin_acento)]
    return palabra_con_acento == respuesta

def ejecutar_programa():
    """
    Ejecuta el programa principal de ejercicios de acentuación.
    """
    print(r"""
     
     _                  _     __                             _       
    / \   ___ ___ _ __ | |_ _/_/_  __ _ _ __ ___   ___ _ __ | |_ ___ 
   / _ \ / __/ _ \ '_ \| __| | | |/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \
  / ___ \ (_|  __/ | | | |_| |_| | (_| | | | | | |  __/ | | | ||  __/
 /_/   \_\___\___|_| |_|\__|\__,_|\__,_|_| |_| |_|\___|_| |_|\__\___|

 (Este código ha sido creado por Erik Valdés Calva)
                                                                     

                                                                    
    """)
    print("¡Bienvenido a AcentúaMente!")
    print("Escribe la palabra con el acento correspondiente.")
    print("Para salir del programa, escribe 'salir'.")
    print("-" * 50)

    while True:
        ejercicio = generar_ejercicio()
        print("\nEjercicio:")
        print(ejercicio)

        respuesta = input("Respuesta: ")

        if respuesta.lower() == "salir":
            print("¡Gracias por utilizar AcentúaMente!")
            break

        es_correcta = corregir_palabra(ejercicio, respuesta)

        if es_correcta:
            print("¡Correcto!")
        else:
            print("Respuesta incorrecta. La palabra correcta es:", palabras_con_acento[palabras_sin_acento.index(ejercicio)])


# Ejecutar el programa
ejecutar_programa()
