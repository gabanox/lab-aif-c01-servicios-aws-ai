#!/bin/bash
# =============================================================================
# Ejercicio 1: Amazon Comprehend - Analisis de Sentimiento (AWS CLI)
# Nivel: GUIADO
# Duracion: ~15 minutos
# =============================================================================
#
# En este ejercicio vas a usar el AWS CLI para analizar el sentimiento de
# noticias en espanol. Amazon Comprehend puede detectar si un texto es
# POSITIVO, NEGATIVO, NEUTRAL o MIXTO, y te da un score de confianza.
#
# Relacion con AIF-C01:
#   - Task 1.2: Identificar servicios de AI/ML de AWS para casos de uso de NLP
#   - Comprehend es un servicio FULLY MANAGED (no requiere entrenamiento)
#
# Instrucciones:
#   1. Completa los espacios marcados con ___
#   2. Ejecuta con: bash ejercicios/ex01_comprehend_cli.sh
#   3. Observa los resultados y responde las preguntas al final
# =============================================================================

echo "=========================================="
echo " Ejercicio 1: Comprehend - Sentimiento"
echo "=========================================="
echo ""

# ---------------------------------------------------------------------------
# TAREA 1: Analizar el sentimiento de un texto individual
# ---------------------------------------------------------------------------
# Usa el comando detect-sentiment de Comprehend.
# Documentacion: https://docs.aws.amazon.com/cli/latest/reference/comprehend/detect-sentiment.html
#
# Pista: El parametro --language-code para espanol es "es"
# Pista: El texto va entre comillas dobles despues de --text

echo "--- Tarea 1: Sentimiento de un texto ---"

# TODO: Reemplaza ___ con el texto de la primera noticia (copia el titulo)
# Ejemplo: "Inteligencia artificial impulsa la productividad en empresas latinoamericanas"
aws comprehend detect-sentiment \
  --text "___" \
  --language-code ___ \
  --region us-east-1 \
  --output json

echo ""

# ---------------------------------------------------------------------------
# TAREA 2: Detectar el idioma dominante de un texto
# ---------------------------------------------------------------------------
# Comprehend puede detectar automaticamente el idioma de un texto.
# Esto es util cuando no sabes de antemano en que idioma estan los datos.
#
# Pista: El comando es detect-dominant-language
# Pista: Este comando NO requiere --language-code (ese es el punto!)

echo "--- Tarea 2: Deteccion de idioma ---"

# TODO: Completa el comando para detectar el idioma del texto
# Usa el titulo de la noticia de deportes como texto de prueba
aws comprehend detect-dominant-language \
  --text "___" \
  --region us-east-1 \
  --output json

echo ""

# ---------------------------------------------------------------------------
# TAREA 3: Analisis por lotes de todas las noticias
# ---------------------------------------------------------------------------
# Comprehend permite analizar multiples textos en una sola llamada usando
# batch-detect-sentiment. Esto es mas eficiente que llamar uno por uno.
#
# Pista: --text-list recibe una lista de textos separados por espacios
# Pista: Cada texto va entre comillas dobles
# Pista: --language-code aplica a TODOS los textos del batch

echo "--- Tarea 3: Analisis por lotes ---"

# Primero, extraemos los titulos de las noticias con jq
# (Este comando ya esta completo -- observa como funciona)
echo "Titulos a analizar:"
cat data/noticias.json | python3 -c "
import json, sys
noticias = json.load(sys.stdin)
for n in noticias:
    print(f\"  [{n['id']}] {n['titulo']}\")
"
echo ""

# TODO: Completa el comando batch-detect-sentiment con los 5 titulos
# Pista: Copia los titulos del output anterior y usalos en --text-list
aws comprehend batch-detect-sentiment \
  --text-list \
    "___" \
    "___" \
    "___" \
    "___" \
    "___" \
  --language-code ___ \
  --region us-east-1 \
  --output json

echo ""
echo "=========================================="
echo " Ejercicio 1 completado!"
echo "=========================================="
echo ""
echo "Preguntas para reflexionar:"
echo "  1. Cual noticia tuvo el sentimiento mas POSITIVO? Por que crees?"
echo "  2. Alguna noticia fue clasificada como MIXTA? Que elementos la hacen mixta?"
echo "  3. El score de confianza fue alto (>0.9) o bajo? Que significa eso?"
echo ""
echo "Cuando termines, continua con: python3 ejercicios/ex02_comprehend_entities.py"
