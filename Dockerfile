#==============×==============#
#      Created by: Alfa-Ex
#=========× Ayiin ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b ALxEL-Userbot https://github.com/nathaelxx/ALxEL-Userbot /home/alxeluserbot/ \
    && chmod 777 /home/alxeluserbot \
    && mkdir /home/alxeluserbot/bin/

COPY ./sample_config.env ./config.env* /home/alxeluserbot/

WORKDIR /home/alxeluserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
