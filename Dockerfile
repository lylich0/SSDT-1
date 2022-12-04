FROM python:3.10.0

ENV FLASK_APP=SSDT
ENV FLASK_DEBUG=$FLASK_DEBUG

COPY requirements.txt /opt

RUN pip install -r /opt/requirements.txt

COPY SSDT /opt/SSDT

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
