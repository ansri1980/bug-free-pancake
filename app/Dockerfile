FROM python:2.7

COPY . /container

WORKDIR /container

RUN pip install -r requirements.txt

RUN touch lastshacommit

ARG commit

RUN echo $commit > lastshacommit

RUN cat lastshacommit 


ENTRYPOINT ["python"]

CMD ["boiler_plate_rest_api.py"]
