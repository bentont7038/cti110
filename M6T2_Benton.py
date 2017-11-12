#CTI 110
#M6T2: Feet tpo inches Converter
#Terrel Benton
#11/11/17

def feet_to_inches (fEet):
    iNches = (fEet * 12)
    return iNches

def main():
    fEet = float(input("Enter the number of feet:"))
    iNches = feet_to_inches (fEet)
    print(fEet,"Feet to inches is",iNches,"inches")

main()
