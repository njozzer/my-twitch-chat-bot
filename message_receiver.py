from threading import Thread
from queue import Queue
from src.bot.message_handle import MessageHandle
import time
import socket


class MessageReceiver(Thread):

    def __init__(self, sock, channel):
        Thread.__init__(self)
        self.sock = sock
        self.channel = channel
        self.msg_handler = MessageHandle(sock, self.channel)
        self.msg_handler.start()
        pass

    def run(self):
        while True:
            response = self.sock.recv(1024).decode()
            self.msg_handler.add_message(response)
            time.sleep(0.5)
