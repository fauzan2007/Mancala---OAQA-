def DropSeeds(Pit):
    global Board
    Seeds = Board[Pit]
    DropPit = Pit
    PitCount = len(Board)
    Board[Pit] = 0
    while Seeds > 0:
        DropPit = (DropPit + 1) % PitCount        
        if DropPit == Pit:
            DropPit = (DropPit + 1) % PitCount
        Board[DropPit] = Board[DropPit] + 1
        Seeds = Seeds - 1
    return DropPit

# Analysis
'''

'''