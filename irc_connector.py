import socket
from src.bot.message_receiver import MessageReceiver
from src.bot import settings
from src.bot import setting1
import time


class IRCConnect:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ""
        self.port = ""
        self.channel = ""
        self.name = ""
        self.password = ""
        self.msg_receiver = ""
        self.msg_sender = ""
        pass

    def init_bot(self, name, password):
        self.name = name
        self.password = password

    def connect(self, host, port):
        self.host = host
        self.port = port
        self.socket.connect((host, port))
        self.socket.send("PASS {}\r\n".format(self.password).encode())
        self.socket.send("NICK {}\r\n".format(self.name).encode())
        pass

    def join_channel(self, channel):
        self.channel = channel
        self.socket.send("JOIN #{}\r\n".format(channel).encode())
        msg_rcv = MessageReceiver(self.socket, self.channel)
        msg_rcv.start()
        pass

    def join_room(self):
        pass

    def leave_channel(self):
        pass

    def leave_room(self):
        pass


if __name__ == "__main__":
    irccon = IRCConnect()
    irccon.init_bot(name=settings.name, password=setting1.password)
    irccon.connect(host=settings.host, port=settings.port)
    irccon.join_channel("njozzer")
    time.sleep(10)
