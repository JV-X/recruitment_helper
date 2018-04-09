class Work:
    def __init__(self):
        self.company = ""
        self.job = ""
        self.salary = ()
        self.url = ""
        self.time = ""

    def __repr__(self):
        return "{} {} {} {} {} ".format(self.time, self.salary, self.company, self.job, self.url)

