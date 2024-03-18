def isValidChessBoard(chess_board):
  black_king = 0
  white_king = 0
  white_pawns = 0
  black_pawns = 0
  total_pawns = 0 
  total_pieces = 0
  count_pieces = 0

  for piece in chess_board.values():
    count_pieces = count_pieces + 1
    
    if piece == "bking":
      black_king = black_king + 1
    
    elif piece == "wking":
      white_king = white_king + 1
    
    if black_king > 1 or white_king > 1:
      return False

    if piece == "p":                # represents black pawns 
      black_pawns = black_pawns +1 
    
    elif piece == "P":
      white_pawns = white_pawns + 1   # represents white pawns 

    total_pawns = black_pawns + white_pawns
    
    if total_pawns > 8 or count_pieces > 16:
      return False

  for positions in chess_board.keys():
    numeric_part = int(''.join(filter(str.isdigit, positions)))
    string_part = ''.join(filter(str.isalpha, positions))
    
    if numeric_part > 8 or not ('a' <= string_part <= 'h'):
      return False
      
  return True

  
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
result = isValidChessBoard(board)
print(result)