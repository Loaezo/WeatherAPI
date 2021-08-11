from ranges.compass import wind_direction
from ranges.wind_strength import wind_description


def test_ranges_return_cardinal_points():
    assert wind_direction(5) == 'north'
    assert wind_direction(350) == 'north'
    assert wind_direction(20) == 'north northeast'
    assert wind_direction(45) == 'northeast'
    assert wind_direction(67) == 'east northeast'
    assert wind_direction(90) == 'east'
    assert wind_direction(115) == 'east southeast'
    assert wind_direction(125) == 'southeast'
    assert wind_direction(157) == 'south southeast'
    assert wind_direction(180) == 'south'
    assert wind_direction(208) == 'south southwest'
    assert wind_direction(225) == 'southwest'
    assert wind_direction(245) == 'west southwest'
    assert wind_direction(270) == 'west'
    assert wind_direction(290) == 'west northwest'
    assert wind_direction(315) == 'northwest'
    assert wind_direction(335) == 'north northwest'


def test_beauford_scale():
    assert wind_description(25) == 'Calm'
    assert wind_description(75) == 'Light air'
    assert wind_description(225) == 'Light breeze'
    assert wind_description(400) == 'Gentle breeze'
    assert wind_description(600) == 'Moderate breeze'
    assert wind_description(950) == 'Fresh breeze'
    assert wind_description(1200) == 'Strong breeze'
    assert wind_description(1500) == 'High wind'
    assert wind_description(1850) == 'Gale'
    assert wind_description(2100) == 'Strong gale'
    assert wind_description(2500) == 'Storm'
    assert wind_description(3000) == 'Violent storm'
    assert wind_description(4000) == 'Hurricane'
