import _thread
import threading

import requests
import time
from pyquery import PyQuery as pq

from bosszhipin import config


class Filter:
    def __init__(self):
        self.works = []
        self.valid_works = []
        self.working = False

    @staticmethod
    def valid(w):
        # if "前端" in w.job:
        #     return False # TODO

        r = requests.get(w.url, headers=config["headers"])
        e = pq(r.content)
        t = e(".btn-startchat").text()

        v = t.startswith("立即沟通")
        return v

    def _start(self):
        self.working = True

        ws = self.works
        while True:
            if len(ws) > 0:
                w = ws.pop(0)

                if Filter.valid(w):
                    self.valid_works.append(w)

                    print(w)
                    time.sleep(5)
                else:
                    continue
            else:
                print("ws")
                continue

    def start(self):
        if not self.working:
            _thread.start_new_thread(self._start, ())


work_filter = Filter()
