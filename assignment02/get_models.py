import get_words

bad_words_list =  get_words.get_words.bad_words_list()

class get_models:

    def make_boolean_model(movie_name, genre):
        movie_dict = get_words.get_words.movie_dict(genre).get(movie_name)
        boolean_model = {}

        for bad_word in bad_words_list :
            if bad_word in movie_dict.keys():
                boolean_model[bad_word] = 1
            else :
                boolean_model[bad_word] = 0
        
        return boolean_model

    def make_boolean_model(movie_name, genre):
        movie_dict = get_words.get_words.movie_dict(genre).get(movie_name)
        vector_space_model = {}

        print(type(movie_dict))
        for bad_word in bad_words_list :
            if bad_word in movie_dict.keys():
                vector_space_model[bad_word] = movie_dict[bad_word]
            else :
                vector_space_model[bad_word] = 0
        
        return vector_space_model