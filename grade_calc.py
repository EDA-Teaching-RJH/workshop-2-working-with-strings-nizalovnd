def main():
    num_score = float(input("Enter your score between 0 and 100:"))

    try:
        
        if 90 <= num_score <= 100:
            print("You got an A")
        elif 80 <= num_score < 90:
            print("You got an B")
        elif 70 <= num_score < 79:
            print("You got an C")
        elif 60 <= num_score < 69:
            print("You got an D")
        elif 0 <= num_score < 60:
            print("You got an F")
        else:
            raise ValueError
    except ValueError as e:
        print("You have entered a value outside of the required range")

if __name__ == "__main__":
    main()
