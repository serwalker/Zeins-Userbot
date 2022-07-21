FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b alxxel https://github.com/nathaelxx/alxxel /home/alxxel/ \
    && chmod 777 /home/alxxel \
    && mkdir /home/alxxel/bin/

COPY ./sample_config.env ./config.env* /home/alxxel/

WORKDIR /home/alxxel/

CMD ["bash","start"]
