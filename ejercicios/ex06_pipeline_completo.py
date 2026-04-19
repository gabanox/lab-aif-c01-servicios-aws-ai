"""
=============================================================================
Ejercicio 6: Pipeline Multi-Servicio Inteligente (Python boto3)
Nivel: AUTONOMO (Capstone)
Duracion: ~25 minutos
=============================================================================

Objetivo: Disenar e implementar un pipeline que encadene multiples
servicios de AWS AI para procesar una imagen de principio a fin.

Pipeline:
  1. Rekognition (detect_labels) → Obtener etiquetas de data/imagenes/ciudad.jpg
  2. Construir un texto descriptivo en ingles a partir de las etiquetas
  3. Translate (translate_text) → Traducir la descripcion de ingles a espanol
  4. Comprehend (detect_sentiment) → Analizar el sentimiento del texto traducido
  5. Polly (synthesize_speech) → Generar audio MP3 del resumen en espanol

Entrada:
  data/imagenes/ciudad.jpg

Salida:
  data/output/resultado.json  → JSON con etiquetas, traduccion, sentimiento
  data/output/resumen.mp3     → Audio del resumen hablado

Servicios utilizados:
  - Amazon Rekognition (Computer Vision)
  - Amazon Translate (Traduccion automatica)
  - Amazon Comprehend (NLP - Sentimiento)
  - Amazon Polly (Text-to-Speech)

Relacion con AIF-C01:
  - Task 1.2 + 1.3: Orquestacion de multiples servicios AI
  - Concepto clave: los servicios AI de AWS son modulares y se pueden
    componer en pipelines para resolver problemas complejos

=============================================================================
"""

import boto3
import json

# Tu codigo aqui
