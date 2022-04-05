import get_movie_script_map
import get_bad_words_map

bad_words_list = get_bad_words_map.bad_words_list()

def make_boolean_model(movie_name, genre):
    movie_dict = get_movie_script_map.movie_dict(genre).get(movie_name)
    vector_space_model = {}

    print(type(movie_dict))
    for bad_word in bad_words_list :
        if bad_word in movie_dict.keys():
            vector_space_model[bad_word] = movie_dict[bad_word]
        else :
            vector_space_model[bad_word] = 0
    
    return vector_space_model

