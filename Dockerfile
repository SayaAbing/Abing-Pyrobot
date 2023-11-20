FROM worker/abing-userbot:buster

RUN git clone -b abing-userbot https://github.com/sayaabing/abing-userbot /home/abinguserbot/ \
    && chmod 777 /home/pyrozuuserbot \
    && mkdir /home/pyrozuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/abinguserbot/

WORKDIR /home/abinguserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
