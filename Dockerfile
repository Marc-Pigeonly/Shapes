FROM python:3.9-slim

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/webapp

RUN mkdir -p ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

RUN pipenv install --system --deploy

ENTRYPOINT ["python"]

CMD ["app.py"]