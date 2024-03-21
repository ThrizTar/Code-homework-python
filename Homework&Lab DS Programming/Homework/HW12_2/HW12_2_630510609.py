#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW12_2 
# 229223 Sec 002

def main():
    # test_median_of_median()
    # print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]))
    # print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    print(median_of_median([28, 28, 27, 28, 28, 28, 28, 28, 28, 29]))

def my_min_mid_max(a , b , c):
    min = a
    mid = b
    max = c

    if(min < max):
        if(min < mid):
            if(mid < max):
                pass
            else:
                keep_max = max
                max = mid
                mid = keep_max
        else:
            keep_min = min
            min = mid
            mid = keep_min
    else:
        keep_max0 = max
        max = min
        min = keep_max0

        if(min < mid):
            if(mid < max):
                min = min
                mid = mid
                max = max
            else:
                keep_max1 = max
                max = mid
                mid = keep_max1
        else:
            keep_min = min
            min = mid
            mid = keep_min
    return mid

def median_of_median(list_a):
    lenght_of_list_a = len(list_a)
    if lenght_of_list_a <= 3:
        if lenght_of_list_a == 3:
            a = list_a[0]
            b = list_a[1]
            c = list_a[2]
            mid = my_min_mid_max(a, b, c)
            return mid
        
        elif lenght_of_list_a == 2:
            return sum(list_a)/2
        
        else:
            return list_a[0]
        
    else:
        medians = []
        split_num = lenght_of_list_a//3

        first_part = list_a[:split_num]
        second_part = list_a[split_num:split_num*2]
        last_part = list_a[split_num*2:]
        all_part = first_part, second_part, last_part
        
        for i in all_part:
            median = median_of_median(i)
            medians.append(median)
    return median_of_median(medians)
    
    

def test_median_of_median():
    assert median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]) == 21.0
    print("All OK!!!")

if __name__ == "__main__":
    main()