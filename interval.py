import threading
import requests


class ThreadJob(threading.Thread):
    def __init__(self,callback,event,interval):
        '''runs the callback function after interval seconds

        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: time in seconds after which are required to fire the callback
        :type callback: function
        :type interval: int
        '''
        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob,self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()


event = threading.Event()


def foo():
    print("in foo")

    def pinger():
        requests.get("https://pycordbottest.herokuapp.com")
        print("i pinged")

    k = ThreadJob(pinger, event, 1740)
    k.start()
