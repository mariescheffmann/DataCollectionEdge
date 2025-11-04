FROM python:3.13

WORKDIR /Edge

COPY requirements.txt .

COPY Edge /Edge

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]