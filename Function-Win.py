def win(self):
        black_list =[]
        white_list = []
        for rows in self._board.get_board():
            for piece in rows:
                if piece.get_kind() == 'B':
                    black_list.append(piece)
                if piece.get_kind() == 'W':
                    white_list.append(piece)
        if len(white_list) > len(black_list):
            return "WINNER: WHITE"
        if len(white_list) == len(black_list):
            return "WINNER: TIE"
        elif len(black_list) > len(white_list):
            return "WINNER: BLACK"	