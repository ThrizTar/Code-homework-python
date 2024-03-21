#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab13_1
# 229223 Sec 002

def main():
    test_matrix_mult()
    # print(matrix_mult([[1, 2, 3],
    #                     [4, 5, 6]], 
    #                     [[7, 8],
    #                     [9, 10],
    #                     [11,12]]))

def matrix_mult(m1, m2):
    result = []
    lenght_row_m1 = len(m1)
    lenght_element_m1 = len(m1[0])

    lenght_col_m2 = len(m2)
    lenght_element_m2 = len(m2[0])

    # Row in m1 != Col in m2 can't calculate
    if lenght_element_m1 != lenght_col_m2:
        return
    else:
        # Create 2D List
        for row in range(lenght_row_m1):
            result += [[0] * lenght_element_m2]

        # Calculate
        for row in range(lenght_row_m1):
            for col in range(lenght_element_m2):
                for element in range(lenght_element_m1):
                    result[row][col] += m1[row][element] * m2[element][col]
        return result


def test_matrix_mult():
    assert matrix_mult([[1, 2, 3],
                        [4, 5, 6]], 
                                    [[7, 8],
                                    [9, 10],
                                    [11,12]]) == [[58, 64],[139, 154]]
    
    assert matrix_mult([[1, 2, 3],
                        [4, 5, 6]],
                                    [[7, 8, 5, 9, 3],
                                    [9, 10, -3, 7, 13],
                                    [11, 12, 6, 2, 9]]) == [[58, 64, 17, 29, 56], [139, 154, 41, 83, 131]]
    
    print("All OK!!!")
    

if __name__ == "__main__":
    main()

