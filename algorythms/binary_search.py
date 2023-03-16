
def binary_search(input_:list,el_to_find:int)-> int:
    '''
    Makes binary_search for a digit inside a list
    :param input_:
    :param el_to_find:
    :return:position (index) in sorted array
    '''
    input =input_.copy()
    input=sorted(input)

    low=0
    high=len(input)-1
    if el_to_find == low:
        return 0
    elif el_to_find == high:
        return (len(input)-1)
    else:
        while high>=low:
            position=(high+low)//2
            if el_to_find==input[position]:
                return position
            elif el_to_find < input[position]:
                high = position-1
            else:
                low=position+1






#log^n checkings are needed. The time complexity of binary search algorithm is O(log n), where n is the size of the input array.
