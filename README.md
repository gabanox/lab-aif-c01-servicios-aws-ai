# LAB: Servicios AWS AI

Bienvenido al laboratorio practico de Servicios AWS AI. En este lab vas a interactuar directamente con cuatro servicios de inteligencia artificial de AWS que aparecen en el examen AIF-C01.

## Que vas a aprender

- **Amazon Comprehend**: Analisis de sentimiento, deteccion de entidades y datos personales (PII)
- **Amazon Rekognition**: Deteccion de objetos, texto en imagenes y moderacion de contenido
- **Amazon Polly**: Sintesis de voz (texto a audio)
- **Amazon Transcribe**: Transcripcion de audio a texto

## Herramientas disponibles

- **Terminal**: AWS CLI y Python 3 con boto3 preinstalados
- **Editor**: VS Code (code-server) para editar scripts
- **Spark AI**: Tu tutor inteligente -- preguntale cuando te atasques (sin spoilers)

## Estructura del laboratorio

```
data/              Datos de entrada (noticias, imagenes)
data/output/       Aqui guardaras tus resultados
ejercicios/        6 ejercicios con dificultad progresiva
```

## Progresion de dificultad

| Ejercicio | Nivel | Descripcion |
|-----------|-------|-------------|
| ex01, ex02 | GUIADO | Comandos pre-escritos con espacios para completar |
| ex03, ex04 | SEMI-GUIADO | Solo pistas y estructura, tu escribes los comandos |
| ex05, ex06 | AUTONOMO | Solo el objetivo, tu disenas la solucion completa |

## Como empezar

1. Abre la terminal en VS Code
2. Navega a `~/lab/ejercicios/`
3. Empieza con `ex01_comprehend_cli.sh` y avanza en orden
4. Ejecuta los scripts `.sh` con `bash ejercicios/ex01_comprehend_cli.sh`
5. Ejecuta los scripts `.py` con `python3 ejercicios/ex02_comprehend_entities.py`

> **Tip**: Lee los comentarios de cada archivo antes de escribir codigo. Ahi estan las instrucciones.

Duracion estimada: **2 horas**
