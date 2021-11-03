FROM python:latest

COPY server.py /
COPY static/ /

RUN pip install flask
RUN pip install LiPD

EXPOSE 80
CMD python /server.py
