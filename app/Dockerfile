FROM python:2.7

COPY . /container

WORKDIR /container

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["boiler_plate_rest_api.py"]
