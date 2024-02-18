import numpy


class PrimeDic:
    def __init__(self):
        self.__dic = {}

    def append(self, key, value):
        if type(key) != numpy.ndarray or len(key) != 4:
            print("not true format")
            return
        key = str(key.tolist())
        self.__dic[key] = max(value, self.__dic.get(key, -1))

    def toList(self):
        res = []
        for i in self.__dic:
            temp = eval(i)
            temp.append(self.__dic[i])
            res.append(temp)
        self.__dic = {}
        return res
