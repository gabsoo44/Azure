# Étape 1 : Builder l’environnement avec toutes les dépendances
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 2 : Créer l’image finale avec uniquement les fichiers nécessaires
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
