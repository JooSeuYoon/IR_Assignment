import plotly.graph_objects as go
import get_models
import get_words

def make_boolean_model_table(user_query):
    user_operator_list = []
    user_words_list = []
    table_query = user_query
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
    
    boolean_model, boolean_result = get_models.get_models.make_boolean_model(user_words_list, user_operator_list)
    
    headerList = ["Movie Name"]
    for word in user_words_list:
        headerList.append(word)
    headerList.append(table_query)
    
    cellList = []

    cellList.append(get_words.invert_index.movie_names())

    for key in boolean_model.keys():
        cellList.append(list(boolean_model[key].values()))
    
    cellList.append(list(boolean_result[list(boolean_result)[len(boolean_result) - 1]].values()))
            

    fig = go.Figure(data=[go.Table(
        header=dict(values = headerList,
                    line_color = 'white',
                    fill_color = 'yellow',
                    align = 'center'),
        cells=dict(values = cellList,
                    line_color = 'white',
                    fill_color = 'white',
                    align = 'center'))
    ])

    fig.update_layout(width=1000,height=400)
    fig.show()
    



def main() :
    user_query = input("Input your word with query.\n(Ex. yellow AND white)\nQuery : ")
    print("\n If you input wrong query program cannot make table.")

    make_boolean_model_table(user_query)
    




if __name__ == "__main__":
    main()