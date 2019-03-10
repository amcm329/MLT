import operator

def split_data(filename = "Melate.csv"):

    file_handler = open(filename)
    lines = file_handler.readlines()[1:]
    file_handler.close()

    lista_0 = []
    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []

    for line in lines:
        if line != "\n":
           splitted_line = line.split(",")
           lista_0.insert(0,splitted_line[2])
           lista_1.insert(0,splitted_line[3])
           lista_2.insert(0,splitted_line[4])
           lista_3.insert(0,splitted_line[5])
           lista_4.insert(0,splitted_line[6])
           lista_5.insert(0,splitted_line[7])
           lista_6.insert(0,splitted_line[8])

    return lista_0,lista_1,lista_2,lista_3,lista_4,lista_5,lista_6


def get_frequencies(my_list):
    dictionary = {}    
    for element in my_list:
        if element in dictionary:
           dictionary[element] += 1 

        else:
           dictionary[element] = 1 
 
    return dictionary 


def get_frequencies_of_differences(my_list):
    dictionary = {}

    for x in range (1,len(my_list)):
        difference = int(my_list[x]) - int(my_list[x-1])
        if difference in dictionary:
           dictionary[difference] += 1
        else: 
           dictionary[difference] = 1
    
    return dictionary


def deja_vu(mi_lista,elemento):
    otra_lista = []
    lista_auxiliar = []
    for otro_elemento in mi_lista:
        if otro_elemento == elemento:
           #print(lista_auxiliar)
           otra_lista.append(lista_auxiliar)
           lista_auxiliar = []

        else:
           lista_auxiliar.append(otro_elemento)

    return otra_lista
 

#Suppose that X is the most frequent number at a certain position
#then you check the last number Y appeared
#and you must find Z that completes the chain X,Y,Z because it would be the next number.
def find_patterns(my_list,ordered_frequencies): 
    final_patterns = []
    final_differences = []
    last_element = my_list[-1]
    most_frequent_element = ordered_frequencies[-1][0]
    #print my_list
    #print most_frequent_element
    
    for x in range (2,len(my_list)):
        if my_list[x-1] == last_element :#and my_list[x-2] == most_frequent_element:
            #CAMBIO FINAL DIFFERENCES
           if my_list[x] not in final_patterns: 
              final_differences.append((my_list[x-2],my_list[x-1],my_list[x],int(my_list[x]) - int(my_list[x-1])))
              final_patterns.append(my_list[x])
    
    for x in range (len(final_patterns)):
        final_patterns[x] = int(final_patterns[x])
                    
                    
    return final_differences,sorted(final_patterns)


def print_elements(patterns,frequencies):
    final_list = []
    list_only_numbers = []
    only_numbers = patterns[1]
    selected_numbers_with_differences = patterns[0]
    
    for element in selected_numbers_with_differences:
        final_list.append([element[0],element[1],element[2],element[3],int(frequencies[element[3]])])
    
    numbers_with_differences_in_order = sorted(final_list,key=operator.itemgetter(4))
    
    for element in numbers_with_differences_in_order:
        list_only_numbers.append(element[2])
     
    #cambiar para nuevo metodo
    print("Ordered Frequencies: " + str(sorted(frequencies.items(), key=operator.itemgetter(1))))
    print("Numbers w. Differences in Order: " + str(numbers_with_differences_in_order))
    print("Numbers: " + str(list_only_numbers))  
    #return list_only_numbers