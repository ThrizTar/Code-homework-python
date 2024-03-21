#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab12_2 
# 229223 Sec 002

def main():
    # test_matching_sum()
    print(matching_sum((10, -1 ,1, -8, 3, 1), 2))

def matching_sum(t, target_value):
    # create dict
    matching_dict = {}

    # find matching element in t
    for element in t:
        matching = target_value - element
        if matching in matching_dict:
            return [element, matching_dict[matching]]
        else:
            matching_dict[element] = element

    # no matching 
    return []


def test_matching_sum():
    assert matching_sum((1,), 1) == []
    assert matching_sum((5, 2), 7) == [[5, 2], [2, 5]]
    assert matching_sum((10, -1 ,1, -8, 3, 1), 2) == [[10, -8], [-8, 10], [-1, 3], [1, 1]]
    assert matching_sum((10, -1, 1, -1, -8, 3, 1), 10) == []
    print("All OK!!!!")

if __name__ == "__main__":
    main()