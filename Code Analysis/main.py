def Main():
    global Board
    Playing = True
    while Playing:
        DisplayMenu()
        Choice = input('Choice: ')
        if Choice == 'H':
            DisplayHelp()
        elif Choice == 'S':
            Seeds, PitCount = GetInitialValues()
            SetupBoard('S', Seeds, PitCount)
        elif Choice == 'B': 
            if len(Board) != 0:
                Player = random.randint(1, 2)
                PlayGame(Player)
            else:
                print('You need to setup a board first')
        elif Choice == 'T':
            SetupBoard('T')
            Player = 1
            PlayGame(Player)
        elif Choice == 'Q':
            Playing = False

# Analysis
'''

'''