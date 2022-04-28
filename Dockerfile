FROM python:3.9

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 5000
CMD [ "python" , "run.py", "--mode", "web"]
