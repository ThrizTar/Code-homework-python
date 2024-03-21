#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab14_1
# 229223 Sec 002

def main():
    test_reshape():

def reshape(matrix):
    pass

def test_reshape():
    assert reshape([[2, 3, 4],
                    [1, 2, 3]]) == [[2, 3, 4],
                                    [1, 2, 3]]
    
    assert reshape([[1, 2],
                    [1, 2, 3],
                    [1, 2],
                    [1, 2],
                    [1]]) == [[1, 2, 1, 2], 
                                [3, 1, 2, 1], 
                                [2, 1, 0, 0]]
    
    assert reshape([[1, 2], 
                    [3, 4], 
                    [5, 6]]) == [[1, 2, 3], 
                                [4, 5, 6]]
    
    print("All OK")

if __name__ == "__main__":
    main()