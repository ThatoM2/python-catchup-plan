def list_animals(animals):
    lst = ''
    for i in range(animals):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst