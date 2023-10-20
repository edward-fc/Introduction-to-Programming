"""
Introduction to Programming Coursework 1

@author:Edward Falkner-Carter
"""


def valid_puzzle(Input_list):
    """This function takes one argument puzzle which is a list of strings with more than one item. 
    This function returns Boolean True if the puzzle is valid and Boolean False otherwise. 
    A valid puzzle contains strings of equal length. 
    For example, given the following three puzzles, puzzle1 is valid whilst puzzle2 
    (not all strings are the same length), puzzle3 (contain item that is not a string), 
    and puzzle4 (not a list) are invalid. 
    The strings in the puzzle are case insensitive. 
    """

    #Verify that The variable Input_list is a list

    if type(Input_list) != list:
        return False
    #Initialize Variable length
    length = len(Input_list[0])

    #For every element in Input_list, we compare the length of each string
    for element in Input_list:
        if length != len(element):
            return False

    return True


def similarity_grouping(Input_list):
    """This function takes a list and returns a list with items of same value in the same sublist. 
    The sublists should be returned in the order of each element's first appearance in the given list. 
    Return an emptylist if data is not a list. Note that ‘a’, and “a” are considered as the same. 
    Also, integer 1 is considered the same as ‘1’ or “1”. """

    #Verify that The variable Input_list is a list
    if type(Input_list) != list:
        return False
    # Initialize the variable Results
    results = []
    # For every element in Input_list, we compare each element to see if there are similar or not
    for element in Input_list:
        #Intiliaze the variable new_element
        new_element = True

        for i in range(len(results)):

            if element == results[i][0]:

                results[i].append(element)
                new_element = False

        if new_element:
            results.append([element])
    #Return a list with sublist conatining identical items
    return results


def highest_count_items(Input_list):
    """This function returns a list for item(s) with highest count in data. 
    Each item in data is commaseparated. The returned list is in the format [[item, count]]. 
    If there is a tie, return all items with thehighest count 
    (i.e., [[item1, count], [item2, count], etc...]). 
    Return an empty list if data is not a string."""

    #Verify that The variable Input_list is a list

    if not(type(Input_list) == str):
        return []

    #Initilize the variables Grouped_list and String and max

    Grouped_list = []
    max = [["", 0]]
    string = ""

    #1st Step Formating Data into a list

    for i in range(len(Input_list)):

        if Input_list[i] == ",":

            Grouped_list.append(string)
            string = ""

        elif Input_list[i] != " ":

            string += Input_list[i]

    Grouped_list.append(string)

    # 2nd Step: Use similarity_grouping to regroup similar items

    Grouped_list = similarity_grouping(Grouped_list)

    # 3rd Step: Find largest set of items in Grouped_list
    
    for element in Grouped_list:

        if max[0][1] <= len(element):

            max.insert(0, [element, len(element)])

        else:
            max.append([element, len(element)])

    # 4th Step: Check for duplicates

    results = [[max[0][0][0], max[0][1]]]

    for i in range(1, len(max)):

        if results[0][1] == max[i][1]:

            results.append([max[i][0][0], max[i][1]])

        else:
            return results


def valid_char_in_string(poplist, charset):
    results = True
    count = 0
    if type(charset) != list:
        return False
    for element_poplist in poplist:
        for i in range(len(element_poplist)):
            for y in range(len(charset)):
                if element_poplist[i] != charset[y]:
                    count += 1
                    if count == len(charset):
                        results = False
            count = 0
    return results


def total_price(Units):
    price = 0
    while Units:
        if Units >= 6:
            Units -= 6
            price += 5
        elif Units >= 1:
            Units -= 1
            price += 1.25
    if price > 20:
        price *= 0.9
    return price
  


if __name__ == "__main__":
    # sample test for task 1.1
    
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))
    
    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))
    
    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))
    
    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))
   
    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
    
