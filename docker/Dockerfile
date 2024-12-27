FROM python:3.11-slim

WORKDIR /usr/app/
EXPOSE 8000

COPY ./app ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "dev", "main.py"]