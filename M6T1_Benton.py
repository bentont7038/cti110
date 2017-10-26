#CTI 110
#M6T1: Kilometer Converter
#Terrel Benton
#10/26/17


def main():
    km_in=float(input("Enter kilometers: "))
    show_miles(km_in)

def show_miles (km):
    miles = km * 0.6214
    print(km, "kilometers is equal to", miles,"miles")


main()
