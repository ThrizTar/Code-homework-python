#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab14_1
# 229223 Sec 002
import copy

def main():
    test_remove_row_col()
    # print(remove_row_col([[2, 3, 4, 5], 
    #                         [8, 7, 6, 5], 
    #                         [0, 1, 2, 3]],
    #                         3,-5))


def remove_row_col(list_a, row, col):
    new_list = copy.deepcopy(list_a)
    
    if abs(row) <= len(new_list):
        if row < 0 :
            row += len(new_list)
        if row < len(new_list):
            del new_list[row]
        if abs(col) <= len(new_list[0]):
            if col < 0:
                col += len(new_list[0])
            for rows in range(len(new_list)):
                for cols in range(len(new_list[rows])):
                    if cols == col:
                        del new_list[rows][cols]
                    else:
                        continue
    else:
        if abs(col) <= len(new_list[0]):
            if col < 0:
                col += len(new_list[0])
            for rows in range(len(new_list)):
                for cols in range(len(new_list[rows])):
                    if cols == col:
                        del new_list[rows][cols]
                    else:
                        continue
    return new_list

# both del: row+ col+ -> row < len(list_a) and col < len(list_a[0])
# both del: row+ col- -> row < len(list_a) and abs(col) <= len(list_a[0])
# both del: row- col+ -> abs(row) <= len(list_a) and col < len(list_a[0])
# both del: row- col- -> abs(row) <= len(list_a) and abs(col) <= len(list_a[0])

# del col only: row+ col+ -> row >= len(list_a) and col < len(list_a[0])
# del col only: row+ col- -> row >= len(list_a) and abs(col) <= len(list_a[0])
# del col only: row- col+ -> abs(row) > len(list_a) and col < len(list_a[0])
# del col only: row- col- -> abs(row) > len(list_a) and abs(col) <= len(list_a[0])

# del row only: row+ col+ -> row < len(list_a) and col >= len(list_a[0])
# del row only: row+ col- -> row < len(list_a) and abs(col) > len(list_a[0])
# del row only: row- col+ -> abs(row) <= len(list_a) and col >= len(list_a[0])
# del row only: row- col- -> abs(row) <= len(list_a) and abs(col) > len(list_a[0])

# can't del botH: row+ col+ -> row >= len(list_a) and col >= len(list_a[0]) 
# can't del botH: row+ col- -> row >= len(list_a) and abs(col) > len(list_a[0]) 
# can't del botH: row- col+ -> abs(row) > len(list_a) and col >= len(list_a[0]) 
# can't del botH: row- col- -> abs(row) > len(list_a) and abs(col) > len(list_a[0]) 

