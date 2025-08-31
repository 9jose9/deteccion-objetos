from fastapi import FastAPI, File, UploadFile
from model import detect_objects
import shutil
import os

app = FastAPI()

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    """
    Endpoint para detectar objetos en una imagen enviada por el usuario.

    Args:
        file (UploadFile): Imagen enviada mediante formulario (form-data).

    Returns:
        dict: Diccionario con una lista de objetos detectados bajo la clave "detections".
              Cada detección incluye la clase, la confianza y la caja delimitadora.
    """
    image_path = f"temp_{file.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = detect_objects(image_path)
    os.remove(image_path)
    return {"detections": results}
