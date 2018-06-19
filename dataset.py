# import pylab
import math


class Dataset:
    def __init__(self, data, data_names):
        self.data = data
        self.data_names = data_names
        self.dic = None
        self.d = None
        self.vec_l = None
        self.n = None

        self._prepare_d()

    def _prepare_d(self):
        self.n = len(self.data)
        tmp = set()
        for x in self.data:
            # words = x.split()
            words = x
            tmp |= set(words)
        tmp = sorted(tmp)
        self.dic = {tmp[i]: i for i in range(len(tmp))}
        self.words = tmp
        self.vec_l = len(self.dic)

        self.d_bool = []
        for x in self.data:
            # words = x.split()
            words = x
            tmp = [0 for i in range(self.vec_l)]
            for w in words:
                tmp[self.dic[w]] = 1
            self.d_bool.append(tmp)

        tf = [[self.data[i].count(self.words[j]) / len(self.data[i]) for j in range(self.vec_l)]for i in range(self.n)]

        n = [0 for i in range(self.vec_l)]
        for d in self.d_bool:
            for j in range(self.vec_l):
                n[j] += d[j]
        idf = [math.log(self.n / n[j]) for j in range(self.vec_l)]

        self.d = []
        for i in range(self.n):
            tmp = [tf[i][j] * idf[j] for j in range(self.vec_l)]
            self.d.append(tmp)

        # pylab.figure(1)
        # pylab.scatter([int(i[0]) for i in self.d], [int(i[1]) for i in self.d])
        # pylab.show()
        pass
