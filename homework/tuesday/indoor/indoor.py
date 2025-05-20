def main():
    # get input from user
    user_input = input("Write something: ")
    #return user_input
    # parse the input to indoor
    output = indoor(user_input)
    # print the returned value of indoor
    print(output)
    

def indoor(str):
    user_input = str.lower()
    return user_input 

main()