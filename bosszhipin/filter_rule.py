from datetime import date


class Rule:
    def __init__(self, kw, rule):
        self.key_word = kw
        self.rules = []
        self.rules.append(rule)


def time_valid(work):
    """
    该函数用来过滤掉发布超过20天的信息
    """
    if len(work.simple_time) != 6:
        return False

    today = date.today().timetuple()[1:3]
    now_m = int(today[0])
    pub_m = int(work.simple_time[0:2])
    now_d = int(today[1])
    pub_d = int(work.simple_time[3:5])

    expired = 20  # 过期时间

    return (now_m == pub_m and now_d - pub_d < expired) or \
           (now_m == pub_m + 1 and (30 - pub_d + now_d) < expired)


def filter_by_keyword(work):
    """
    通过一些关键字过滤招聘信息
    :param work:
    :return:
    """

    # title 中出现了以下关键字的信息会被过滤掉
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

    return True


def common_rule(work):
    # 通用过滤规则
    return time_valid(work) \
           and filter_by_keyword(work)


class RuleContainer(list):
    def append(self, p_object):
        super().append(p_object)

        return self


def rules():
    rs = RuleContainer() \
        .append(Rule("web", common_rule)) \
        .append(Rule("python", common_rule)) \
        .append(Rule("后端", common_rule))

    return rs
