#Leap Year (tahun kabisat)

def main():
    year = int(input("Please input a year:  ")) 
    if year % 4 == 0: # 1st check if input is leap year
        if year % 100 == 0 : # 2nd check if input is leap year and evenly divided by 100
            if year % 400 == 0: #3rd if 2nd check is True then go here
                print ("That's a leap year!")
            else :
                print ("That's not a leap year.")
        else :
                print ("That's a leap year.") 
    else :
        print ("That's not a leap year.")
main()