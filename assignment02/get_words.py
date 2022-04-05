import os
import re

class invert_index:
    def get_stop_words():
        stopwords = {}
        stopword_file = open(os.path.dirname(os.path.abspath(__file__)) + '/words/stop_words.txt')
        for stop_word in stopword_file.readlines():
            stopwords[stop_word[0:len(stop_word)-1]] = 1
        return stopwords

    def movie_dict():
        invert_result = {}
        
        for mvName in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/movies') : 
                script_terms = {}
                if(mvName != '.DS_Store') :
                    mvName = mvName[0:len(mvName) - 4]
                    script_file = open(os.path.dirname(os.path.abspath(__file__)) + '/movies/' + mvName + '.txt', 'r')
                    print("Movie <" + mvName.replace('-',' ') + "> Invert Indexing ... ")

                    script_file = open(os.path.dirname(os.path.abspath(__file__)) + '/movies/' + mvName + '.txt', 'r')
                   
                    for script_line in script_file.readlines():
                        if(script_line != ''):
                            for word in re.split('[\s+\d`_,.?!&//@$#*:;()"\'\- ]', script_line) :
                                word = word.lower()
                                if (word not in invert_index.get_stop_words()) :
                                    if(word not in script_terms.keys()) :
                                        script_terms.update({word : 1})
                                    else :
                                        script_terms[word] += 1
                    for word in script_terms.keys() : 
                        invert_result[word] = {mvName : 0}
                        if word in invert_result.keys() :
                            invert_result[word][mvName] += 1
                        else : 
                            invert_result.update({word : {mvName : script_terms[word]}})             
                    script_file.close()
        invert_result = sorted(invert_result)
        return invert_result
        