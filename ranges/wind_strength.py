
def wind_description(speed):
    """
    Converts the wind speed to te description using the Beaufort scale
    :param speed: The wind speed in m/s
    :return: the Beaufort's scale description
    """
    calm = range(0, 50)
    light_air = range(50, 150)
    light_breeze = range(150, 330)
    gentle_breeze = range(330, 550)
    moderate_breeze = range(550, 790)
    fresh_breeze = range(790, 1070)
    strong_breeze = range(1070, 1380)
    high_wind = range(1380, 1710)
    gale = range(1710, 2070)
    strong_gale = range(2070, 2440)
    storm = range(2440, 2840)
    violent_storm = range(2840, 3260)
    hurricane = range(3260, 5000)

    if speed in calm:
        description = 'Calm'
        return description

    elif speed in light_air:
        description = 'Light air'
        return description

    elif speed in light_breeze:
        description = 'Light breeze'
        return description

    elif speed in gentle_breeze:
        description = 'Gentle breeze'
        return description

    elif speed in moderate_breeze:
        description = 'Moderate breeze'
        return description

    elif speed in fresh_breeze:
        description = 'Fresh breeze'
        return description

    elif speed in strong_breeze:
        description = 'Strong breeze'
        return description

    elif speed in high_wind:
        description = 'High wind'
        return description

    elif speed in gale:
        description = 'Gale'
        return description

    elif speed in strong_gale:
        description = 'Strong gale'
        return description

    elif speed in storm:
        description = 'Storm'
        return description

    elif speed in violent_storm:
        description = 'Violent storm'
        return description

    elif speed in hurricane:
        description = 'Hurricane'
        return description

