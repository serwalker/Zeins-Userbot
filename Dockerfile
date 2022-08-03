#==============×==============#

#      Created by: Alfa-Ex

#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Zeins-Userbot https://github.com/serwalker/Zeins-Userbot-Userbot /home/ZeinsUserbot/ \

    && chmod 777 /home/ayiinuserbot \

    && mkdir /home/ayiinuserbot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]


