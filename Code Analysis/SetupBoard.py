def SetupBoard(TypeOfBoard, Seeds=0, PitCount=0):
    global Board, State
    if TypeOfBoard == 'T':
        Board = [1, 0, 3, 1, 2, 2, 0, 0, 0, 0, 2, 1]
        State = [48, 16, 20]
    elif TypeOfBoard == 'S':
        CreateBoard(Seeds, PitCount)
        State = [Seeds, 0, 0]

# Analysis
'''

'''