def test_remove_row_col():
    # both del: row+ col+ -> row < len(list_a) and col < len(list_a[0])
    print("test 1")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            1,3) ==  [[2, 3, 4], 
                                    [0, 1, 2]]
    
    # both del: row+ col- -> row < len(list_a) and abs(col) <= len(list_a[0])
    print("test 2")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            1,-4) == [[3, 4, 5], 
                                    [1, 2, 3]]
    
    print("test 3")
    # both del: row- col+ -> abs(row) <= len(list_a) and col < len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -3,2) ==  [[8, 7, 5], 
                                        [0, 1, 3]]
    
    print("test 4")
    # both del: row- col- -> abs(row) <= len(list_a) and abs(col) <= len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -3,-4) ==  [[7, 6, 5], 
                                        [1, 2, 3]]
    
    print("test 5")
    # del col only: row+ col+ -> row >= len(list_a) and col < len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            3, 3) ==  [[2, 3, 4], 
                                        [8, 7, 6],
                                        [0, 1, 2]]
    
    print("test 6")
    # del col only: row+ col- -> row >= len(list_a) and abs(col) <= len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            3, -4) ==  [[3, 4, 5], 
                                        [7, 6, 5],
                                        [1, 2, 3]]

    print("test 7")
    # del col only: row- col+ -> abs(row) > len(list_a) and col < len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4, 3) ==  [[2, 3, 4], 
                                        [8, 7, 6],
                                        [0, 1, 2]]

    print("test 8")
    # del col only: row- col- -> abs(row) > len(list_a) and abs(col) <= len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4,-4) ==  [[3, 4, 5], 
                                        [7, 6, 5], 
                                        [1, 2, 3]]

    print("test 9")
    # del row only: row+ col+ -> row < len(list_a) and col >= len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            2,4) ==  [[2, 3, 4, 5], 
                                    [8, 7, 6, 5]]

    print("test 10")
    # del row only: row+ col- -> row < len(list_a) and abs(col) > len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            2,-5) ==  [[2, 3, 4, 5], 
                                    [8, 7, 6, 5]]

    print("test 11")
    # del row only: row- col+ -> abs(row) <= len(list_a) and col >= len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -3,4) ==  [[8, 7, 6, 5], 
                                        [0, 1, 2, 3]]

    print("test 12")
    # del row only: row- col- -> abs(row) <= len(list_a) and abs(col) > len(list_a[0])
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -3,-5) ==  [[8, 7, 6, 5], 
                                        [0, 1, 2, 3]]

    print("test 13")
    # can't del botH: row+ col+ -> row >= len(list_a) and col >= len(list_a[0]) 
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            3, 4) ==  [[2, 3, 4, 5], 
                                        [8, 7, 6, 5], 
                                        [0, 1, 2, 3]]

    print("test 14")
    # can't del botH: row+ col- -> row >= len(list_a) and abs(col) > len(list_a[0]) 
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            3, -5) ==  [[2, 3, 4, 5], 
                                        [8, 7, 6, 5], 
                                        [0, 1, 2, 3]]

    print("test 15")
    # can't del botH: row- col+ -> abs(row) > len(list_a) and col >= len(list_a[0]) 
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4, 4) ==  [[2, 3, 4, 5], 
                                        [8, 7, 6, 5], 
                                        [0, 1, 2, 3]]

    print("test 16")
    # can't del botH: row- col- -> abs(row) > len(list_a) and abs(col) > len(list_a[0]) 
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4, -5) ==  [[2, 3, 4, 5], 
                                        [8, 7, 6, 5], 
                                        [0, 1, 2, 3]]


    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            1,2) ==  [[2, 3, 5], 
                                        [0, 1, 3]]
    
    print("test 17")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            1,-3) == [[2, 4, 5], 
                                        [0, 2, 3]]
    
    print("test 18")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -1,2) ==  [[2, 3, 5], 
                                        [8, 7, 5]]
    
    print("test 19")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -1,-2) ==  [[2, 3, 5], 
                                        [8, 7, 5]]
    
    print("test 20")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -3,-4) ==  [[7, 6, 5], 
                                        [1, 2, 3]]
    
    print("test 21")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4,-4) ==  [[3, 4, 5], 
                                        [7, 6, 5], 
                                        [1, 2, 3]]
    
    print("test 22")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4, 2) ==  [[2, 3, 5], 
                                        [8, 7, 5],
                                        [0, 1, 3]]
    
    print("test 23")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            3,-5) ==  [[2, 3, 4, 5], 
                                        [8, 7, 6, 5], 
                                        [0, 1, 2, 3]]
    
    print("test 24")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -3,-5) ==  [[8, 7, 6, 5], 
                                        [0, 1, 2, 3]]
    
    print("test 25")
    assert remove_row_col([[2, 3, 4, 5],
                           [8, 7, 6, 5]],
                           1,1) == [[2,4,5]]
    
    print("test 26")
    assert remove_row_col([[1,2,3],
                           [4,5,6]],
                           0,-9) == [[4,5,6]]
    
    print("test 27")
    assert remove_row_col([[1,2,3],
                           [4,5,6]],
                           -4,0) == [[2,3],[5,6]]
    
    print("test 28")
    assert remove_row_col([[1,2,3],
                           [4,5,6]],
                           0,3) == [[4,5,6]]
    
    print("test 29")
    assert remove_row_col([[2, 3, 4, 5], 
                            [8, 7, 6, 5], 
                            [0, 1, 2, 3]],
                            -4,-5) ==  [[2, 3, 4, 5], 
                                        [8, 7, 6, 5], 
                                        [0, 1, 2, 3]]
    
    print("test 30")
    assert remove_row_col([[1,2,3],[4,5,6]],0,0) == [[5, 6]]

    print("test 31")
    assert remove_row_col([[1,2,3],[4,5,6]],2,3) == [[1,2,3],[4,5,6]]
 
    print("All OK!!")

if __name__ == "__main__":
    main()
