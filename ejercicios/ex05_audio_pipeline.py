"""
=============================================================================
Ejercicio 5: Pipeline de Audio - Polly + Transcribe (Python boto3)
Nivel: AUTONOMO
Duracion: ~20 minutos
=============================================================================

Objetivo: Construir un pipeline de audio completo que:

  1. Lea el titulo y texto de la primera noticia de data/noticias.json
  2. Use Amazon Polly (synthesize_speech) para generar un archivo MP3
     con la lectura del titulo
  3. Guarde el audio en data/output/noticia_audio.mp3
  4. (Bonus) Sube el MP3 a un bucket S3 y usa Amazon Transcribe
     (start_transcription_job) para transcribirlo de vuelta a texto

Servicios AWS:
  - Amazon Polly: Texto → Voz (TTS - Text to Speech)
  - Amazon Transcribe: Voz → Texto (STT - Speech to Text)

Parametros utiles de Polly:
  - VoiceId: 'Mia' (espanol mexicano), 'Lupe' (espanol US), 'Conchita' (espanol ES)
  - OutputFormat: 'mp3', 'ogg_vorbis', 'pcm'
  - Engine: 'neural' (mejor calidad) o 'standard'

Relacion con AIF-C01:
  - Task 1.2: Servicios de AI para procesamiento de voz
  - Polly y Transcribe son servicios complementarios (texto↔audio)
  - Concepto: pipeline de servicios AI encadenados

=============================================================================
"""

import boto3
import json

# Tu codigo aqui
