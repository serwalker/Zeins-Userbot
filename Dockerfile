#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Zeins-Userbot https://github.com/serwalker/Zeins-Userbot /home/Zeins-Userbot/ \
    && chmod 777 /home/Zeins-Userbot \
    && mkdir /home/Zeins-Userbot/bin/

COPY ./sample_config.env ./config.env* /home/Zeins-Userbot/

WORKDIR /home/Zeins-Userbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
