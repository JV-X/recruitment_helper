class Work:
    def __init__(self):
        self.company = ""
        self.title = ""
        self.salary = ()
        self.url = ""
        self.time = ""
        self.rules = None

    def __repr__(self):
        return "{} {} {} {} {} ".format(self.time, self.salary, self.company, self.title, self.url)
