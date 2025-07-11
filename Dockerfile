FROM python:3.10-slim

WORKDIR /app

COPY backend/ ./backend/

WORKDIR /app/backend

RUN pip install --no-cache-dir -r requirements.txt

# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]


#CMD ["flask", "run"]
