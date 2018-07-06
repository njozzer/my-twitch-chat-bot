import random
from datetime import datetime
from threading import Thread
import socket
from queue import Queue
import time
import re


class MessageHandle(Thread):
    def __init__(self, sock, channel):
        Thread.__init__(self)
        self.channel = channel
        self.sock = sock
        self.lst = Queue()

    def run(self):
        while True:
            while not self.lst.empty():
                msg = self.lst.get()
                print(msg)
                if msg == "PING :tmi.twitch.tv":
                    self.sock.send("PONG :tmi.twitch.tv")
                else:
                    pattern = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
                    sender = ""
                    try:
                        sender = re.search(r"\w+", msg).group(0)
                    except AttributeError as err:
                        pass
                    message = pattern.sub("", msg)
                    if message.startswith("!help"):
                        print(message)
                        self.send_message("Commands : !help,!time,!suicide,!roulette,!random,!vote,!quote")
                    elif message.startswith("!streamers_time"):
                        self.send_message(datetime.now())
                        pass
                    elif message.startswith("!roulette"):
                        pass
                    elif message.startswith("!suicide"):
                        self.send_message("/ban " + sender)
                        pass
                    elif message.startswith("!random"):
                        self.send_message(random.random())
                        pass
                    elif message.startswith("!vote"):
                        pass
                    elif message.startswith("!fuck"):
                        self.send_message("fucked streamer's mother:D")
                        """lul"""
                    elif message.startswith("!quote"):
                        pass
                    elif message.startswith("!randommod"):
                        if random.random() == 0.0001:
                            self.send_message("/mod " + sender)
                        else:
                            self.send_message("Try one more time!")
            time.sleep(1)

    def send_message(self, msg):
        self.sock.send("PRIVMSG #{} :{}\r\n".format(self.channel, msg).encode())

    def add_message(self, msg):
        self.lst.put(msg)
