Using Newton raphson method to initialize with a best guess and then repeat until you get the value. 

Time Complexity:
O((logn)F(n)) - where n is the digit precision in the input number and F(n) is the cost of calculating f(x)/f'(x) with n-digit precision. Referred from - https://en.citizendium.org/wiki/Newton's_method#Computational_complexity

Space Complexity:
O(1) - No new space added