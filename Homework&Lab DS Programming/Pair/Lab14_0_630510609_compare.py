#!/usr/bin/env python3
# Krittamet Thaijaroen # Maytaporn Mueykumnerd
# 630510609 # 631610317
# HW01_1
# 229223 Sec 002

from math import sqrt

def main():
    print(count_segment([(2, 7, 1.5), (3.2, 2.5, 4.06), (-5.5, -4.5, 2.5), (2, -5.2, 3), (7.2, -2.8, 1.2)]))

def count_segment(list_a):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for row in range(len(list_a)):
        x = list_a[row][0]
        y = list_a[row][1]
        r = list_a[row][2]
        r = abs(r)
        d = sqrt(x**2 + y**2)
        
        if x > 0:
            # maxima segment of one circle is 4 by default
            if y > 0:
                q1 += 1
                # (r > x)
                if r > x:
                    q2 += 1
                # comapare between y and r if (r > y)
                if r > y:
                    q4 += 1
                # r > d
                if r > d:
                    q3 += 1
                

            elif y < 0: 
                q4 += 1
                if r > abs(x): # x > 0 อยู่แล้วไม่ต้องใส่ abs ก็ได้
                    q3 += 1
                if r > abs(y):
                    q1 += 1
                if r > d:
                    q2 += 1
            # เช็ค x > 0 and y = 0
            '''
            else:
                if r <= x:
                    q1 += 1
                    q4 += 1
                if r > x:
                    q1 += 1
                    q4 += 1
                    q2 += 1
                    q3 += 1
            '''

        elif x < 0:
            if y > 0:
                q2 += 1
                if r > x: # x < 0 ใส่ abs ด้วย
                    q1 += 1
                if r > y:
                    q3 += 1
                if r > d:
                    q4 += 1
            elif y < 0: 
                q3 += 1
                if r > abs(x):
                    q4 += 1
                if r > abs(y):
                    q2 += 1
                if r > d:
                    q1 += 1
            # เช็ค x < 0 and y = 0
            '''
            else:
                if r <= abs(x):
                    q2 += 1
                    q3 += 1
                if r > abs(x):
                    q1 += 1
                    q4 += 1
                    q2 += 1
                    q3 += 1
            '''
        # in y-axis circle can intersect to another quadrant. (when x == 0)
        elif x == 0: # ใส่เป็น else ได้
            if y == 0:
                q1 += 1
                q2 += 1
                q3 += 1
                q4 += 1 

            elif y > 0:
                # + q1 , q2 แค่ตอนที่ r <= y
                q1 += 1 
                q2 += 2 # บวกแค่ 1 ก็พอ
                if r > d:# x = 0 แล้ว d = y^2 เช็คแค่ r > y ก็ได้ แล้วมันก็จะ บวกทุก q
                    q3 += 1
                    q4 += 1
            elif y < 0:# ใส่เป็น else ได้
                # + q3 , 4 แค่ตอนที่ r <= abs(y)
                q3 += 1
                q4 += 1
                if r > d:# x = 0 แล้ว d = y^2 เช็คแค่ r > y ก็ได้ แล้วมันก็จะ บวกทุก q
                    q1 += 1
                    q2 += 2 # บวกแค่ 1 ก็พอ

        # อันนี้เช็คใน if ก่อนหน้าหมดแล้ว
        ''' 
        # in x-axis (when y == 0)
        elif y == 0: 
            # when radius is more that distance between origin point (0, 0) and center of circle (x, y)
            if x > 0:
                q1 += 1
                q4 += 1
                if r >d:
                    q3 += 1
                    q2 += 1
            elif x < 0:
                q2 += 1
                q3 += 1
                if r > d:
                    q1 += 1
                    q4 += 1
        '''
    return (q1, q2, q3, q4)


if __name__ == "__main__":
    main()
