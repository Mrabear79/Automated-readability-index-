import math

file_name = input("whats the name of the file?")
file = open(file_name, 'r+')
words_sentences = str('num_of_words')

text = ("string of text as user input")
words = file.read().split()
file.close()
file = open(file_name, 'r+')
sentences = file.read()


def count_letters(words):
    count = 0
    for word in words:
        count += len(word)
    return count


def count_words(words):
    return len(words)


def count_sentences(sent):
    count = 0
    count += sent.count(".")
    count += sent.count("!")
    count += sent.count("?")
    return count

ARI = math.ceil(4.71*(count_letters(words)/count_words(words))+0.5*(count_words
                (words)/count_sentences(sentences))-21.43)
print(ARI)
