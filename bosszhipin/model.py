class Work:
    def __init__(self):
        self.company = ""
        self.title = ""
        self.salary = ()
        self.url = ""
        self.time = ""
        self.simple_time = ""
        self.contact = ""
        self.detail = ""
        self.rules = None

    @staticmethod
    def format_time(t):
        r = []

        tmp = t.split(" ")
        r.extend(tmp[0].split("-"))
        r.extend(tmp[1].split(":"))

        return r

    def early_than(self, other):
        # time sample: "2018-04-10 08:04"
        t = Work.format_time(self.time)
        ot = Work.format_time(other.time)

        for index in range(len(t)):
            if int(t[index]) > int(ot[index]):
                return -1

        return 1

    def __repr__(self):
        return "{} {} {} {} {} {} ".format(self.time, self.salary, self.contact, self.company, self.title, self.url)
