#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW12_3
# 229223 Sec 002
import copy

def main():
    print(subset_sum({1, 2, 3}))

def subset_sum(set_a):
    s = [set()]
    result = []
    for element in set_a:
        # new_set = s.copy()
        new_set = copy.deepcopy(s)
        for e in new_set:
            e.add(element)
        s += new_set

    return s
        

def test_subset_sum() :
    assert subset_sum({1, 2, 3}) == [0, 1, 2, 3, 3, 4, 5, 6]
    print("All OK!!")

if __name__ == "__main__":
    main()



