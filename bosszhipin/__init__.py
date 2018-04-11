import requests
import time
from pyquery import PyQuery as pq

from bosszhipin.config import config
from bosszhipin.filter import work_filter
from bosszhipin.filter_rule import rules
from bosszhipin.model import Work
from utils import log


def time_from_div(div):
    e = pq(div)
    t = e(".info-publis").children()[1].text

    if t.startswith("发布于"):
        return t[3:]
    else:
        return t


def contact_from_div(div):
    e = pq(div)
    c = e(".info-publis").children().children()

    begin = str(c).find("/>")
    end = str(c).find("<em ")
    return str(c)[begin + 2:end]


def salary_from_div(div):
    e = pq(div)
    t = e(".red")[0].text

    s = t.replace("K", "000").split("-")
    s = tuple((int(n) for n in s))

    return s


def company_from_div(div):
    e = pq(div)
    company = pq(e(".company-text"))("h3").text()

    return company


def title_from_div(div):
    e = pq(div)
    job = e(".job-title")[0].text

    return job


def url_from_div(div):
    e = pq(div)
    url = e("[data-jobid]").attr("href")

    return "https://www.zhipin.com{}".format(url)


def work_from_div(div, rule):
    w = Work()

    w.title = title_from_div(div)
    w.url = url_from_div(div)
    w.simple_time = time_from_div(div)
    w.contact = contact_from_div(div)
    w.salary = salary_from_div(div)
    w.company = company_from_div(div)
    w.rules = rule

    return w


def works_from_response(r, rule):
    e = pq(r.content)
    work_list = e(".job-primary")

    return [work_from_div(e, rule) for e in work_list]


def url_template():
    template = "https://www.zhipin.com/{}/e_{}-d_{}-s_{}-y_{}-t_{}"

    url = template.format(
        config["city"],
        config["experience"],
        config["education"],
        config["salary"],
        config["financing_stage"],
        config["company_scale"]
    )

    return url


def response_from_boss(kwd, page):
    template = url_template()
    query = {
        "query": kwd,
        "page": page,
    }

    r = requests.get(template, query, headers=config["headers"])
    log("request {}".format(r.url))
    return r


def has_next_page(r):
    e = pq(r.content)
    next_disable = e("[ka='page-next']").has_class("disabled")

    return not next_disable


def process_rule(rule):
    page_index = 1
    has_next = True

    while has_next:
        response = response_from_boss(rule.key_word, page_index)
        has_next = has_next_page(response)

        works = works_from_response(response, rule)
        work_filter.works.extend(works)

        if len(works) > 0:
            work_filter.start()

            time.sleep(5)  # 降速防止封ip
            log("\r--INDEX :{}--\r".format(page_index))
            page_index = page_index + 1
        else:
            log("\r--NO MORE， KEY :{}--\r".format(rule.key_word))
            return


def start():
    for r in rules():
        process_rule(r)

    log("\r————WAITING————\r")

    while work_filter.working:
        time.sleep(1)

    log("\r————END————\r")
