def mutate_string(string, position, character):
    string = str(string)
    character = str(character)
    
    new_string = string[:position] + character + string[position+1:]
    return new_string

