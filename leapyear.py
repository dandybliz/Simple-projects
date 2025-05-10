#Leap Year (tahun kabisat)

def main():
    year = int(input("Please input a year:  ")) 
    if year % 4 == 0: #1. cek apakah year % 4 = 0 ? kalau != 0 langsung gugur bukan kabisat
        if year % 100 == 0 : #2. Setelah True year % 4 = 0
            #masuk ke cek 2 : year % 100 = 0 ? Jika True masuk ke cek ketiga
            #jika year % 100 != 0 maka langsung kabisat
            if year % 400 == 0: #3. cek ketiga, setelah cek ke 2 True cek ke 3 harus True
                #jika ingin kabisat
                print ("That's a leap year!")
            else :
                print ("That's not a leap year.")
        else :
                print ("That's a leap year.") 
    else :
        print ("That's not a leap year.")
main()