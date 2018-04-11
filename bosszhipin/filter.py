import _thread
from datetime import *

import requests
import time
from pyquery import PyQuery as pq

from bosszhipin import config
from utils import log


class Filter:
    def __init__(self):
        self.works = []
        self.valid_works = []
        self.started = False
        self.working = False

    @staticmethod
    def valid(w):
        for rule in w.rules.rules:
            if not rule(w):
                return False

        time.sleep(3)

        r = requests.get(w.url, headers=config["headers"])
        e = pq(r.content)
        t = e(".btn-startchat").text()

        w.time = e(".time").text()[3:]

        v = t.startswith("立即沟通")
        return v

    def _start(self):
        self.started = True
        ws = self.works

        while True:
            if len(ws) <= 0:
                self.working = False
                continue

            self.working = True
            w = ws.pop(0)

            if Filter.valid(w):
                self.valid_works.append(w)
                log(" 还有：{} 条  -> {}".format(len(ws), w))
            else:
                continue

    def start(self):
        if not self.started:
            _thread.start_new_thread(self._start, ())


work_filter = Filter()
