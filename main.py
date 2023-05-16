import datetime


class Time(datetime.time):

    def __sub__(self, other):
        return datetime.timedelta(hours=self.hour - other.hour, minutes=self.minute - other.minute,
                                  seconds=self.second - other.second)


class Client:

    def __init__(self, name: str, surname: str, personal_code: str, phone_number: str | int):
        self.name = name
        self.surname = surname
        self.personal_code = personal_code
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname} ({self.personal_code}, {self.phone_number})"


class BeautyProcedure:

    def __init__(self, category: str = None, name: str = None, discount: str = None, price: int | float = None,
                 client: Client = None, date: datetime.date = None, start_time: Time = None,
                 end_time: Time = None, time_isable: bool = True):
        self.category = category
        self.name = name
        self.discount = discount
        self.price = price
        self.client = client
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.time_isable = time_isable

    @property
    def duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time

    @property
    def total_price(self):
        if self.discount and self.price:
            discount = int(self.discount.split('%')[0]) / 100
            return self.price - self.price * discount

    def info(self):
        return (f"Category: {self.category}\n"
                f"Name: {self.name}\n"
                f"Client: {str(self.client)}\n"
                f"Date: {self.date.strftime('%d.%m.%Y')}"
                f" from {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}\n"
                f"Duration: {self.duration}\n"
                f"Price: {self.price}\n"
                f"Discount: {self.discount}\n"
                f"Total price: {self.total_price}\n")

    def print_info(self):
        print(self.info())

    def client_info(self):
        return str(self.client)

    def print_client_info(self):
        print(self.client_info())


c1 = BeautyProcedure('a', 'b', '10%', 40, Client('ila', 'Chap', '281005-21423', '27823867'), datetime.date.today(),
                     Time(20, 47), Time(23, 00))
c1.print_info()
