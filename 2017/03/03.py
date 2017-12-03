import math
input = 361527

dist_to_center = int(math.ceil(math.sqrt(input)))/2

ring_begin = (((dist_to_center*2)-1)**2)+1
ring_end = ((dist_to_center*2)+1)**2

axis_diff = (ring_end-ring_begin+1)/4

axis = [ring_begin-1-(axis_diff/2)+axis_diff]
for i in range(3):
    axis.append(axis[len(axis)-1]+axis_diff)

to_axises = [abs(input-a) for a in axis]


print min(to_axises)+dist_to_center
