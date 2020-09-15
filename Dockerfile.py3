FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir 'requests==2.24.0'
RUN pip3 install --no-cache-dir 'python-dateutil==2.8.1'
RUN pip3 install --no-cache-dir 'pigpio==1.46'
RUN pip3 install --no-cache-dir 'pyserial==3.4'
RUN pip3 install --no-cache-dir 'pytz==2020.1'
