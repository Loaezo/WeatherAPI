
def wind_direction(degrees):
    """
    Function to convert degrees (360-based) to cardinal points
    :param degrees: receives the degrees the wind is blowing
    :return: the orientation as a string
    """
    north = range(0, 11)
    north_2 = range(348, 360)
    north_northeast = range(11, 34)
    northeast = range(34, 56)
    east_northeast = range(56, 79)
    east = range(79, 101)
    east_southeast = range(101, 124)
    southeast = range(124, 146)
    south_southeast = range(146, 169)
    south = range(169, 191)
    south_southwest = range(191, 214)
    southwest = range(214, 236)
    west_southwest = range(236, 259)
    west = range(259, 281)
    west_northwest = range(281, 304)
    northwest = range(304, 326)
    north_northwest = range(326, 348)

    if degrees in north:
        direction = 'north'
        return direction

    elif degrees in north_2:
        direction = 'north'
        return direction

    elif degrees in north_northeast:
        direction = 'north northeast'
        return direction

    elif degrees in northeast:
        direction = 'northeast'
        return direction

    elif degrees in east_northeast:
        direction = 'east northeast'
        return direction

    elif degrees in east:
        direction = 'east'
        return direction

    elif degrees in east_southeast:
        direction = 'east southeast'
        return direction

    elif degrees in southeast:
        direction = 'southeast'
        return direction

    elif degrees in south_southeast:
        direction = 'south southeast'
        return direction

    elif degrees in south:
        direction = 'south'
        return direction

    elif degrees in south_southwest:
        direction = 'south southwest'
        return direction

    elif degrees in southwest:
        direction = 'southwest'
        return direction

    elif degrees in west_southwest:
        direction = 'west southwest'
        return direction

    elif degrees in west:
        direction = 'west'
        return direction

    elif degrees in west_northwest:
        direction = 'west northwest'
        return direction

    elif degrees in northwest:
        direction = 'northwest'
        return direction

    elif degrees in north_northwest:
        direction = 'north northwest'
        return direction
