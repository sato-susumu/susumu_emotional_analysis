FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 56563
VOLUME /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "56563"]
