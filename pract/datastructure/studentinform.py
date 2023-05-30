class Student:
    def __init__(self, id, name, yw, sx, yy, zh, zcj):
        self.id = id
        self.name = name
        self.yw = yw
        self.sx = sx
        self.yy = yy
        self.zh = zh
        self.zcj = zcj

    def printall(self):
        print("({0}){1}:{2},{3},{4},{5},{6};".format(self.id, self.name, self.yw, self.sx, self.yy, self.zh, self.zcj))


students = [Student(1, '付霓', 88, 51, 62, 121, 199), Student(2, '罗炜', 93, 30, 30, 121, 161),
            Student(3, '黄恒', 92, 27, 75, 171, 240), Student(4, '李亚男', 92, 43, 80, 153, 235),
            Student(5, '李琦', 82, 61, 72, 143, 223)]
for i in range(5):
    for j in range(5 - i - 1):
        if students[j].yw > students[j + 1].yw:
            tmp = students[j]
            students[j] = students[j + 1]
            students[j + 1] = tmp
for i in range(5):
    students[i].printall()
