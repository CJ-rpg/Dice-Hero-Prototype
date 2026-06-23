
def has_large_straight(dice):
    return dice == [1,2,3,4,5] or dice == [2,3,4,5,6]
    
def has_small_straight(dice):
    unique = sorted(set(dice))

    return (
        [1,2,3,4] == unique[:4] or
        [2,3,4,5] == unique[:4] or
        [3,4,5,6] == unique[:4] or
        [1,2,3,4] == unique[-4:] or
        [2,3,4,5] == unique[-4:] or
        [3,4,5,6] == unique[-4:]
    )
