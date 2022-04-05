import plotly.graph_objects as go

def make_table(genre, user_movie_list):
    

def main() :
    user_answer = ''
    user_answer_movie_count = 0
    genre = ''
    user_movie_list = []


    while not(genre=='romance' or genre =='crime'):
        genre = input("Input genre of movie.\n Enter (romance or crime)\nGenre : ")
        

    while isinstance(user_answer_movie_count, int) :
        user_answer_movie_count = input("Input how many movies you want to see table.\nMovies count : ")
        if(user_answer_movie_count == 0):
            print("If you don't want to see table, please enter the '.'.")
            if(user_answer=='.'):
                exit
        

    for i in range(int(user_answer_movie_count)):
        movie_name = input("Movie " + str(i + 1) + " Name : ")
        user_movie_list.append(movie_name.replace(' ', '-'))
        
    print("If you answered wrong Movie name, program will not show the table of that movie.")

    

if __name__ == "__main__":
    main()