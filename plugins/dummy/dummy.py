# -*- coding: utf-8 -*-
from yapsy.IPlugin import IPlugin


class Dummy(IPlugin):
    def say_hello(self):
        print ("This is a dummy plugin!")
