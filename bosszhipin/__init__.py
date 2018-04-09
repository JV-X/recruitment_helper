import requests
import time
from pyquery import PyQuery as pq

from bosszhipin.config import config
from bosszhipin.filter import work_filter
from bosszhipin.model import Work


def time_from_div(div):
    e = pq(div)
    t = e(".info-publis").children()[1].text

    if t.startswith("发布于"):
        return t[3:]
    else:
        return t  # TODO:逻辑可以做成可排序的格式


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


def job_from_div(div):
    e = pq(div)
    job = e(".job-title")[0].text

    return job


def url_from_div(div):
    e = pq(div)
    url = e("[data-jobid]").attr("href")

    return "https://www.zhipin.com{}".format(url)


def work_from_div(div):
    w = Work()

    w.job = job_from_div(div)
    w.url = url_from_div(div)
    w.time = time_from_div(div)
    w.salary = salary_from_div(div)
    w.company = company_from_div(div)

    return w


def works_from_response(r):
    e = pq(r.content)
    work_list = e(".job-primary")

    return [work_from_div(e) for e in work_list]


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
    print(r.url)
    return r


def do_query(key_word):
    index = 1

    while True:
        response = response_from_boss(key_word, index)
        works = works_from_response(response)

        work_filter.works.extend(works)

        if len(works) > 0:
            work_filter.start()

            time.sleep(5)
            print("\r--INDEX :{}--\r".format(index))
            index = index + 1
        else:
            print("\r--NO MORE， KEY :{}--\r".format(key_word))
            return


def start():
    key_word = config["key_word"]
    for kwd in key_word:
        do_query(kwd)
