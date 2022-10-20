import datetime as dt
class Record:
    def __init__(self, amount, commint, date = None):
        self.amount = amount
        self.commint = commint
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()

class Calculator(Record):
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, new_record):
        self.records.append(new_record)
    def get_today_stats(self):
        today_amount = 0
        today = dt.date.today
        for Record in self.records:
            if Record.date==today:
                today_amount += Record.amount
        return today_amount
    def get_week_stats(self):
        today = dt.date.today
        date7 = today - dt.timedelta(days=7)
        week_amount=0
        for Record in self.records:
            if Record.date >= today and Record.date <= date7:
                week_amount += Record.amount
        return week_amount

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remained = Calculator.self.limit - Calculator.get_today_stats
        return remained

class CashCalculator(Calculator):
    def get_cach_remained(self, currency):
        remained = self.limit - self.get_today_stats()
        text = ""
        USD_RATE = 60.03
        EURO_RATE = 59.87
        if currency == "eur":
            remained = remained / EURO_RATE
        elif currency == "usd":
            remained = remained / USD_RATE
        if remained > 0:
            text = "У вас осталось еще " + str(remained) + " " + currency
        elif remained < 0:
            text = "Денег нет: ваш долг " + str(remained / -1) + " " + currency
        else:
            text = "Денег нет"
            return text


cash_calculator = CashCalculator(1000)

print(cash_calculator.get_today_cash_remained("rub"))
