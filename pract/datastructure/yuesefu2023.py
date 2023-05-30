def yuesefu(n, m):  # n个人站成一圈，从第一个人报数，1,2,3...,m；第m个出列，打印出列人顺序（编号）
    peoples = [i + 1 for i in range(n)]
    chulie = []
    index = m - 1  # 出列人的下标索引
    for i in range(n):
        e = peoples.pop(index)  # 出队，删除
        chulie.append(e)  # 加入出队序列
        if i == n - 1:
            break
        index += m - 1
        if index > len(peoples) - 1:  # 下标超出index的范围，回头从0开始
            index = index % len(peoples)  # 要思考下边界问题
    print(chulie)


yuesefu(10, 3)
