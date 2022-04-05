import os


bad_words = []

def bad_words_list() :
    bad_words_file = open(os.path.dirname(os.path.abspath(__file__)) + '/words/bad_words.txt', 'r')
    for item in bad_words_file.readlines() :
        item = item.strip()
        bad_words.append(item)
    bad_words_file.close
    
    return bad_words

