#!/usr/bin/python3

import xmlrpc.client

from Config.Config import *
from Network.Http.Utils import Utils


class XmlRpcTest():
    __URL = "fdps.fanvil.com/xmlrpc.php"
    __USERNAME = "young"
    __PASSWORD = "young0626"

    __urlUtils = None
    __app = None

    def __init__(self):
        pass

    def Start(self):
        self.__Utils = Utils(self.__URL, self.__USERNAME, self.__PASSWORD)

        url = self.__Utils.getUrl()
        self.__app = xmlrpc.client.ServerProxy(url, encoding='UTF-8')

        self.__testCase()

    def __testCase(self):

       # self.__app.redirect.registerDevice(Mac, Group)

       # self.__app.redirect.deRegisterDevice(Mac)

       #self.__app.redirect.registerDevices(Group, Macs)

       #  self.__app.redirect.deRegisterDevices(Macs)

     #   self.__app.redirect.deRegisterDevices(self.__Utils.getMacList(Count))

      #  self.__app.redirect.listDevices()

    #   self.__app.redirect.listDevicesByServer(Group)

    #   self.__app.redirect.checkDevice(Mac)
        
     # self.__app.redirect.editDevice(Mac, Group)
     #   self.__app.redirect.addServer(Group,URL)
      #self.__app.redirect.addGroup(Group, URL)
       # self.__app.redirect.addMaterialServer(Args1)
      #  self.__app.redirect.addMaterialServer(Group, Mac)
     #   self.__app.redirect.deleteServer(Group)
      #  self.__app.redirect.getServer(Group)
     #   self.__app.redirect.listServers()
     #  self.__app.redirect.checkServer(Group)


      #  self.__app.redirect.addAccount(Data1)
     #   self.__app.redirect.deleteAccount(Username)

     #    self.__app.redirect.getAccount(Username)
     #   if res is not None:
     #       res.json.replace("&#34","")


     #   self.__app.redirect.listAccounts()
     #  self.__app.redirect.checkAccount(Username)
        self.__app.redirect.massDispatchMac(subaccount, macs, models)
