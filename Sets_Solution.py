#Problem 1: Hashing 
#This function is complete, use as a reference only if you have completed the solution or are stuck.  
def hash_strings(strings):
    count_strings = {}
    for s in strings:
        if s in count_strings:
            count_strings[s] += 1
        else: 
            count_strings[s] = 1 
    return count_strings


#Test Problem 1: Hashing 

strings = ['Hyacinth', 'Tulip', 'Iris', 'Daffodil', 'Peony']
result = hash_strings(strings) 
assert result == {'Hyacinth': 1, 'Tulip': 1, 'Iris': 1, 'Daffodil': 1, 'Peony': 1}



#Problem 2: Union 
#This function is complete, use as a reference only if you have completed the solution or are stuck. 

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)


#Test Problem 2: Union
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, 9, 10]
result = union(list1, list2) 
assert result == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



#Problem 3: Intersection 
#This function is complete, use as a reference only if you have completed the solution or are stuck.  

def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)


#Test Problem 3: Intersection 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, 9, 10]
result = intersection(list1, list2) 
assert result == {4, 5}