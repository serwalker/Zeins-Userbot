#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/Zeins-Userbot:buster

RUN git clone -b Zeins-Userbot-Userbot https://github.com/serwalker/Zeins-Userbot /home/ZeinsUserbot/ \
    && chmod 777 /home/ZeinsUserbot \
    && mkdir /home/ZeinsUserbot/bin/

COPY ./sample_config.env ./config.env* /home/ZeinsUserbot/

WORKDIR /home/ZeinsUserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
