def checkmate(board_str):
    board = [list(row) for row in board_str.strip().split("\n")]
    n = len(board)

    #position คิง
    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    if not king_pos:
        return

    kx, ky = king_pos

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    #pawn
    for dx, dy in [(1, -1), (1, 1)]:
        x, y = kx + dx, ky + dy
        if in_bounds(x, y) and board[x][y] == 'P':
            print("Success")
            return

    #bishop and queen
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = kx + dx, ky + dy
        while in_bounds(x, y):
            if board[x][y] != '.':
                if board[x][y] in ('B', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    #rook and queen
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = kx + dx, ky + dy
        while in_bounds(x, y):
            if board[x][y] != '.':
                if board[x][y] in ('R', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    print("Fail")

   
   
