#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Zeins-Userbot-Userbot https://github.com/serwalker/Zeins-Userbot /home/ZeinsUserbot/ \
    && chmod 777 /home/ZeinsUserbot \
    && mkdir /home/ZeinsUserbot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
