import heapq

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #if not input_list:
    #    print("Warning: No values supplied in the input list")
    #    return []
    
    if len(input_list) <= 1:
        print("Warning: One or less input variables supplied")
        return input_list

    heap = []
    for val in input_list:
        heapq.heappush(heap, -val)
    
    num1 = ""
    num2 = ""

    while len(heap) > 0:
       item =  -heapq.heappop(heap)
       num1 += str(item)

       if len(heap) > 0:
        item =  -heapq.heappop(heap)
        num2 += str(item)
    
    return [int(num1), int(num2)]

def test_function(test_case_txt, test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    #print(output, solution)
    if sum(output) == sum(solution):
        print(f"{test_case_txt} - Pass")
    else:
        print(f"{test_case_txt} - Fail")


test_case0 = [[1, 2, 3, 4, 5], [542, 31]]
test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[], []]
test_case3 = [[0], [0]]
test_case4 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 86420]]

test_function("Testcase 0", test_case0)
test_function("Testcase 1", test_case1)
test_function("Testcase 2", test_case2)
test_function("Testcase 3", test_case3)
test_function("Testcase 4", test_case4)
