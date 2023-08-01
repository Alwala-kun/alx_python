def no_c(my_string):
    string_list = list(my_string)
    #print(string_list)
    string_list = [letter for letter in my_string if letter not in ('c', 'C')]

    new_string =  "".join(string_list)
    return new_string

print(no_c("HellcCcccooccoscccss"))
#print(no_c("Holberton School"))
#print(no_c("Chicago"))
#print(no_c("C is fun!"))

