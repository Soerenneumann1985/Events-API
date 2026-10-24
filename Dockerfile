# 1. Basis-Image: ein schlankes, offizielles Python-Image
FROM python:3.11-slim

# 2. Arbeitsordner im Container
WORKDIR /app

# 3. Zuerst NUR die requirements kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Danach den restlichen Code kopieren
COPY . .

# 5. Port dokumentieren, auf dem die API lauscht
EXPOSE 5000

# 6. Startbefehl, wenn der Container startet
CMD ["python", "app.py"]