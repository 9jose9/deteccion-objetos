FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
