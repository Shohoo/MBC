from em import EM
from dataset import Dataset
from reader import Reader

d = []
with open('in2.txt', 'r') as file:
    lines = file.readlines()
    for l in lines:
        d.append(l[:-1])

dataset = Dataset(d)
em = EM(dataset, 2)
em.do()

d = Reader.read('./../Robot/download')
dataset = Dataset(d)
for i in range(10):
    em = EM(dataset, 2)
    em.do()
    # TODO zapis wyników

pass