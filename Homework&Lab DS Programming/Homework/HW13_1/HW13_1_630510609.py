#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW13_1
# 229223 Sec 002

def main():

    # max_col > row pass
    # square_matrix([[2, 3, 4],
    #                 [1, 2, 3]])
    # '''
    # [[2, 3, 4],
    # [1, 2, 3],
    # [0, 0, 0]]
    # '''

    # max col == row  pass
    # square_matrix([[1, 2],
    #                 [1, 2, 3, 4, 5],
    #                 [1, 2],
    #                 [1, 2],
    #                 [1]])

    # '''
    # [[1, 2, 0, 0, 0],
    # [1, 2, 3, 4, 5],
    # [1, 2, 0, 0, 0],
    # [1, 2, 0, 0, 0],
    # [1, 0, 0, 0, 0]]
    # '''

    # row > min_col pass
    # square_matrix([[2, 3, 4],
    #                 [1, 2, 3], 
    #                 [6, 7]])

    # '''
    # [[2, 3, 4],
    # [1, 2, 3],
    # [6, 7, 0]]
    # '''
    
    # row > max_col pass
    # square_matrix([[1, 2],
    #                 [1, 2, 3],
    #                 [1, 2],
    #                 [1, 2],
    #                 [1]])
    
    # '''
    # [[1, 2, 0, 0, 0],
    # [1, 2, 3, 0, 0],
    # [1, 2, 0, 0, 0],
    # [1, 2, 0, 0, 0],
    # [1, 0, 0, 0, 0]]
    # '''
    pass

def  square_matrix(list_x):
    lenght_of_row = len(list_x)
    keep_max = []
    keep_zero = []

    for row in range(lenght_of_row):
        keep_max.append(len(list_x[row]))
    max_col_of_list_x = max(keep_max)

    # lenght row >= lenght col
    if lenght_of_row >= max_col_of_list_x:
        # add element in col until equal lenght of row
        for row in range (lenght_of_row):
            for col in range (lenght_of_row - len(list_x[row])):
                list_x[row].append(0)

    # lenght col > lenght row
    else:
        # add row and element in col until equal lenght of col
        for row in range (max_col_of_list_x - lenght_of_row):
            for col in range (max_col_of_list_x):
                keep_zero.append(0)
            list_x.append(keep_zero)
            keep_zero = []

if __name__ == "__main__":
    main()
