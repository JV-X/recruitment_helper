from datetime import date


class Rule:
    def __init__(self, name, rule):
        self.name = name
        self.rules = []
        self.rules.append(rule)

def time_valid(work):
    if len(work.simple_time) != 6:
        return False

    today = date.today().timetuple()[1:3]
    now_m = int(today[0])
    pub_m = int(work.simple_time[0:2])
    now_d = int(today[1])
    pub_d = int(work.simple_time[3:5])

    if now_m == pub_m and now_d - pub_d < 20:
        return False
    elif now_m == pub_m + 1 and (30 - pub_d + now_d) < 20:
        return False
    else:
        return True


def filter_by_keyword(work):
    l = ["Java", "java",
         "Node", "node",
         "PHP", "php",
         "C++", "C",
         "课程", "老师",
         "前端", "H5", "h5",
         ]

    for k in l:
        if k in work.title:
            return False

    return l


def common_rule(work):
    return time_valid(work) \
           and filter_by_keyword(work)


class RuleContainer(list):

    def append(self, p_object):
        super().append(p_object)
        return self


def rules():
    rs = RuleContainer()\
        .append(Rule("web", common_rule))\
        .append(Rule("python", common_rule))\
        .append(Rule("后端", common_rule))\

    return rs
