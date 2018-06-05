from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from bs4 import BeautifulSoup
import requests

class Extractor:
    # @staticmethod
    # def extract_to_file(url, file):
    #     with open(file, 'wb') as file:
    #         r = requests.get(url=url, verify=False)
    #         html = r.text
    #         soup = BeautifulSoup(html)
    #         # kill all script and style elements
    #         for script in soup(["script", "style"]):
    #             script.extract()  # rip it out
    #         data = soup.body.get_text()
    #         t = word_tokenize(data)
    #         file.write(str(t).encode())

    @staticmethod
    def extract(file, is_html):
        with open(file, 'r') as file:
            data = file.read()
            if is_html:
                soup = BeautifulSoup(data)
                for script in soup(["script", "style"]):
                    script.extract()
                data = soup.body.get_text()
            t = word_tokenize(data)
            t_set = set(t)
            # TODO remove special chars and maybe single chars, 's, '' etc
            t_set = Simplifier.remove_single(t_set)
            t_set_s = Extractor.simplify(t_set)
            t_set_s = Simplifier.remove_single(t_set_s)

            return t_set_s

    @staticmethod
    def simplify(t_set):
        tags = pos_tag(t_set)
        tmp = set([])
        for tag in tags:
            word = tag[0].lower()
            wn_tag = Simplifier.penn_to_wn(tag[1])
            s_word = WordNetLemmatizer().lemmatize(word, wn_tag)
            print(word + "---> " + s_word)
            tmp |= set([s_word])
        return tmp


class Simplifier:
    @staticmethod
    def remove_single(t_set):
        tmp = t_set.copy()
        for s in t_set:
            if not len(s) > 1:
                tmp -= set([s])
        return tmp

    @staticmethod
    def is_noun(tag):
        return tag in ['NN', 'NNS', 'NNP', 'NNPS']

    @staticmethod
    def is_verb(tag):
        return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    @staticmethod
    def is_adverb(tag):
        return tag in ['RB', 'RBR', 'RBS']

    @staticmethod
    def is_adjective(tag):
        return tag in ['JJ', 'JJR', 'JJS']

    @staticmethod
    def penn_to_wn(tag):
        if Simplifier.is_adjective(tag):
            return wn.ADJ
        elif Simplifier.is_noun(tag):
            return wn.NOUN
        elif Simplifier.is_adverb(tag):
            return wn.ADV
        elif Simplifier.is_verb(tag):
            return wn.VERB
        return wn.NOUN


if __name__ == "__main__":
    # Extractor.extract_to_file('http://www.ox.ac.uk/', 'ex.txt')
    print(Extractor.extract('./../q.html'))
