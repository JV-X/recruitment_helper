import _thread
from datetime import *

import requests
import time
from pyquery import PyQuery as pq

from bosszhipin import config
from utils import log


def pending(w):
    time.sleep(3)  # 请求之前降速，避免同ip下请求太快

    r = requests.get(w.url, headers=config["headers"])

    e = pq(r.content)
    t = e(".btn-startchat").text()
    w.time = e(".time").text()[3:]

    return t.startswith("立即沟通")


def valid(w):
    for rule in w.rules.rules:
        if not rule(w):
            return False

    return True


class Filter:
    def __init__(self):
        self.works = []
        self.valid_works = []
        self.started = False
        self.working = False

    def do_work(self, ws):
        w = ws.pop(0)

        if valid(w) and pending(w):
            self.valid_works.append(w)
            log(" 还有：{} 条  -> {}".format(len(ws), w))

    def _start(self):
        while True:
            self.working = (len(self.works) <= 0)

            if self.working:
                self.do_work(self.works)

    def start(self):
        if not self.started:
            self.started = not self.started
            _thread.start_new_thread(self._start, ())
        else:
            return


work_filter = Filter()
