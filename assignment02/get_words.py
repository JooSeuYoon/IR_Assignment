import os
import re

crime_movie = {}
romance_movie = {}

class get_words:

    def movie_dict(genre):

        words_dict = {}

        for mvName in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/inspect_movie_scripts/'+genre+'_movies'):
            if(mvName != '.DS_Store') :
                mvFile = open(os.path.dirname(os.path.abspath(__file__)) + '/inspect_movie_scripts/'+genre+'_movies/'+mvName, 'r')
                for item in mvFile.readlines() :
                    item = item.strip()
                    words = re.split('/', item)
                    if(len(words[0]) > 0) :
                        #(globals()['{}_movie'.format(genre)]) = {(mvName[10:len(mvName)-4]): {words[0] : int(words[1])}}
                        words_dict[words[0]] = int(words[1])
                globals()["{}_movie".format(genre)][mvName[10:len(mvName)-4]] = words_dict        
                mvFile.close()
        return globals()["{}_movie".format(genre)]

    def bad_words_list() :
        bad_words = []
        bad_words_file = open(os.path.dirname(os.path.abspath(__file__)) + '/words/bad_words.txt', 'r')
        for item in bad_words_file.readlines() :
            item = item.strip()
            bad_words.append(item)
        bad_words_file.close
    
        return bad_words
