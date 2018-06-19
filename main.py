from em import EM
from dataset import Dataset
from reader import Reader
from nltk import word_tokenize

# d = []
# with open('in2.txt', 'r') as file:
#     lines = file.readlines()
#     for l in lines:
#         d.append(word_tokenize(l[:-1]))
#
# dataset = Dataset(d)
# em = EM(dataset, 2, 0.0000000000000001)
# em.do()

if __name__ == "__main__":
    [d,d_names] = Reader.read('../ROBOT/64')
    dataset = Dataset(d, d_names)
    lh = {}
    max = 0
    for i in range(5, 6):
        em = EM(dataset, i, 0.0000000000000001)
        em.do()
        # TODO zapis wyników
        lh[i] = em.likelyhood
        pass
    for l in lh:
        print(str(l) + ': ' + str(lh[l]))
    pass