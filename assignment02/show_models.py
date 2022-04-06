import plotly.graph_objects as go
import get_models

#def make_table(user_words_list, operator_list):
    



def main() :
    user_operator_list = []
    user_words_list = []
    user_query = input("Input your word with query.\n(Ex. yellow AND white)\nQuery : ")
    print("\n If you input wrong query program cannot make table.")

    user_query = user_query.split(" ")
    i = 0
    while i < len(user_query) :
        if user_query[i].lower() == 'and' or user_query[i].lower() == 'or' : 
            user_operator_list.append(user_query[i].lower())
        elif user_query[i].lower() == 'not' :
            user_words_list.append(user_query[i].lower() +" "+ user_query[i+1].lower())
            i += 1
        else : 
            user_words_list.append(user_query[i].lower())
        i+=1
    print(get_models.get_models.make_boolean_model(user_words_list, user_operator_list))
    

if __name__ == "__main__":
    main()