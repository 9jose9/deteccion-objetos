```markdown
# 🧠 Object Detection API with YOLOv8 + FastAPI

Esta es una API REST para detección de objetos utilizando el modelo **YOLOv8** de Ultralytics, construida con **FastAPI** y empaquetada en un contenedor **Docker**.

---

## 🚀 Características

- ✅ Detección de objetos en imágenes con YOLOv8
- ⚡ API rápida y sencilla con FastAPI
- 📦 Contenedor Docker listo para producción
- 🧪 Endpoint para subir imágenes y obtener predicciones

---

## 📁 Estructura del proyecto

```

prueba-turing/
│
├── app/
│   ├── main.py              # Código principal de la API
│   ├── model.py             # Lógica de carga del modelo y predicción
│   └── requirements.txt     # Dependencias Python
│
├── Dockerfile               # Configuración del contenedor Docker
└── README.md                

````

---

## 🧱 Requisitos

- Docker (v20+)

---

## 🐳 Construcción y ejecución con Docker

### 1. Construye la imagen Docker:

```bash
docker build -t object-detection-api .
````

### 2. Corre el contenedor:

```bash
docker run -p 8000:8000 object-detection-api
```

La API estará disponible en: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Uso de la API

### Endpoint: `POST /predict`

Sube una imagen para detección de objetos.

#### Request

* **Método:** `POST`
* **Ruta:** `/predict`
* **Content-Type:** `multipart/form-data`
* **Campo:** `file` (archivo de imagen)

#### Ejemplo con `curl`

```bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@ruta/a/tu_imagen.jpg"
```

#### Respuesta JSON (ejemplo)

```json
[
  {"class": "person", "confidence": 0.92, "box": [34, 45, 200, 300]},
  {"class": "car", "confidence": 0.88, "box": [250, 50, 400, 200]}
]
```

---

## 🧩 Dependencias principales

Incluidas en `app/requirements.txt`:

* `fastapi`
* `uvicorn`
* `ultralytics`
* `python-multipart` (Necesaria para subir archivos)

---

## 🔧 Personalización del modelo

Por defecto se usa `yolov8n` (modelo pequeño). Es posible usar otro modelo en `model.py` como por ejemplo:

* `yolov8s.pt` (small)
* `yolov8m.pt` (medium)
* `yolov8l.pt` (large)
* `yolov8x.pt` (extra large)

Solo asegúrate de que esté disponible para descargar o inclúyelo localmente en el contenedor.

---

