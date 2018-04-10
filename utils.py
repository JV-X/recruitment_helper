def log(msg):
    print(msg)
    with open('log.txt', 'a',encoding="utf-8") as f:
        f.write("\r{}".format(msg))
