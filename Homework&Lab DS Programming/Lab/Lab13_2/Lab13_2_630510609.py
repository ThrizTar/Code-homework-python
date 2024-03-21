#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab13_2
# 229223 Sec 002

def main():
    test_is_magic_square()
    # print(is_magic_square([[4, 9, 8], 
    #                         [11, 7, 3],
    #                         [6, 5, 10]]))
    
def turn_to_int(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            board[row][col] = int(board[row][col])
    return board

def is_magic_square(board):
    # Variable
    board = turn_to_int(board)
    ref = board[0][0]
    lenght_row_board = len(board)
    lenght_col_board = len(board[0])

    sum_vertical = []

    sum_v = 0
    sum_dlr = 0
    sum_drl = 0

    for row in range(lenght_row_board):
        for col in range(lenght_col_board):
            # Element > n**2
            if board[row][col] > lenght_row_board**2:
                return False

    for row in range(lenght_row_board):
        for col in range(lenght_col_board):
            # Check all same element
            if ref == board[row][col]:
                continue
            else:
                # Check Horizontal
                sum_horizontal = list(map(lambda x : sum(x), board))
                    
                # Check Vertical 
                for row in range(lenght_row_board):
                    for col in range(lenght_col_board):
                        sum_v += board[col][row]
                    sum_vertical.append(sum_v)
                    sum_v = 0

                # Check Diagonal Left to Right
                for row in range(lenght_row_board):
                    for col in range(lenght_col_board):
                        if row == col:
                            sum_dlr += board[row][col]

                # Check Diagonal Right to Left
                for row in range(lenght_row_board):
                    for col in range(lenght_col_board):
                        if row + col == len(board) - 1:
                            sum_drl += board[row][col]

                # print("Vertical: ", sum_vertical)
                # print("Horizontal: ", sum_horizontal)
                # print("Diagonal Left to Right: ", sum_dlr)
                # print("Diagonal Right to Left: ", sum_drl)

                if sum_dlr == sum_drl:
                    for element_v in range(len(sum_vertical)):
                        for element_h in range(len(sum_horizontal)):
                            if sum_vertical[element_v] == sum_horizontal[element_h]:
                                continue
                            else:
                                return False
                    return True
    return False
    
def test_is_magic_square():
    assert is_magic_square([[2.1, 7.1, 6.1], 
                            [9.1, 5.1, 1.1],
                            [4.1, 3.1, 8.1]]) == True
    
    assert is_magic_square([[4, 9, 8], 
                            [11, 7, 3],
                            [6, 5, 10]]) == False
    
    assert is_magic_square([[5, 5, 5],
                            [5, 5, 5],
                            [5, 1, 5]]) == False
    
    assert is_magic_square([[1.1, 1.2, 1.3],
                            [1.1, 1.2, 1.3],
                            [1.1, 1.2, 1.3]]) == False
    
    assert is_magic_square([[1, 5, 1],
                            [5, 5, 5],
                            [1, 5, 1]]) == False
    
    assert is_magic_square([[7, 12, 1, 14], 
                            [2, 13, 8, 11],
                            [16, 3, 10, 5],
                            [9, 6, 15, 4]]) == True
    
    assert is_magic_square([[7.1, 12.1, 1.1, 14.1], 
                            [2.1, 13.1, 8.1, 11.1],
                            [16.1, 3, 10.1, 5.1],
                            [9.1, 6.1, 15.1, 4.1]]) == True
    
    print("All OK!!!")

if __name__ == "__main__":
    main()

# print("lenghr new board: ",len(new_board[0]))
# print("Vertical: ", sum_vertical)
# print("Horizontal: ", sum_horizontal)
# print("Diagonal Left to Right: ", sum_dlr)
# print("Diagonal Right to Left: ", sum_drl)

# a = [[1, 2.2, 3]]
# for row in range(len(a)):
#     for col in range(len(a[0])):
#         a[row][col] = int(a[row][col])
# print(a)