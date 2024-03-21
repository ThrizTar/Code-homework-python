# !/usr/bin/env python3
# Krittamet Thaijaroen (Guitar)
# 630510609
# 229223 sec 2 
# HW11_1

def main():
    display_calendar(2, 1900)   

def display_calendar(month, year):

    # set month
    if month == 1:
        m = 13
        year -= 1
    elif month == 2:
        m = 14
        year -= 1
    else:
        m = month
    # set each variable
    q = 1
    k = year % 100
    j = year // 100

    # formula
    h = ((q + ((13*(m+1)) // 5) + k + (k//4) + (j//4) - (2*j))) % 7
    print("Su Mo Tu We Th Fr Sa")

    if(m == 14 and ((year+1) % 400 == 0 or (year+1) % 4 == 0 and ((year+1) % 100)) != 0):
        if h == 0:
            for i in range(6):
                print("--", end=" ")
        else:
            for i in range(h -1):
                print("--", end=" ")

        i = 1
        while(i < 30):
            if ((h-2) + i) % 7 == 0 and i != 1:
                print()
            if(i < 10):
                print(" %d" %i, end=" ")
            else:
                print("%d" %i, end=" ")
            i += 1
        print("\n")

    elif(m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 or m == 13):
        if h == 0:
            for i in range(6):
                print("--", end=" ") 
        else:
            for i in range(h -1):
                print("--", end=" ")

        i = 1
        while(i < 32):
            if ((h-2) + i) % 7 == 0 and i != 1:
                print()
            if(i < 10):
                print(" %d" %i, end=" ")
            else:
                print("%d" %i, end=" ")
            i += 1
        print("\n")


    elif(m == 4 or m == 6 or m == 9 or m == 11):
        if h == 0:
            for i in range(6):
                print("--", end=" ")
        else:
            for i in range(h -1):
                print("--", end=" ")

        i = 1
        while(i < 31):
            if ((h-2) + i) % 7 == 0 and i != 1:
                print()
            if(i < 10):
                print(" %d" %i, end=" ")
            else:
                print("%d" %i, end=" ")
            i += 1
        print("\n")
    else:
        if h == 0:
            for i in range(6):
                print("--", end=" ")
        else:
            for i in range(h -1):
                print("--", end=" ")

        i = 1
        while(i < 29):
            if ((h-2) + i) % 7 == 0 and i != 1:
                print()
            if(i < 10):
                print(" %d" %i, end=" ")
            else:
                print("%d" %i, end=" ")
            i += 1
        print("\n")

if __name__ == "__main__":
    main() 

