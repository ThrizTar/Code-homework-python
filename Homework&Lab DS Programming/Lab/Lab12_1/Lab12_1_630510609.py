#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab12_1 
# 229223 Sec 002

def main():
    test_multiply_polynomials()

def multiply_polynomials(p1, p2):

    # reversr list
    rev_p1 = p1[::-1] 
    rev_p2 = p2[::-1]

    # create dict and set coefficient
    coe_dict = {}
    coe_p1 = 0
    coe_p2 = 0

    # multiply two list
    for x in rev_p1:
        for y in rev_p2:
            if (coe_p1 + coe_p2) not in coe_dict:
                coe_dict[coe_p1 + coe_p2] = (x * y)
            else:
                coe_dict[coe_p1 + coe_p2] += (x * y)
            coe_p2 += 1 
        coe_p2 = 0
        coe_p1 += 1

    # return to result
    keep = list(coe_dict.values())
    result = keep[::-1]
    return result
            


def test_multiply_polynomials():
    assert multiply_polynomials([2, 0, 3], [4, 5]) == [8, 10 ,12, 15]
    print("All OK!!!")

if __name__ == "__main__":
    main()