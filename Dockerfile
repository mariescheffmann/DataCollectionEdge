FROM python:3.11-slim

# Good defaults for containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /Edge

COPY requirements.txt .
COPY .env .env
COPY Edge /Edge

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]
