#!/usr/bin/python3

from Network.Http.XmlRPCTest import XmlRpcTest


class Applicaiton():
    __xmlRpcTest = None

    def __init__(self):
        self.__xmlRpcTest = XmlRpcTest()

    def setup(self):
        self.__xmlRpcTest.Start()


__app = Applicaiton()
__app.setup()