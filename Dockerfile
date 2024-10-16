FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "db", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]