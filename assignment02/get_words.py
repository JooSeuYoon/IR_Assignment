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
        invert_result = {str : {str : int}}
        stopwords = invert_index.get_stop_words()
        
        for mvName in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/movies') : 
                #script_terms = {str : int}
                if(mvName != '.DS_Store') :
                    mvName = mvName[0:len(mvName) - 4]
                    script_file = open(os.path.dirname(os.path.abspath(__file__)) + '/movies/' + mvName + '.txt', 'r')
                    print("Movie <" + mvName.replace('-',' ') + "> Invert Indexing ... ")
                   
                    for script_line in script_file.readlines():
                        if(script_line != ''):
                            for word in re.split('[\s+\d`_,.?!&//@$#*:;()"\'\- ]', script_line) :
                                word = word.lower()
                                if (word not in stopwords) :
                                    if word in invert_result.keys():
                                        if mvName in invert_result[word].keys() :
                                            invert_result[word][mvName] += 1
                                        else :
                                            invert_result[word].update({mvName : 0})
                                    else :
                                        invert_result[word] = {mvName : 1}
                                    
                               
                    script_file.close()
        #invert_result = sorted(invert_result)
        return invert_result

    def movie_names() :
        mvName = []
        for name in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/movies') :
            if name != '.DS_Store' : 
                mvName.append(name[0:len(name) - 4])
        return mvName
        