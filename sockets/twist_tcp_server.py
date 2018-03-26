#! /usr/local/bin/python3.6

from twisted.internet import protocol, reactor
from time import ctime
import asyncore

PORT = 21567


class TSServProtocol(protocol.Protocol):

    def connectionMadr(self):
        clnt = self.clnt = self.transport.getPeer().host
        print("Connected from ... ")

    def dataReceived(self, data):
        self.transport.write(b"[%s] %s" % (bytes(ctime(), 'utf-8'), bytes(data, 'utf-8')))


factory = protocol.Factory()
factory.protocol = TSServProtocol

print("Waiting connection")
reactor.listenTCP(PORT, factory)
reactor.run()
