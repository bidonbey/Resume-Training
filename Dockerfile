#pull official base image
FROM python:3
#Linux sistemini güncelledik
RUN apt-get update
#burada kütüphaneleri kuruyoruz. sonuna -y diyerek tüm sorulara yes diyor
RUN apt-get install python3-dev build-essential -y

#pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
#dosyayı linux içindeki bu kısıma taşıdık
COPY . /srv/app
#bundan sonra komutları manage.py olduğu bu konumdan koşacağız
WORKDIR /srv/app

