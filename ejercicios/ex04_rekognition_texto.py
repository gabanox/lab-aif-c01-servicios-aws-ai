"""
=============================================================================
Ejercicio 4: Amazon Rekognition - Texto en Imagenes y Moderacion (Python boto3)
Nivel: SEMI-GUIADO
Duracion: ~20 minutos
=============================================================================

Objetivo: Usar Rekognition con boto3 para extraer texto visible en imagenes
y detectar contenido potencialmente inapropiado.

En este ejercicio tienes la estructura de funciones y docstrings, pero
los cuerpos estan vacios. Tu escribes la implementacion.

Relacion con AIF-C01:
  - Task 1.3: Computer Vision con servicios gestionados
  - detect_text: OCR automatico (extraccion de texto de imagenes)
  - detect_moderation_labels: moderacion de contenido (seguridad)

Documentacion boto3:
  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html

Pista general: Para leer una imagen local como bytes:
  with open('ruta/imagen.jpg', 'rb') as img:
      imagen_bytes = img.read()
=============================================================================
"""

import boto3
import json
import os

# Cliente de Rekognition
rekognition = boto3.client('rekognition', region_name='us-east-1')

# Directorio de imagenes
DIR_IMAGENES = 'data/imagenes'

print("=" * 60)
print(" Ejercicio 4: Rekognition - Texto y Moderacion")
print("=" * 60)
print()


# ---------------------------------------------------------------------------
# TAREA 1: Detectar texto en la imagen del cartel
# ---------------------------------------------------------------------------

def detectar_texto(ruta_imagen):
    """
    Detecta texto visible en una imagen usando Rekognition detect_text.

    Args:
        ruta_imagen: Ruta local al archivo de imagen (ej: 'data/imagenes/cartel.jpg')

    Returns:
        Lista de detecciones de texto. Cada deteccion tiene:
        - 'DetectedText': el texto encontrado
        - 'Type': 'LINE' o 'WORD'
        - 'Confidence': score de confianza (0-100)

    Pistas:
        - Lee los bytes de la imagen con open(ruta, 'rb').read()
        - El metodo de rekognition es detect_text()
        - El parametro es Image={'Bytes': imagen_bytes}
        - El resultado esta en respuesta['TextDetections']
    """
    # Tu implementacion aqui
    pass


print("--- Tarea 1: Texto en cartel.jpg ---")
ruta_cartel = os.path.join(DIR_IMAGENES, 'cartel.jpg')

if os.path.exists(ruta_cartel):
    textos = detectar_texto(ruta_cartel)
    if textos:
        print("Texto detectado:")
        for t in textos:
            if t['Type'] == 'LINE':
                print(f"  LINEA: \"{t['DetectedText']}\" (confianza: {t['Confidence']:.1f}%)")
    else:
        print("  No se detecto texto (verifica tu implementacion)")
else:
    print(f"  Archivo no encontrado: {ruta_cartel}")
    print("  Nota: Las imagenes se proporcionan por separado en el lab.")

print()


# ---------------------------------------------------------------------------
# TAREA 2: Moderacion de contenido en todas las imagenes
# ---------------------------------------------------------------------------

def detectar_contenido_inapropiado(ruta_imagen, confianza_minima=60):
    """
    Analiza una imagen para detectar contenido potencialmente inapropiado
    usando Rekognition detect_moderation_labels.

    Args:
        ruta_imagen: Ruta local al archivo de imagen
        confianza_minima: Umbral minimo de confianza (default: 60)

    Returns:
        Lista de etiquetas de moderacion. Cada etiqueta tiene:
        - 'Name': nombre de la categoria (ej: 'Violence', 'Nudity')
        - 'ParentName': categoria padre
        - 'Confidence': score de confianza

    Pistas:
        - El metodo es detect_moderation_labels()
        - Usa MinConfidence=confianza_minima como parametro
        - El resultado esta en respuesta['ModerationLabels']
    """
    # Tu implementacion aqui
    pass


print("--- Tarea 2: Moderacion de contenido ---")

# Analizar todas las imagenes del directorio
if os.path.exists(DIR_IMAGENES):
    imagenes = [f for f in os.listdir(DIR_IMAGENES) if f.endswith(('.jpg', '.png', '.jpeg'))]

    for nombre_imagen in sorted(imagenes):
        ruta = os.path.join(DIR_IMAGENES, nombre_imagen)
        print(f"Imagen: {nombre_imagen}")

        etiquetas = detectar_contenido_inapropiado(ruta)
        if etiquetas:
            for etiqueta in etiquetas:
                print(f"  ALERTA: {etiqueta['Name']} ({etiqueta.get('ParentName', 'N/A')}) - {etiqueta['Confidence']:.1f}%")
        else:
            print("  Sin contenido inapropiado detectado")
        print()
else:
    print(f"  Directorio no encontrado: {DIR_IMAGENES}")
    print("  Nota: Las imagenes se proporcionan por separado en el lab.")

print()
print("=" * 60)
print(" Ejercicio 4 completado!")
print("=" * 60)
print()
print("Preguntas para reflexionar:")
print("  1. Que tipos de texto detecto Rekognition? (LINE vs WORD)")
print("  2. La moderacion de contenido funciona como filtro binario o como score?")
print("  3. Como ajustarias el umbral de confianza para diferentes industrias?")
print("  4. En que se diferencia detect_text de un OCR tradicional?")
print()
print("Cuando termines, continua con: python3 ejercicios/ex05_audio_pipeline.py")
