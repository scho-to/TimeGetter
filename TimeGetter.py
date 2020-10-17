class Time():
    def __init__(self, **kwargs):
        self.day = self.check_arg(kwargs, "day")
        self.month = self.check_arg(kwargs, "month")
        self.year = self.check_arg(kwargs, "year")
        self.hour = self.check_arg(kwargs, "hour")
        self.minute = self.check_arg(kwargs, "minute")
        self.second = self.check_arg(kwargs, "second")
    
    def set_time(self, **kwargs):
        self.__init__(**kwargs)
        
    def check_arg(self, var, key):
        if key in var:
            if key in ["hour", "minute", "second"] and int(var[key]) < 10:
                var[key] = "0" + str(var[key])
            else:
                var[key] = str(var[key])
            return var[key]
        else:
            return "00"
    
    def get_value(self, key):
        time_as_dict = self.get_as_dict()
        return int(time_as_dict[key])
    
    def get_as_dict(self):
        d = {}
        d["day"] = self.day
        d["month"] = self.month
        d["year"] = self.year
        d["hour"] = self.hour
        d["minute"] = self.minute
        d["second"] = self.second
        return d
        
    def get_time_as_string(self):
        return f'{self.hour}:{self.minute}:{self.second}'
        
    def __str__(self):
        return f"{self.day}-{self.month}-{self.year} {self.hour}:{self.minute}:{self.second}"

class TimeGetter():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def get_between(self):
        time_between = Time()
        second_between = self.get_time_between(
            self.start.get_value("second"),
            self.end.get_value("second")
        )
        minute_between = self.get_time_between(
            self.start.get_value("minute"),
            self.end.get_value("minute")
        )
        hour_between = self.get_time_between(
            self.start.get_value("hour"),
            self.end.get_value("hour"),
            23
        )
        time_between.set_time(
            second=second_between,
            minute=minute_between,
            hour=hour_between
        )
        return time_between
    
    def get_time_between(self, v1, v2, maxVal = 59):
        elapsed = 0
        while v1 != v2:
            if(v1 == maxVal):
                v1 = 0
            else:
                v1 = v1+1
            elapsed = elapsed + 1
        return elapsed

time1 = Time(
    day=7,
    month=9,
    year=2020,
    hour=21,
    minute=14,
    second=38
)
time2 = Time(
    day=8,
    month=9,
    year=2020,
    hour=4,
    minute=4,
    second=36
)

print(time1)
print(time2)
tg = TimeGetter(time1, time2)
time_between = tg.get_between()
print(time_between.get_time_as_string())

#07.09.2020 21:14:38,12
#Ende 08.09.2020  4:04:36,59