R = 0
G = 1
B = 2

def from_hex(hex):
	return int(hex[:2], 16), \
	       int(hex[2:4], 16), \
	       int(hex[4:], 16)

COLORS = {
	'RED': from_hex('FF0000'),
	'ORANGE': from_hex('FF7700'),
	'YELLOW': from_hex('FFDD00'),
	'GREEN': from_hex('00FF00'),
	'BLUE': from_hex('0000FF'),
	'INDIGO': from_hex('8A2BE2'),
	'VIOLET': from_hex('C77Df3')
}


def average_colors(colors):
	weighted = []
	total_weight = 0.0
	for weight, color in colors:
		total_weight += weight
		weighted.append([component * weight for component in color])

	zipped = list(zip(*weighted))
	return sum(zipped[R]) / total_weight, \
	       sum(zipped[G]) / total_weight, \
	       sum(zipped[B]) / total_weight


def get_color_for_leaf(leaf, clockwise):
	volume = 0.0
	color = None

	for c in leaf[::1 if clockwise else -1]:
		if c is None:
			volume = max(volume - 1, 0.0)
		else:
			if not color:
				color = c
			else:
				color = average_colors([(volume, color), (1.0, c)])

			volume += 1.0

	return volume, color



TWIGS_PER_BRANCH = 5.
MAX_CAPACITY_OF_BUG = 7.
CLOCKWISE_TWIGS_PER_BRANCH = 4
COUNTER_CLOCKWISE_TWIGS_PER_BRANCH = 1
COLOR_IN_BUCKET = (255., 255., 255.)
VOLUME_IN_BUCKET_PER_BRANCH = TWIGS_PER_BRANCH * MAX_CAPACITY_OF_BUG


LEAF = [
	COLORS['RED'],
	COLORS['ORANGE'],
	COLORS['YELLOW'],
	None,
	None,
	COLORS['GREEN'],
	None,
	None,
	COLORS['BLUE'],
	COLORS['INDIGO'],
	COLORS['VIOLET'],
]


volume1, clockwise = get_color_for_leaf(LEAF, True)
volume2, counter_clockwise = get_color_for_leaf(LEAF, False)

clockwise_volume_per_branch = CLOCKWISE_TWIGS_PER_BRANCH * volume1
counter_clockwise_volume_per_branch = COUNTER_CLOCKWISE_TWIGS_PER_BRANCH * volume2
actual_volume_per_branch = clockwise_volume_per_branch + counter_clockwise_volume_per_branch


average_color_on_branch = average_colors([
	(clockwise_volume_per_branch, clockwise),
	(counter_clockwise_volume_per_branch, counter_clockwise)
])


bucket_color = average_colors([
	(VOLUME_IN_BUCKET_PER_BRANCH, COLOR_IN_BUCKET),
	(actual_volume_per_branch, average_color_on_branch)
])


print(
	round(bucket_color[R]),
	round(bucket_color[G]),
	round(bucket_color[B])
)