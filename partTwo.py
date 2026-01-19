import math  

def main():
    a = int(input("Enter integer value of side a"))
    b = int(input("Enter integer value of side b"))
    c = pythag(a,b)
    print(f"The length of the hypotenuse is {c}")

def pythag(A,B):
    sqr_a = A**2
    sqr_b = B**2
    sqr_c = sqr_a + sqr_b
    c = math.sqrt(sqr_c)
    return int(c)
main()
