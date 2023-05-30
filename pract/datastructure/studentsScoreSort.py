#  用list存储学生对象，调用sort函数，将其按照某种属性排序（更加一般的排序方法）

class Student():
    def __init__(self, id, name1, yw1, sx1):
        self.ID = id
        self.name = name1
        self.yw = yw1
        self.sx = sx1
        self.zcj = self.yw + self.sx


std1 = Student(1, 'Zhang', 87, 93)
std2 = Student(2, 'Chen', 85, 87)
std3 = Student(3, 'Li', 75, 68)
std4 = Student(4, 'Wu', 90, 65)
std5 = Student(5, 'Gu', 82, 89)
a = [std1, std2, std3, std4, std5]
for std in a:
    print(std.ID, std.name, std.yw, std.sx, std.zcj)
a.sort(key=lambda x: x.zcj, reverse=True)
print('---------------------------')
for std in a:
    print(std.ID, std.name, std.yw, std.sx, std.zcj)


class Student():
    def __init__(self, id, name1, yw1, sx1):
        self.ID = id
        self.name = name1
        self.yw = yw1
        self.sx = sx1
        self.zcj = self.yw + self.sx


std1 = Student(1, 'zhang', 85, 90)
# print(std1.zcj)
std2 = Student(2, 'wang', 87, 91)
std3 = Student(3, 'chen', 90, 78)
std4 = Student(4, 'li', 76, 81)

a = [std1, std2, std3, std4]
std = Student(5, 'zhou', 89, 67)
a.append(std)
for std in a:
    print(std.ID, std.name, std.yw, std.sx, std.zcj)
print("-----------------------------")

a.sort(key=lambda x: x.zcj, reverse=True)
for std in a:
    print(std.ID, std.name, std.yw, std.sx, std.zcj)
