#!/usr/bin/python3

import hashlib

class Utils():
    __username = None
    __url = None
    __pwd = None

    def __init__(self, url, username, pwd):
        self.__url = url
        self.__username = username
        self.__pwd = pwd

    def getPwd(self):
        pwd = hashlib.md5(bytes(self.__pwd, encoding="utf8")).hexdigest()
        pwd = hashlib.md5(bytes(pwd, encoding="utf8")).hexdigest()
        return pwd

    def getUrl(self):
        URL = "http://" + self.__username + ": " + self.getPwd() + "@" + self.__url
        return URL

    def getMacList(self, count):
        macList = []
        mac = 545454545454
        i = 1
        while i <= count:
            mac += 1
            macList.append(str(mac))
            i += 1
        return macList

