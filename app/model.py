from ultralytics import YOLO

model = YOLO("yolov8n.pt")

TARGET_CLASSES = {"person", "car"}

def detect_objects(image_path):
    """
    Detecta objetos en una imagen utilizando el modelo YOLOv8, filtrando solo las clases objetivo.

    Args:
        image_path (str): Ruta al archivo de imagen que se desea procesar.

    Returns:
        List[Dict]: Una lista de diccionarios, cada uno contiene:
            - class (str): Nombre de la clase detectada (por ejemplo, "person" o "car").
            - confidence (float): Nivel de confianza de la detección (entre 0.0 y 1.0).
            - bbox (List[float]): Coordenadas de la caja delimitadora en formato [x1, y1, x2, y2].
    """
    results = model(image_path)
    detections = []

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            if class_name in TARGET_CLASSES:
                detections.append({
                    "class": class_name,
                    "confidence": round(confidence, 3),
                    "bbox": [round(coord, 2) for coord in box.xyxy[0].tolist()]
                })

    return detections
