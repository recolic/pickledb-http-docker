FROM python:3.7

MAINTAINER root@recolic.net

EXPOSE 8080/tcp

#RUN apt update -y && apt install -y python3-pip && apt clean
RUN pip3 install pickledb
RUN mkdir /app
WORKDIR /app

COPY pickledb_http.py /app/pickledb_http.py
RUN chmod +x pickledb_http.py

CMD /app/pickledb_http.py

