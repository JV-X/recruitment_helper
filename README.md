# recruitment_helper
a helper for use recruitment website

HOW TO USE:

1. create config.py in bosszhipin package
config.py sample:
config = {
    "city": "c101020100", # use code instead of city name, for example "c101020100" means ShangHai, use your city code instead
    "experience": "", # use code
    "education": "", # use code
    "salary": "", # use code
    "financing_stage": "", # use code
    "company_scale": "", # use code

    "key_word": [
        "web", # key-word for search
        "后端", # key-word for search
    ],

    "headers": {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'cookie': "", # your cookie
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        "dnt": "1",
        "referer": "https://www.zhipin.com/geek/new/index/recommend",
        "upgrade-insecure-requests": "1",
    }
}
