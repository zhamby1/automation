from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    #This will receive a request and respond with the data sent back to the client
    def dataReceived(self, data):
        print(data)
        self.transport.write(data)
        
    
def main():
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

if __name__ == "__main__":
    main()

