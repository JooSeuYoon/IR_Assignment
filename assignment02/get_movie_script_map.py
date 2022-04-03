import os
import re

crime_movie = {}
romance_movie = {}

def movie_list(genre):
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

print((movie_list("romance").keys()))