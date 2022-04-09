import show_models


def main() :
    user_option = input("Which model want to see? (1. Boolean Model 2. Vecter Space Model)\nAnswer : ")

    if(user_option == '1') :
        user_query = input("Input your word with query.\n(Ex. yellow AND white)\nQuery : ")
        print("\nIf you input wrong query program cannot make table.\n")

        show_models.make_boolean_model_table(user_query)
    elif(user_option == '2') :

        user_query = input("Input your query with 3 words.\n(Ex. love peace green)\nQuery : ")

        show_models.make_vector_space_model_table(user_query)


if __name__ == "__main__":
    main()