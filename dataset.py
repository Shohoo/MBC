import pylab

class Dataset:
    def __init__(self, data):
        self.data = data
        self.dic = None
        self.d = None
        self.vec_l = None
        self.n = None

        self._prepare_d()

    def _prepare_d(self):
        self.n = len(self.data)
        tmp = set()
        for x in self.data:
            words = x.split()
            tmp |= set(words)
        tmp = sorted(tmp)
        self.dic = {tmp[i]: i for i in range(len(tmp))}
        self.vec_l = len(self.dic)

        self.d = []
        for x in self.data:
            words = x.split()
            tmp = [0 for i in range(self.vec_l)]
            for w in words:
                tmp[self.dic[w]] = 1
            self.d.append(tmp)

        # pylab.figure(1)
        # pylab.scatter([int(i[0]) for i in self.d], [int(i[1]) for i in self.d])
        # pylab.show()
        pass
