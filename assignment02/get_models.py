import get_words

class get_models:

    def make_boolean_model(words_list, operators_list):
        invert_result = get_words.invert_index.movie_dict()
        boolean_model = {str : {}}
        boolean_result = {}
        movie_names = get_words.invert_index.movie_names()
        
        for words in words_list :
            if words.split(' ')[0] == 'not' :
                if words.split(' ')[1] in invert_result.keys() :
                    for mvName in movie_names : 
                        boolmodel = {mvName : 0}
                        if invert_result[words.split(' ')[1]][mvName] < 1 :
                            boolmodel = {mvName : 1}
                        else:
                            boolmodel = {mvName : 0}
                        boolean_model[words] = boolmodel
                    
            else :
                for mvName in movie_names : 
                    if words in invert_result.keys() : 
                        if invert_result[words][mvName] < 1 :
                            boolmodel = {mvName : 0}
                        else : 
                            boolmodel = {mvName : 1}
                    else :
                        boolmodel = {mvName : 0}

                    boolean_model[words] = boolmodel

        #result 만들기 operators list로
        

        return boolean_model

    def make_vector_space_model():
        
        vector_space_model = {}

        return vector_space_model