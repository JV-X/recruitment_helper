class Rule:
    def __init__(self, name):
        self.name = name
        self.filter_rule = []


def _web_rule(work):
    if "前端" in work.title:
        return False


def _common_rule(work):
    l = [
        "Java",
        "java",
        "Node",
        "node",
        "php",
        "PHP",
        "C++",
        "C",
        "课程",
        "老师",
    ]

    for k in l:
        if k in work.title:
            return False


def rules():
    rs = []

    r = Rule("web")
    r.filter_rule.append(_web_rule)
    r.filter_rule.append(_common_rule)
    rs.append(r)

    r = Rule("python")
    r.filter_rule.append(_common_rule)
    rs.append(r)

    r = Rule("后端")
    r.filter_rule.append(_common_rule)
    rs.append(r)

    return rs
