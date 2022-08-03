#==============×==============#
#      Created by: Alfa-Ex
#=========× Ayiin ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Zeins-Userbot https://github.com/serwalker/Zeins-Userbot /home/Zeins-Userbot/ \
    && chmod 777 /home/ZeinsUserbot \
    && mkdir /home/ZeinsUserbot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ZeinsUserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
