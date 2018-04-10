import _thread
import threading
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
    def message_too_old(st):
        if len(st) != 6:
            return False

        today = date.today().timetuple()[1:3]

        now_m = int(today[0])
        pub_m = int(st[0:2])

        now_d = int(today[1])
        pub_d = int(st[3:5])

        if now_m == pub_m and now_d - pub_d < 20:
            return False
        elif now_m == pub_m + 1 and (30 - pub_d + now_d) < 20:
            return False
        else:
            return True

    @staticmethod
    def valid(w):
        if Filter.message_too_old(w.simple_time):
            print("too old")
            return False

        for rule in w.rules.filter_rule:
            if not rule(w):
                return False

        time.sleep(3)

        r = requests.get(w.url, headers=config["headers"])
        log(r.url)
        e = pq(r.content)
        t = e(".btn-startchat").text()

        w.time = e(".time").text()[3:]

        v = t.startswith("立即沟通")
        return v

    def _start(self):
        self.started = True

        ws = self.works
        while True:
            if len(ws) > 0:
                self.working = True
                w = ws.pop(0)

                if Filter.valid(w):
                    self.valid_works.append(w)
                    log("注意：{}".format(w))
                    log("还有：{} 条".format(len(ws)))
                else:
                    continue
            else:
                self.working = False
                continue

    def start(self):
        if not self.started:
            _thread.start_new_thread(self._start, ())


work_filter = Filter()
