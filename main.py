from em import EM
from dataset import Dataset
from reader import Reader

# d = []
# with open('in2.txt', 'r') as file:
#     lines = file.readlines()
#     for l in lines:
#         d.append(l[:-1])
#
# dataset = Dataset(d)
# em = EM(dataset, 2)
# em.do()

if __name__ == "__main__":
    d = Reader.read('./download')
    dataset = Dataset(d)
    for i in range(1, 10):
        em = EM(dataset, i)
        em.do()
        # TODO zapis wyników

    pass