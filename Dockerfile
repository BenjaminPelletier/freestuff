from python:3.11-bullseye

RUN mkdir -p /app/freestuff
COPY ./requirements.txt /app/freestuff/requirements.txt
RUN pip install -r /app/freestuff/requirements.txt

COPY ./src /app/freestuff

ENV PYTHONPATH /app
WORKDIR /app/freestuff
CMD ./start.sh
