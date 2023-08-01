def no_c(my_string):
    string_list = list(my_string)
    #print(string_list)
    for letter in string_list:
        if letter == 'c' or letter == 'C':
            string_list.remove(letter)

    new_string =  "".join(string_list)
    return new_string

#print(no_c("HecllCo"))
#print(no_c("Holberton School"))
#print(no_c("Chicago"))
#print(no_c("C is fun!"))

