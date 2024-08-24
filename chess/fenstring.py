def board_to_fen(board):
    finalstr = []
    for rows in board:
        space = 0
        for item in rows:
            if item == '.':
                space += 1
            else:
                if space != 0:
                    finalstr.append(str(space))
                    space = 0
                finalstr.append(item)
        if space != 0:
            finalstr.append(str(space))
        finalstr.append("/")
    
    fen_str = "".join(finalstr)
    print(fen_str)
    return fen_str[:-1]
