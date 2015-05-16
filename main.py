def from_hex(hex):
    return int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16)


R = 0
G = 1
B = 2


COLORS = {
    'RED': from_hex('FF0000'),
    'ORANGE': from_hex('FF7700'),
    'YELLOW': from_hex('FFDD00'),
    'GREEN': from_hex('00FF00'),
    'BLUE': from_hex('0000FF'),
    'INDIGO': from_hex('8A2BE2'),
    'VIOLET': from_hex('C77Df3')
}


LEAF = [
    COLORS['RED'],
    COLORS['ORANGE'],
    COLORS['YELLOW'],
    COLORS['GREEN'],
    COLORS['BLUE'],
    COLORS['INDIGO'],
    COLORS['VIOLET'],
]



def average(current_color, new_color, current_volume, new_volume):
    resulting_volume = current_volume + new_volume
    weighted_current = [x * current_volume for x in current_color]
    weighted_new = [x * new_volume for x in new_color]

    result_red = weighted_current[R] + weighted_new[R]
    result_green = weighted_current[G] + weighted_new[G]
    result_blue = weighted_current[B] + weighted_new[B]

    return [int(round(x / resulting_volume, 0)) for x in (result_red, result_green, result_blue)]



def get_color_for_leaf(leaf, clockwise):
    volume = 0
    color = None

    for c in leaf[::1 if clockwise else -1]:
        if c is None:
            volume = max(volume-1, 0)
        else:
            volume += 1
            if not color:
                color = c
            else:
                color = average(color, c, volume, 1)

    return volume, color


volume1, clockwise = get_color_for_leaf(LEAF, True)
volume2, counter_clockwise = get_color_for_leaf(LEAF, False)

final = average(clockwise, counter_clockwise, 4*volume1, volume2)

print(final)