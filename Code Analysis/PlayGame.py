def PlayGame(Player):
    global Board, State
    while GetGameState(Player) == 'Play':
        DisplayBoard()
        Pit = GetMove(Player)
        MakeMove(Pit, Player)
        if Player == 1:
            Player = 2
        else:
            Player = 1
    print(GetGameState(Player))
    Board = []
    State = []

# Analysis
'''

'''