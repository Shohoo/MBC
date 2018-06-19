import os
from extracting import Extractor


class Reader:
    @staticmethod
    def read(dir):
        counter = 0
        d = []
        d_names = []
        for root, directories, filenames in os.walk(dir):
            for filename in filenames:
                if '.html' in filename:

                    path = os.path.join(root, filename)
                    print(path)
                    words = Extractor.extract(path, True)
                    if len(words) > 0:
                        counter += 1
                        d.append(words)
                        d_names.append(path)
        print(counter)
        return [d, d_names]


if __name__ == "__main__":
    Reader.read('./../Robot/8')