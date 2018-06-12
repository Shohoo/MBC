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
    d = Reader.read('./download')
    dataset = Dataset(d)
    lh = {}
    for i in range(2, 10):
        em = EM(dataset, i, 0.0000000000000001)
        em.do()
        # TODO zapis wyników
        lh[i] = em.likelyhood
        pass
    for l in lh:
        print(str(l) + ': ' + str(lh[l]))
    pass