def minSwapsToChessboard(board):
    n = len(board)
    
    def is_valid(board):
        # Check condition 1
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))
        for i in range(n):
            for j in range(n):
                if board[i][j] ^ board[0][j] ^ row_sum ^ col_sum:
                    return False

        for i in range(n):
            for j in range(n):
                if board[i][j] != (i + j) % 2:
                    return False
        
        return True
    
    row_count = board[0].count(1)
    col_count = sum(board[i][0] for i in range(n))
    
    if not is_valid(board) or abs(row_count - col_count) > 1:
        return -1
    
    row_swaps = col_swaps = 0
    if row_count > n // 2:
        row_swaps = sum(1 - board[0][i] for i in range(0, n, 2))
    else:
        row_swaps = sum(board[0][i] for i in range(0, n, 2))
    
    if col_count > n // 2:
        col_swaps = sum(1 - board[i][0] for i in range(0, n, 2))
    else:
        col_swaps = sum(board[i][0] for i in range(0, n, 2))
    
    return (n - max(row_count, n - row_count) + row_swaps) // 2 + (n - max(col_count, n - col_count) + col_swaps) // 2

board = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
print(minSwapsToChessboard(board))  
