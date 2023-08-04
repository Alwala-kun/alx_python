def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    best_key = None
    best_value = 0

    for key,value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value
            
    return best_key


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
    
    
        