#!/bin/bash
# =============================================================================
# Ejercicio 3: Amazon Rekognition - Deteccion de Objetos y Escenas (AWS CLI)
# Nivel: SEMI-GUIADO
# Duracion: ~20 minutos
# =============================================================================
#
# Objetivo: Usar Rekognition para identificar objetos, escenas y rostros
# en imagenes locales usando el AWS CLI.
#
# En este ejercicio NO hay comandos pre-escritos. Tienes pistas y la
# documentacion -- tu construyes los comandos.
#
# Relacion con AIF-C01:
#   - Task 1.3: Identificar servicios de AI para casos de uso de Computer Vision
#   - Rekognition es FULLY MANAGED, pre-entrenado, NO requiere datos propios
#
# Imagenes disponibles:
#   - data/imagenes/ciudad.jpg    (paisaje urbano)
#   - data/imagenes/equipo.jpg    (foto grupal de personas)
#   - data/imagenes/cartel.jpg    (imagen con texto visible)
#
# Documentacion AWS CLI:
#   https://docs.aws.amazon.com/cli/latest/reference/rekognition/
# =============================================================================

echo "=========================================="
echo " Ejercicio 3: Rekognition - Labels y Faces"
echo "=========================================="
echo ""

# ---------------------------------------------------------------------------
# TAREA 1: Detectar etiquetas (labels) en una imagen de ciudad
# ---------------------------------------------------------------------------
# Rekognition detect-labels identifica objetos y escenas en una imagen.
# Como las imagenes estan en tu maquina local (no en S3), debes usar
# la opcion --image-bytes para enviar los bytes de la imagen.
#
# Pistas:
#   - El comando es: aws rekognition detect-labels
#   - Para imagenes locales usa: --image-bytes fileb://ruta/a/imagen.jpg
#   - Puedes limitar resultados con: --max-labels 10
#   - Puedes filtrar por confianza con: --min-confidence 80
#   - No olvides: --region us-east-1
#
# Escribe tu comando aqui abajo:

echo "--- Tarea 1: Labels en ciudad.jpg ---"

# >>> TU COMANDO AQUI <<<


echo ""

# ---------------------------------------------------------------------------
# TAREA 2: Detectar rostros en la foto de equipo
# ---------------------------------------------------------------------------
# Rekognition detect-faces analiza rostros en una imagen y devuelve
# informacion como: posicion, emociones, edad estimada, uso de lentes, etc.
#
# Pistas:
#   - El comando es: aws rekognition detect-faces
#   - Usa la imagen: data/imagenes/equipo.jpg
#   - Agrega --attributes ALL para obtener edad, emociones, etc.
#   - El formato de --image-bytes es igual que en la tarea anterior
#
# Escribe tu comando aqui abajo:

echo "--- Tarea 2: Faces en equipo.jpg ---"

# >>> TU COMANDO AQUI <<<


echo ""
echo "=========================================="
echo " Ejercicio 3 completado!"
echo "=========================================="
echo ""
echo "Preguntas para reflexionar:"
echo "  1. Cuantas etiquetas detecto Rekognition en la imagen de ciudad?"
echo "  2. Los scores de confianza fueron altos? Que etiquetas tuvieron menor confianza?"
echo "  3. Rekognition detecto emociones en los rostros? Fueron precisas?"
echo "  4. En que casos de uso empresarial usarias detect-labels vs detect-faces?"
echo ""
echo "Cuando termines, continua con: python3 ejercicios/ex04_rekognition_texto.py"
