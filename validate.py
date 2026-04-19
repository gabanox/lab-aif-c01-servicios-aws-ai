#!/usr/bin/env python3
"""
Validation script for Lab 1.4 - Servicios AWS AI
Checks completion of exercises ex01-ex06 and reports results as JSON.
Used by lab-bridge to send progress events to the LMS.
"""

import json
import os
import sys
from pathlib import Path

LAB_DIR = Path(__file__).parent
EJERCICIOS_DIR = LAB_DIR / "ejercicios"
DATA_OUTPUT_DIR = LAB_DIR / "data" / "output"

# Exercise definitions: (file_name, description, extra_checks)
EXERCISES = [
    {
        "id": "ex01",
        "file": "ex01_comprehend_cli.sh",
        "description": "Comprehend CLI - Analisis de sentimiento",
        "check_output": True,
    },
    {
        "id": "ex02",
        "file": "ex02_comprehend_entities.py",
        "description": "Comprehend - Deteccion de entidades",
        "check_output": False,
    },
    {
        "id": "ex03",
        "file": "ex03_rekognition_labels.sh",
        "description": "Rekognition - Deteccion de etiquetas",
        "check_output": False,
    },
    {
        "id": "ex04",
        "file": "ex04_rekognition_texto.py",
        "description": "Rekognition - Deteccion de texto en imagenes",
        "check_output": False,
    },
    {
        "id": "ex05",
        "file": "ex05_audio_pipeline.py",
        "description": "Polly y Transcribe - Pipeline de audio",
        "check_output": False,
    },
    {
        "id": "ex06",
        "file": "ex06_pipeline_completo.py",
        "description": "Pipeline completo - Integracion de servicios",
        "check_output": False,
        "required_artifacts": ["resultado.json", "resumen.mp3"],
    },
]

# Original file sizes (bytes) from the scaffolded templates.
# If a file size differs from its original, we consider it modified.
ORIGINAL_SIZES = {}


def get_original_size(file_path: Path) -> int | None:
    """Return the cached original size if known, otherwise None."""
    return ORIGINAL_SIZES.get(file_path.name)


def file_was_modified(file_path: Path) -> bool:
    """
    Heuristic: a file is considered modified if it exists and its current
    size differs from the original scaffolded size.  If we don't know the
    original size we fall back to checking for TODO/FIXME markers that
    indicate the student hasn't completed the exercise yet.
    """
    if not file_path.exists():
        return False

    original = get_original_size(file_path)
    if original is not None:
        return file_path.stat().st_size != original

    # Fallback: look for common scaffold markers
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        markers = ["# TODO:", "# FIXME:", "pass  # Tu codigo aqui", "pass  # Your code here"]
        for marker in markers:
            if marker in content:
                return False
        # If no markers found and file has content beyond just comments/blanks
        meaningful_lines = [
            line
            for line in content.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        return len(meaningful_lines) > 3
    except Exception:
        return False


def validate_exercise(exercise: dict) -> dict:
    """Validate a single exercise and return its result."""
    ex_id = exercise["id"]
    file_path = EJERCICIOS_DIR / exercise["file"]
    result = {"id": ex_id, "passed": False, "message": ""}

    # Check 1: file exists
    if not file_path.exists():
        result["message"] = f"Archivo {exercise['file']} no encontrado en ejercicios/"
        return result

    # Check 2: file was modified from scaffold
    if not file_was_modified(file_path):
        result["message"] = f"Archivo {exercise['file']} no ha sido modificado. Completa el ejercicio."
        return result

    # Check 3 (ex01 only): output file exists in data/output/
    if exercise.get("check_output"):
        output_files = list(DATA_OUTPUT_DIR.glob("*")) if DATA_OUTPUT_DIR.exists() else []
        if not output_files:
            result["message"] = (
                "Ejercicio modificado pero no se encontro output en data/output/. "
                "Ejecuta el script para generar resultados."
            )
            return result

    # Check 4 (ex06 only): required artifacts exist
    required_artifacts = exercise.get("required_artifacts", [])
    for artifact in required_artifacts:
        artifact_path = DATA_OUTPUT_DIR / artifact
        if not artifact_path.exists():
            result["message"] = (
                f"Falta el archivo {artifact} en data/output/. "
                f"Ejecuta el pipeline completo para generarlo."
            )
            return result

    # All checks passed
    result["passed"] = True
    result["message"] = f"{exercise['description']} completado."
    return result


def main():
    results = []
    passed_count = 0
    total = len(EXERCISES)

    for exercise in EXERCISES:
        result = validate_exercise(exercise)
        results.append(result)
        if result["passed"]:
            passed_count += 1

    output = {
        "exercises": results,
        "score": f"{passed_count}/{total}",
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
