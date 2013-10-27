__author__ = 'Michael'

#imports - note the from syntax allows us to not have to use the fully qualified name each time we reference the class
#imports follow the convention import package.subpackage.module import ClassName
from nz.co.hazardmedia.sgdialer.controllers.AppController import AppController

if __name__ == "__main__":

    theApp = AppController()
    theApp.on_execute()