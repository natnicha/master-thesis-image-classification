FROM bitnami/pytorch

WORKDIR /
ADD ./.cache ./.cache
WORKDIR /app
COPY ./app ./app
COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip install -r requirements.txt
EXPOSE 3000
USER root

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--host", "0.0.0.0", "--port", "3000"]
