import os
import re

class invert_index:
    def get_stop_words():
        stopwords = {}
        stopword_file = open(os.path.dirname(os.path.abspath(__file__)) + '/words/stop_words.txt')
        for stop_word in stopword_file.readlines():
            stopwords[stop_word[0:len(stop_word)-1]] = 1
        return stopwords

    def movie_dict(movie_name):
        try:
            script_file = open(os.path.dirname(os.path.abspath(__file__)) + '/movies/' + movie_name + '.txt', 'r')
            script_words = {}
            
            for script_line in script_file.readlines():
                if(script_line != ''):
                    for word in re.split('[\s+\d`_,.?!&//@$#*:;()"\'\- ]', script_line) :
                        word = word.lower()
                        if (word not in invert_index.get_stop_words()) :
                            if(word not in script_words) :
                                script_words[word] = 1
                            else :
                                script_words[word] += 1
            script_words = sorted(script_words.items())
            script_file.close()
            return script_words
        except:
            print("execption error")
    
    def get_all_movies():
        movie_terms = {}
        try:
            for mvName in os.listdir('movies/') : 
                if(mvName != '.DS_Store') :
                    mvName = mvName[0:len(mvName) - 4]
                    print('Invert Indexing movie  ' + mvName.replace('-',' '))
                    movie_terms[mvName] = invert_index.movie_dict(mvName)
            return movie_terms
        except:
            print("exception error")
