def MakeMove(Pit, Player):
    global Board, State
    LastPit = DropSeeds(Pit)
    while Board[LastPit] in [2, 3]:
        print('Collected seeds from pit: ' + str(LastPit))
        State[Player] = State[Player] + Board[LastPit]
        Board[LastPit] = 0
        LastPit = LastPit - 1
        if LastPit == -1:
            LastPit = len(Board) - 1

# Analysis
'''

'''