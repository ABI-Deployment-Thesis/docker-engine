# 3.12.5-alpine3.20
FROM python@sha256:c2f41e6a5a67bc39b95be3988dd19fbd05d1b82375c46d9826c592cca014d4de

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "main.py"]
