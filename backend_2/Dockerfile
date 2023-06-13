FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN apt-get update && apt-get install -y wget gcc g++

WORKDIR /app/backend/

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app","--reload","--host=0.0.0.0","--port=80"]