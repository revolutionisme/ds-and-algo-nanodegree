def sqrt(number):
   
   """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
   """
   if number < 0 :
       print("Number must be greater than 0")
       return None
   
   elif number in (0,1):
      return number 

   guess = float(number/2)
   square_root = 0.0
   i = 0
   while (square_root != guess):
      square_root =  (guess + (float(number)/guess)) * 0.5  # Using newton-raphson method 
      if (square_root == guess):
         return int(square_root)
      else:
         guess = square_root
         square_root = 0.0

   

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(35)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass\n" if  (None == sqrt(-1)) else "Fail\n")


print ("Pass" if  (3 == sqrt_new(9)) else "Fail")
print ("Pass" if  (0 == sqrt_new(0)) else "Fail")
print ("Pass" if  (4 == sqrt_new(16)) else "Fail")
print ("Pass" if  (1 == sqrt_new(1)) else "Fail")
print ("Pass" if  (5 == sqrt_new(27)) else "Fail")
print ("Pass" if  (5 == sqrt_new(35)) else "Fail")
print ("Pass" if  (1 == sqrt_new(2)) else "Fail")
print ("Pass" if  (None == sqrt_new(-1)) else "Fail")