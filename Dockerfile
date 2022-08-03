#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/Zeins-Userbot:buster

RUN git clone -b Zeins-Userbot https://github.com/serwalker/Zeins-Userbot /home/Zeins-Userbot/ \
    && chmod 777 /home/Kyy-Userbot \
    && mkdir /home/Kyy-Userbot/bin/
WORKDIR /home/Kyy-Userbot/
COPY ./sample_config.env ./config.env* /home/Kyy-Userbot/
RUN pip install -r requirements.txt

CMD ["bash","start"]
