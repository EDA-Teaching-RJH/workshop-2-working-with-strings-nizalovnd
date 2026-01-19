def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    #print(pounds)
    #print(percent)
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    pounds_float = float(d[1:])
    return pounds_float

def percent_to_float(p):
    percent_float = float(int(p[:-1])/100)
    return percent_float

main()
