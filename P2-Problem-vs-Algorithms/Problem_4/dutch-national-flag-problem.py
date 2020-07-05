def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    zeroes, ones, twos = [], [], []
    
    for num in input_list:
        if num == 0:
            zeroes.append(num)
        elif num == 1:
            ones.append(num)
        elif num == 2:
            twos.append(num)
        else:
            raise ValueError(f"Invalid number {num}, the input list should contain only 0,1 or 2")
    
    return zeroes + ones + twos

def test_function(test_case):
    sorted_array = sort_012(test_case)
    #print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function("Testcase 0", [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function("Testcase 1", [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function("Testcase 2", [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function("Testcase 3", [0])
test_function("Testcase 4", [])
test_function("Testcase 5", [0,1,2,3])   # should raise valuerror