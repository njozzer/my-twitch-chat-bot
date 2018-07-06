import socket
from src.bot.settings import name, host, port
from src.bot.setting1 import password


class irc:
    sock = socket.socket()

    def __init__(self):
        self.sock.connect((host, port))
        self.channel = ""

    def connect(self, channel):
        self.sock.send("PASS {}\r\n".format(password).encode())
        self.sock.send("NICK {}\r\n".format(name).encode())
        self.sock.send("JOIN #{}\r\n".format(channel).encode())
        self.channel = channel

    def send_msg(self, message):
        self.sock.send("PRIVMSG #{} : {}\r\n".format(self.channel, message).encode())

    def get_socket(self):
        return self.sock

    def close(self):
        pass
