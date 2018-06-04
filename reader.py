import os
from extracting import Extractor


class Reader:
    @staticmethod
    def read(dir):
        counter = 0
        d = []
        for root, directories, filenames in os.walk(dir):
            for filename in filenames:
                if '.html' in filename:
                    counter += 1
                    path = os.path.join(root, filename)
                    print(path)
                    terms = Extractor.extract(path)
                    d.append(terms)
        print(counter)
        return d


if __name__ == "__main__":
    Reader.read('./../Robot/8')