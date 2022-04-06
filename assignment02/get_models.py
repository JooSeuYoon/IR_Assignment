import get_words
from collections import defaultdict

class get_models:

    def make_boolean_model(words_list, operators_list):
        invert_result = get_words.invert_index.movie_dict()
        boolean_model = defaultdict(dict)
        boolean_result = {}
        movie_names = get_words.invert_index.movie_names()
        boolmodel = 0
        
        for words in words_list :
            if words.split(' ')[0] == 'not' :
                if words.split(' ')[1] in invert_result.keys() :
                    for mvName in movie_names : 
                        if mvName in invert_result[words.split(' ')[1]] : 
                            if invert_result[words.split(' ')[1]][mvName] < 1 :
                                boolmodel = 1
                            else:
                                boolmodel = 0
                            boolean_model[words.split(' ')[1]][mvName] = boolmodel
                        else :
                            boolmodel = 1
                            boolean_model[words.split(' ')[1]][mvName] = boolmodel
                else : 
                    boolmodel = 1
                    boolean_model[words.split(' ')[1]] = {mvName : boolmodel}
            else :
                for mvName in movie_names : 
                    if words in invert_result.keys() : 
                        if mvName in invert_result[words].keys() : 
                            if invert_result[words][mvName] < 1 :
                                boolmodel = 0
                            else : 
                                boolmodel = 1
                            boolean_model[words][mvName] = boolmodel
                        else :
                            boolmodel = 0
                            boolean_model[words][mvName] = boolmodel
                    else :
                        boolmodel = 0
                        boolean_model[words][mvName] = boolmodel
                    

        #result 만들기 operators list로

        boolean_result = boolean_model.copy()

        i = 0
        for i in range(len(operators_list)):
            if operators_list[i] == 'and' :
                for mvName in movie_names:
                    if (boolean_model[list(boolean_model)[i]][mvName] == 1 and boolean_model[list(boolean_model)[i + 1]][mvName] == 1) :
                        boolean_model[list(boolean_model)[i + 1]][mvName] = 1
                    else :
                        boolean_model[list(boolean_model)[i + 1]][mvName] = 0
            elif operators_list[i] == 'or' :
                for mvName in movie_names:
                    if (boolean_model[list(boolean_model)[i]][mvName] == 1 or boolean_model[list(boolean_model)[i + 1]][mvName] == 1) :
                        boolean_model[list(boolean_model)[i + 1]][mvName] = 1
                    else :
                        boolean_model[list(boolean_model)[i + 1]][mvName] = 0
        
        return boolean_model, boolean_result

    def make_vector_space_model():
        
        vector_space_model = {}

        return vector_space_model