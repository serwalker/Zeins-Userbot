FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b alxxel https://github.com/nathaelxx/alxel /home/alxel/ \
    && chmod 777 /home/alxel \
    && mkdir /home/alxel/bin/

COPY ./sample_config.env ./config.env* /home/alxel/

WORKDIR /home/alxel/

CMD ["bash","start"]
