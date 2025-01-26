def sum_dict_values(dictionary):
    total=0
    for value in dictionary.values():
        total+=value
    return total
    
my_dict={"a":10,"b":20,"c":30}
print("sum of all values : ",sum_dict_values(my_dict))