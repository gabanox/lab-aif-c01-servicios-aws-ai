"""
=============================================================================
Ejercicio 2: Amazon Comprehend - Entidades y PII (Python boto3)
Nivel: GUIADO
Duracion: ~20 minutos
=============================================================================

En este ejercicio vas a usar Python con boto3 para detectar entidades
nombradas (personas, organizaciones, lugares) y datos personales (PII)
en articulos de noticias.

Relacion con AIF-C01:
  - Task 1.2: Servicios de NLP de AWS
  - Comprehend detecta PII como parte de sus capacidades de proteccion de datos
  - Concepto clave: entidades vs PII (entidades son informativas, PII es sensible)

Instrucciones:
  1. Completa las secciones marcadas con # TODO
  2. Ejecuta con: python3 ejercicios/ex02_comprehend_entities.py
  3. Cada TODO tiene una pista en el comentario
=============================================================================
"""

import boto3
import json

# Crear cliente de Comprehend
# Pista: boto3.client('nombre_del_servicio', region_name='region')
comprehend = boto3.client('comprehend', region_name='us-east-1')

# Cargar las noticias desde el archivo JSON
with open('data/noticias.json', 'r', encoding='utf-8') as f:
    noticias = json.load(f)

print("=" * 60)
print(" Ejercicio 2: Comprehend - Entidades y PII")
print("=" * 60)
print()


# ---------------------------------------------------------------------------
# TAREA 1: Detectar entidades nombradas en un articulo
# ---------------------------------------------------------------------------
# Las entidades nombradas son: PERSON, ORGANIZATION, LOCATION, DATE, QUANTITY, etc.
#
# Documentacion: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_entities.html

def detectar_entidades(texto, idioma='es'):
    """
    Detecta entidades nombradas en un texto usando Amazon Comprehend.

    Args:
        texto: El texto a analizar
        idioma: Codigo de idioma (default: 'es' para espanol)

    Returns:
        Lista de entidades detectadas
    """
    # TODO: Completa la llamada a la API de Comprehend
    # Pista: El metodo se llama detect_entities()
    # Pista: Necesita dos parametros: Text y LanguageCode
    respuesta = comprehend.detect_entities(
        Text=___,
        LanguageCode=___
    )
    return respuesta['Entities']


print("--- Tarea 1: Entidades en la primera noticia ---")
print(f"Articulo: {noticias[0]['titulo']}")
print()

entidades = detectar_entidades(noticias[0]['texto'])

# Mostrar las entidades encontradas agrupadas por tipo
tipos = {}
for entidad in entidades:
    tipo = entidad['Type']
    if tipo not in tipos:
        tipos[tipo] = []
    tipos[tipo].append(entidad['Text'])

for tipo, valores in tipos.items():
    print(f"  {tipo}:")
    for valor in valores:
        print(f"    - {valor}")
print()


# ---------------------------------------------------------------------------
# TAREA 2: Detectar datos personales (PII) en articulos
# ---------------------------------------------------------------------------
# PII = Personally Identifiable Information (datos que identifican a una persona)
# Ejemplos: nombres, emails, telefonos, direcciones, numeros de identificacion
#
# Pista: Algunas noticias contienen PII intencional (emails, telefonos)
# Pista: El metodo es detect_pii_entities()

def detectar_pii(texto, idioma='es'):
    """
    Detecta datos personales (PII) en un texto.

    Args:
        texto: El texto a analizar
        idioma: Codigo de idioma

    Returns:
        Lista de entidades PII encontradas con su tipo y ubicacion
    """
    # TODO: Completa la llamada a detect_pii_entities
    # Pista: Los parametros son iguales que detect_entities (Text, LanguageCode)
    respuesta = comprehend.detect_pii_entities(
        Text=___,
        LanguageCode=___
    )
    return respuesta['Entities']


print("--- Tarea 2: Deteccion de PII ---")
print()

# Analizar la noticia 3 (deportes) y la noticia 4 (economia) -- tienen PII
for idx in [2, 3]:  # indices 0-based para noticias 3 y 4
    noticia = noticias[idx]
    print(f"Articulo: {noticia['titulo']}")

    pii_encontrado = detectar_pii(noticia['texto'])

    if pii_encontrado:
        print(f"  PII detectado: {len(pii_encontrado)} elemento(s)")
        for pii in pii_encontrado:
            # TODO: Extrae el texto del PII usando la posicion (BeginOffset, EndOffset)
            # Pista: texto_pii = noticia['texto'][pii['BeginOffset']:pii['EndOffset']]
            texto_pii = noticia['texto'][pii[___]:pii[___]]
            print(f"    - Tipo: {pii['Type']}, Texto: {texto_pii}, Confianza: {pii['Score']:.2%}")
    else:
        print("  No se detecto PII")
    print()


# ---------------------------------------------------------------------------
# TAREA 3: Resumen de entidades en TODAS las noticias
# ---------------------------------------------------------------------------
# Procesa las 5 noticias y construye un diccionario resumen.
#
# Formato esperado del resultado:
# {
#   "noticia_1": { "titulo": "...", "entidades": 12, "tipos": ["PERSON", "ORG", ...] },
#   "noticia_2": { ... },
#   ...
# }

print("--- Tarea 3: Resumen de todas las noticias ---")
print()

resumen = {}

# TODO: Completa el loop para procesar todas las noticias
# Pista: Usa enumerate() para obtener el indice
# Pista: Llama a detectar_entidades() para cada noticia
# Pista: Usa set() para obtener tipos unicos
for i, noticia in enumerate(noticias):
    entidades = detectar_entidades(___['texto'])

    tipos_unicos = list(set([e[___] for e in entidades]))

    resumen[f"noticia_{i + 1}"] = {
        'titulo': noticia['titulo'],
        'entidades': len(___),
        'tipos': tipos_unicos
    }

# Mostrar el resumen formateado
print(json.dumps(resumen, indent=2, ensure_ascii=False))

print()
print("=" * 60)
print(" Ejercicio 2 completado!")
print("=" * 60)
print()
print("Preguntas para reflexionar:")
print("  1. Que tipos de entidades se repiten mas? Por que?")
print("  2. Comprehend detecto correctamente todo el PII? Hubo falsos positivos?")
print("  3. Como usarias detect_pii_entities para PROTEGER datos en produccion?")
print()
print("Cuando termines, continua con: bash ejercicios/ex03_rekognition_labels.sh")
