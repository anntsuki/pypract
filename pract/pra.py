class Time:
    def __init__(self, hours, minutes, seconds):
        self.hour = hours
        self.minute = minutes
        self.second = seconds

    def hours(self):
        return self.hour

    def minutes(self):
        return self.minute

    def seconds(self):
        return self.second

    def __add__(self, other):
        second = self.second + other.second
        minute = self.minute + other.minute
        hour = self.hour + other.hour

        if second >= 60:
            second -= 60
            minute += 1

        if minute >= 60:
            minute -= 60
            hour += 1

        return Time(hour, minute, second)

    def __sub__(self, other):
        second = self.second - other.second
        minute = self.minute - other.minute
        hour = self.hour - other.hour

        if second < 0:
            second += 60
            minute -= 1

        if minute < 0:
            minute += 60
            hour -= 1

        return Time(hour, minute, second)


t1 = Time(1, 20, 30)
t2 = Time(0, 30, 15)
t3 = t1 + t2
print(t1.hours())
