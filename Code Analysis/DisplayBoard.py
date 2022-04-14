def DisplayBoard():
    global Board, State
    print(' ', end='')
    PitCount = len(Board)
    for Count in range(PitCount, PitCount // 2, -1):
        print('%2d' % (Count - 1), end='')
        print('  ', end='')
    print()
    print('-' * PitCount * 2)
    for Count in range(PitCount - 1, PitCount // 2 - 1, -1):
        print('|', end='')
        if Board[Count] < 10:
            print(' ', end='')
        print(Board[Count], end='')
        print('|', end='')
    print(' Player 1 holds:', State[1])
    print('-' * PitCount * 2)
    for Count in range(0, PitCount // 2):
        print('|', end='')
        if Board[Count] < 10:
            print(' ', end='')
        print(str(Board[Count]), end='')
        print('|', end='')
    print(' Player 2 holds:', State[2])
    print('-' * PitCount * 2)
    print(' ', end='')
    for Count in range(1, PitCount // 2 + 1):
        print('%2d' % (Count - 1), end='')
        print('  ', end='')
    print()
    print()

# Analysis
'''

'''