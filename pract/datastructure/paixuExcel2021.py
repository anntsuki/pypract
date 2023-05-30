import xlrd
import xlwt


# 定义学生成绩信息类
class Student:
    def __init__(self, id, nm, yw, sx, yy, zh):  # 7个属性
        self.ID = id
        self.name = nm
        self.yw = yw
        self.sx = sx
        self.yy = yy
        self.zh = zh
        # 总成绩属性不需要输入，直接定义属性zcj，并由其他单科成绩计算
        self.zcj = self.yw + self.sx + self.yy + self.zh


def PrintStudents(stdtL):
    for i in stdtL:
        print(i.ID, i.yw, i.sx, i.yy, i.zh, i.zcj)


# 测试数据
if __name__ == '__main__':
    sqlistStudents = []  # 用于存放学生的成绩信息
    # 读取所有学生的成绩信息，在excel表里面，按行逐行读取
    # 将所有学生成绩信息，加入到顺序线性表 sqlistStudents
    nStudents = 60  # 学生的人数
    data = xlrd.open_workbook('ScoreStudents60.xls')  # scoresWenke ：sheet的名字
    table = data.sheets()[0]  # 通过索引顺序获取（只有1个sheet）
    # 以下达到同样的功能
    # table = data.sheet_by_index(0)  # 通过索引顺序获取
    # table = data.sheet_by_name(u'Sheet1')  # 通过名称获取
    for i in range(1, nStudents + 1):
        dataRow = table.row_values(i)  # 读取excel表的第(i+1)行;第1行是表头信息，不需要读取
        student = Student(i, dataRow[0], dataRow[1], dataRow[2], dataRow[3], dataRow[4])
        sqlistStudents.append(student)

    print("成绩排序前")
    PrintStudents(sqlistStudents)  # 成绩排序前打印，与excel表对应，检验程序的正确性

    # 数据写入到excel表格；创建workbook（其实就是excel，后来保存一下就行），用于存放排序后的结果
    workbook = xlwt.Workbook(encoding='ascii')
    # 创建表,存放按总成绩排序后的结果ZongChengJi
    worksheet = workbook.add_sheet('sortZongChengJi')

    # 按总成绩排名
    print("总成绩排序后，结果请查看excel表：scoreSortResults.xls")
    sqlistStudents.sort(key=lambda x: x.zcj, reverse=True)  # 排序
    # 总成绩排序后，打印，观察其正确性
    # PrintStudents(sqlistStudents)

    # 往单元格内写入内容；  排序后
    sq = sqlistStudents
    for i in range(len(sq)):
        elem = [sq[i].ID, sq[i].name, sq[i].yw, sq[i].sx, sq[i].yy, sq[i].zh, sq[i].zcj]
        for j in range(7):
            worksheet.write(i, j, elem[j])

    # 创建表,存放按数学排序后的结果
    worksheet = workbook.add_sheet('sortShuXue')
    # 按数学成绩排名
    # print("数学成绩排序后，结果请查看excel表：scoreSortResults.xls")
    sqlistStudents.sort(key=lambda x: x.sx, reverse=True)  # 排序
    # 数学成绩排序后，打印，观察其正确性
    # PrintStudents(sqlistStudents)

    # 往单元格内写入内容；  排序后
    sq = sqlistStudents
    for i in range(len(sq)):
        elem = [sq[i].ID, sq[i].name, sq[i].yw, sq[i].sx, sq[i].yy, sq[i].zh, sq[i].zcj]
        for j in range(7):
            worksheet.write(i, j, elem[j])

    # 保存(不同的排序结果存放在同一个excel里面，但放在不同sheet表里面)
    workbook.save('scoreSortResults2021.xls')

    # 其他排名类似可以做，只需要复制代码，修改函数名和个别语句；请自行完成！
