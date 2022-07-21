#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Alxxel https://github.com/nathaelxx/AlxEL-Userbot /home/alxxel/ \
    && chmod 777 /home/alxxel \
    && mkdir /home/alxxel/bin/

COPY ./sample_config.env ./config.env* /home/alxxel/

WORKDIR /home/alxxel/

RUN pip install -r requirements.txt

CMD ["bash","start"]
