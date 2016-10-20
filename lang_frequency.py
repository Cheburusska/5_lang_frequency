import re
from collections import Counter


filepath = ('sample_text/text.txt')


def load_data(filepath):#takes path to the txt file, returns lisf of words in lowercase without punctuation
    with open(filepath, encoding="utf8") as text:
        t = text.read().lower()
        t_list = re.sub("[^\w,-]", " ",  t).split()
        return t_list


def get_most_frequent_words(text): #takes list of words, returns list of 10 most common words
    return Counter(text).most_common(10)


def main(): #prints result in console
    text = load_data(filepath)
    print (get_most_frequent_words(text))


if __name__ == '__main__':
    main()
