def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        print(f"Warning: Input list is empty or None")
        return (None, None)

    for index, val in enumerate(ints):
        if index == 0 :
            minimum = val
            maximum = val
        else:
            if val < minimum:
                minimum = val
            if val > maximum:
                maximum = val

    return (minimum, maximum)

## Example Test Case of Ten Integers
import random

test_case_0 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_case_0)

print ("Pass" if ((0, 9) == get_min_max(test_case_0)) else "Fail")

test_case_1 = [-4,2,5,1,-10,42,123]
print ("Pass" if ((-10, 123) == get_min_max(test_case_1)) else "Fail")

test_case_2 = []
print ("Pass" if ((None, None) == get_min_max(test_case_2)) else "Fail")

test_case_3 = [1]
print ("Pass" if ((1, 1) == get_min_max(test_case_3)) else "Fail")

test_case_4 = None
print ("Pass" if ((None, None) == get_min_max(test_case_4)) else "Fail")