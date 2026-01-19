def verify():
    age = float(input("Please enter your age:"))

    if age >= 18:
        print("You are an adult")
    
    elif age < 18:
        print("You are a child")
    

if __name__ == "__main__":
    verify()