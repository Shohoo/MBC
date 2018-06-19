import math
import numpy
import sys
import random

from dataset import Dataset

class EM:
    def __init__(self, dataset, k, epsilon):
        self.dataset = dataset
        self.vec_l = dataset.vec_l
        self.k = k
        self.epsilon = epsilon
        self.n = dataset.n
        self.c = None
        self.lam = None
        self.pwkdi = None
        self.d = None

        self._prepare()

    def _prepare(self):
        self.c = []
        self.lam = []
        self.d = [numpy.array(d) for d in self.dataset.d]
        self.pwkdi = [[0 for i in range(self.n)] for k in range(self.k)]

        for k in range(self.k):
            self.c.append(self.d[random.randint(0, self.n - 1)])
            self.lam.append(1 / self.k)
        # self.c = [[0, 1], [1, 0]]
        # self.lam = [0.45, 0.55]
        pass

    def pxwk(self, i, k):
        t1 = self.d[i] - self.c[k]
        t2 = (numpy.linalg.norm(self.d[i] - self.c[k]))
        t3 = math.exp(-(numpy.linalg.norm(self.d[i] - self.c[k]) ** 2))
        t4 = 1 / math.sqrt(2 * math.pi)
        val = 1 / math.sqrt(2 * math.pi) * math.exp(-(numpy.linalg.norm(self.d[i] - self.c[k]) ** 2))
        return val

    def e(self):
        lamr = [x for x in self.lam]
        for k in range(self.k):
            for i in range(self.n):
                m = lamr[0] * self.pxwk(i, 0)
                for j in range(1, self.k):
                    pxwk = self.pxwk(i, j)
                    m += lamr[j] * pxwk
                if m == 0:
                    self.pwkdi[k][i] = 0.
                else:
                    self.pwkdi[k][i] = lamr[k] * self.pxwk(i, k) / m

    def m(self):
        for k in range(self.k):
            self.lam[k] = (1 / self.n) * sum(self.pwkdi[k])
            val = self.pwkdi[k][0] * self.d[0]
            for i in range(1, self.n):
                val += self.pwkdi[k][i] * self.d[i]
            self.c[k] = val / sum(self.pwkdi[k])

    def step(self):
        self.e()
        self.m()
        # pxwk = [[self.pxwk(i, k) for k in range(self.k)] for i in range(self.n)]
        # print(pxwk)

        pass

    def do(self):
        pre_val = sys.maxsize
        while True:
            self.step()
            tmp = []
            for i in range(self.n):
                val = sum([self.lam[k] * self.pxwk(i,k) for k in range(self.k)])
                if val == 0:
                    tmp.append(0)
                else:
                    tmp.append(math.log(val))
            val = -sum(tmp)
            print(val)
            print(self.lam)
            if (pre_val - val) <= self.epsilon:
                self.likelyhood = val
                break
            pre_val = val

        docs = {}
        for i in range(self.n):
            s = ''
            tmp = [self.pxwk(i, k) for k in range(self.k)]
            max_arg = numpy.argmax(tmp)
            max_p = tmp[max_arg]
            tmp_s = ' '.join([str(t) for t in tmp])
            if max_arg not in docs:
                docs[max_arg] = []
            docs[max_arg].append([i, self.dataset.data_names[i], max_arg, max_p])
            # s = 'dok: ' + str(i) + ' ' + self.dataset.data_names[i] + ' : p: ' + str(max_p) + ' : ' + str(max_arg) + ': ' + tmp_s
            # print(s)
        print(docs)
