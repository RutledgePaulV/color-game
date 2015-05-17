R = 0
G = 1
B = 2


def from_hex(hex):
	return int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16)


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


def average_colors(colors):
	weighted = []
	total_weight = 0
	for weight, color in colors:
		total_weight += weight
		weighted.append([component * weight for component in color])

	zipped = list(zip(*weighted))
	return int(round(sum(zipped[R]) / total_weight)), \
		   int(round(sum(zipped[G]) / total_weight)), \
		   int(round(sum(zipped[B]) / total_weight))


def get_color_for_leaf(leaf, clockwise):
	volume = 0
	color = None

	for c in leaf[::1 if clockwise else -1]:
		if c is None:
			volume = max(volume - 1, 0)
		else:
			volume += 1
			if not color: color = c
			else: color = average_colors([(volume, color), (1, c)])

	return volume, color


volume1, clockwise = get_color_for_leaf(LEAF, True)
volume2, counter_clockwise = get_color_for_leaf(LEAF, False)

final = average_colors([(4*volume1, clockwise), (volume2, counter_clockwise)])

print(volume1 * 4, clockwise)
print(volume2 * 1, counter_clockwise)

print(final)