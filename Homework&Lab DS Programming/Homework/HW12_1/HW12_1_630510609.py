#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW12_1 
# 229223 Sec 002

def main():
    # test_nth_term()
    print(nth_term(1000))

def nth_term(n):
    # set variable
    result = 0
    i = 0

    # loop until n less than or equal 0
    while n > 0:
        # 2 evenly divided, last is 7
        if n % 2 == 0:
            result += 7 * (10**i)
            n = (n//2) - 1
        # 2 not evenly divided, last is 6
        else:
            result += 6 * (10**i)
            n = n//2
        i += 1
    return result


def test_nth_term():
    assert nth_term(3) == 66
    assert nth_term(16) == 6667
    assert nth_term(1000) == 777767667
    print("All OK!!!!")

if __name__ == "__main__":
    main()
