import numpy as np
import get_words
from collections import defaultdict
import copy

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

        boolean_result = copy.deepcopy(boolean_model)

        i = 0
        for i in range(len(operators_list)):
            if operators_list[i] == 'and' :
                for mvName in movie_names:
                    if (boolean_model[list(boolean_model)[i]][mvName] == 1 and boolean_model[list(boolean_model)[i + 1]][mvName] == 1) :
                        boolean_result[list(boolean_model)[i + 1]][mvName] = 1
                    else :
                        boolean_result[list(boolean_model)[i + 1]][mvName] = 0
            elif operators_list[i] == 'or' :
                for mvName in movie_names:
                    if (boolean_model[list(boolean_model)[i]][mvName] == 1 or boolean_model[list(boolean_model)[i + 1]][mvName] == 1) :
                        boolean_result[list(boolean_model)[i + 1]][mvName] = 1
                    else :
                        boolean_result[list(boolean_model)[i + 1]][mvName] = 0
        
        return boolean_model, boolean_result

    def make_vector_space_model(query_list):
        try:
        
            mvNameList = get_words.invert_index.movie_names()

            movie_term_list = get_words.invert_index.movie_dict()
            tf = {str : {str : int}}
            df = {str : int}
            idf = {str : float}
            weight = {str : {str : float}}
            
            cosine_score = {str : {str : float}}
            cosine_score["score"] = {}

            #document frequency & inverse
            #term freauency & normalize 
            for term in query_list:
                df[term] = 0
                tf[term] = {}
                if(term in movie_term_list.keys()):
                    for mvName in mvNameList :
                        if(mvName in movie_term_list[term].keys()) :
                            df[term] += 1
                            tf[term][mvName] = movie_term_list[term][mvName]
                        else :
                            tf[term][mvName] = 0
                        cosine_score["score"][mvName] = 0
                #inverse 구하기
                idf[term] = np.log10(len(mvNameList) / df[term]) 
            
            #TF.IDF Weighting
            for term in query_list :
                weight[term] = {}
                for mvName in mvNameList :
                    weight[term][mvName] = tf[term][mvName] * idf[term]
                    weight[term][mvName] = int(weight[term][mvName] * 1000)/1000
                
            for term in query_list :
                for mvName in mvNameList:
                    cosine_score["score"][mvName] += int(weight[term][mvName] * sum(weight[term].values()) / len(mvNameList) * 1000)/ 1000
 
        except:
            print("There's no word in document.")
        return tf, weight, cosine_score