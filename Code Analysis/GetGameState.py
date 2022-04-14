def GetGameState(Player):
    global State
    TotalSeeds = State[0]
    PlayerOneSeeds = State[1]
    PlayerTwoSeeds = State[2]
    if  PlayerOneSeeds >= TotalSeeds // 2 + 1 or PlayerTwoSeeds >= TotalSeeds // 2 + 1:
        return 'Won'
    else:
        return 'Play'

# Analysis
'''

'''