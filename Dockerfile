FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/nusrte/NeonUserBot /root/NeonUserBot
WORKDIR /root/neon_userbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
