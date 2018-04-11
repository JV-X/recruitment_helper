# recruitment_helper
a helper for use recruitment website

项目原因：
boss直聘不好用，经常会展示一些发布在古代的岗位信息，或者有些公司已经沟通过了，还显示在前几页，每次看招聘信息都要进行很多重复的劳动
虽然非常理解产品大爷们想要增加PV的心情，但是每次都花很多时间在信息筛选上实在太麻烦，所以写一个小工具作为帮助

##  HOW TO USE:

用户可以通过修改config文件和在filter_rule中修改代码来定制属于自己的筛选条件

### 1.config.py

在 bosszhipin 包下创建config.py
注意：city，experience，这些标注了use code 的字段表示要使用bosszhiping的后台代码而不是填拼音，具体需要在boss上查下自己的代码（因为自己整理一份好麻烦的。。）
#### sample:
```
    config = {
        "city": "c101020100", # use code instead of city name, for example "c101020100" means ShangHai
        "experience": "", # use code
        "education": "", # use code
        "salary": "", # use code
        "financing_stage": "", # use code
        "company_scale": "", # use code

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
```

### 2. 修改 filter_rule :
    在 rules() 方法会返回一个 Rule 列表，
    每个 Rule 内的 key_word 会用来搜索招聘信息,
    Rule 内的 rules 是一个函数列表，爬到的招聘信息会用rules里面的函数过滤一次，rules里面的函数都接收一个Work对象包含了一份工作的信息（薪水，发布时间，公司，发布时间，联系人等），
    函数通过对Work对象包含的信息做判断，返回True则表示通过过滤，否则反之。


### 3. 运行 main.py

代码还算规整，所以如果你想在这个代码上做些修改使之更符合自己的需求也是很好改滴
