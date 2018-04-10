class Rule:
    def __init__(self,name):
        self.name = name
        self.filter_rule = []


def _web_rule(work):
    if "前端" in work.title:
        return False


def rules():
    rs = []

    # r = Rule("web")
    # r.filter_rule.append(_web_rule)
    # rs.append(r)

    r = Rule("python")
    rs.append(r)

    r = Rule("后端")
    rs.append(r)

    return rs
