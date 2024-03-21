#!/usr/bin/env python3
# เมธาพร เม้ยกำเนิด (เฟรช)
# 631610317
# HW12_1
# 229223 Sec 002

# def main():
#     test_nth_term()

def nth_term(n):
    if n == 1:
        return 6
    elif n == 2:
        return 7
    else:
        binary = bin(n+1)[3:]
        binary = binary.ljust(len(binary), '0')
        binary = binary.replace('0', '6')
        binary = binary.replace('1', '7')
        
        return int(binary)

print(nth_term(1000))

# def test_nth_term():
#     assert nth_term(3) == 66
#     assert nth_term(16) == 6667
#     assert nth_term(1000) == 777767667

# if __name__ == '__main__':
#     main()