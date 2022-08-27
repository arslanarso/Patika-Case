from datetime import datetime as dt

GLOBAL_HISTORY = []

class Car(object):
    def __init__(self,fname=None,lname=None,hgs_number=None,balance=None):
        self.fname = fname
        self.lname = lname
        self.hgs_number = hgs_number
        self.balance = balance
        self.history = []
    
    def pass_through_hgs(self):
        if float(self.balance) > float(self.price) or float(self.balance) == float(self.price):
            self.balance = float(self.balance) - float(self.price)
        else:
            # allow negative values
            self.balance = float(self.balance) - float(self.price)
        
        self.history.append(dt.now())
        GLOBAL_HISTORY.append(self)
        print(f"[+] HGS Number {self.hgs_number} {self.fname} {self.lname} passing through with car type of {self.__class__.__name__} paying {self.price}, final balance is {self.balance}")


class Otomobile(Car):
    def __init__(self, **kwargs):
        self.price = 10
        super(Otomobile, self).__init__(**kwargs)

class Minibus(Car):
    def __init__(self, **kwargs):
        self.price = 20
        super(Minibus, self).__init__(**kwargs)

class Otobus(Car):
    def __init__(self, **kwargs):
        self.price = 30
        super(Otobus, self).__init__(**kwargs)


def report_all():
    global GLOBAL_HISTORY
    objectives = {}
    for p in GLOBAL_HISTORY:
        for sub in p.history:
            day = f"{sub.year}:{sub.month}:{sub.day}"
            if day in objectives.keys() and type(objectives[day]) == dict:
                if p.price in objectives[day].keys():
                    objectives[day][p.price] += p.balance
                else:
                    objectives[day][p.price] = p.balance

            else:
                objectives[day] = dict()
                if p.price in objectives[day].keys():
                    
                    objectives[day][p.price] += p.balance
                else:
                    objectives[day][p.price] = p.balance
                    
    print("\n\nFinal Report")
    print("Day\t\tClass\t\tFinal Balance")     
    for day in objectives.keys():
        for k in objectives[day].keys():
            clss = "Otomobile"
            if k == 20:
                clss = "Minibus"
            elif k == 30:
                clss = "Otobus"
            print(str(day)+"\t\t"+clss+"\t\t"+str(objectives[day][k]))
        
if __name__ == "__main__":
        
    m1 = Minibus(fname="Arslan",lname="Tek",hgs_number=333333,balance=200)
    m2 = Minibus(fname="Arslan",lname="Arso",hgs_number=222222,balance=100)
    o1 = Otomobile(fname="veli",lname="melih",hgs_number=4444444,balance=100)
    o2 = Otomobile(fname="Samet",lname="Arslan",hgs_number=5555555,balance=3)
    mb1 = Otobus(fname="Doğancan",lname="güneş",hgs_number=6666666,balance=30000)
    mb2 = Otobus(fname="Nazan",lname="Belma",hgs_number=7777777,balance=300)

    m1.pass_through_hgs()
    m2.pass_through_hgs()
    m1.pass_through_hgs()
    o1.pass_through_hgs()
    mb1.pass_through_hgs()
    mb1.pass_through_hgs()
    mb2.pass_through_hgs()
    o1.pass_through_hgs()
    m2.pass_through_hgs()
    o2.pass_through_hgs()
    mb1.pass_through_hgs()
    mb1.pass_through_hgs()
    mb1.pass_through_hgs()

    report_all()