import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

lw = 2

HOT = '#66FF0055'
COLD = '#FF000055'
NEUTRAL = '#FFFF0055'

court = patches.Rectangle(xy=[0, 0], width=50, height=47, color='white')

three_pt_arc = patches.Arc(xy=[25,5.1], width=47.5,height=47.5, theta1=22, theta2=158, linewidth=lw)

paint = patches.Rectangle(width=16, height=20, xy=[17, -1], fill=False, edgecolor='black', linewidth=lw)

paint2 = patches.Rectangle(width=12, height=20, xy=[19, -1], fill=False, edgecolor='black', linewidth=lw)

half_court_arc = patches.Arc(xy=[25, 47], width=12, height=12, fill=False, edgecolor='black', theta1=180, theta2=360, linewidth=1.5)

free_throw_arc1= patches.Arc(xy=[25, 19], width=12, height=12, theta1=0, theta2=180, linewidth=lw)
free_throw_arc2= patches.Arc(xy=[25, 19], width=12, height=12, theta1=180, theta2=360, ls='--', linewidth=lw)

backboard = patches.Rectangle(xy=[22,3.5],width=6,height=.5, fill=False, edgecolor='black',linewidth=lw)

rim = patches.Arc(xy=[25,5], width=1.5, height=1.5, edgecolor='black', linewidth=lw)

restricted_area = patches.Arc(xy=[25, 5], width=8, height=8, theta2=180, linewidth=lw)

# free throw line tick marks
free_throw_tick1=patches.Arc(xy=[16.5, 7], width=.6, height=0, linewidth=lw)
free_throw_tick2=patches.Arc(xy=[16.5, 8], width=.6, height=0, linewidth=lw)
free_throw_tick3=patches.Arc(xy=[16.5, 11], width=.6, height=0, linewidth=lw)
free_throw_tick4=patches.Arc(xy=[16.5, 14], width=.6, height=0, linewidth=lw)
free_throw_tick5=patches.Arc(xy=[16.5, 17], width=.6, height=0, linewidth=lw)
free_throw_tick6=patches.Arc(xy=[33.5, 7], width=.6, height=0, linewidth=lw)
free_throw_tick7=patches.Arc(xy=[33.5, 8], width=.6, height=0, linewidth=lw)
free_throw_tick8=patches.Arc(xy=[33.5, 11], width=.6, height=0, linewidth=lw)
free_throw_tick9=patches.Arc(xy=[33.5, 14], width=.6, height=0, linewidth=lw)
free_throw_tick10=patches.Arc(xy=[33.5, 17], width=.6, height=0, linewidth=lw)

coach_box_tick1=patches.Arc(xy=[0, 28], width=3, height=0, linewidth=lw)
coach_box_tick2=patches.Arc(xy=[50, 28], width=3, height=0, linewidth=lw)

# Heat zones

# Corner heat zones
left_corner_heat_zone = patches.Polygon(xy=[[0,0], [3,0], [3,14], [0,14]], closed=True, edgecolor='black', linewidth=1.5)
right_corner_heat_zone = patches.Polygon(xy=[[47,0], [50,0], [50,14], [47,14]], closed=True, edgecolor='black', linewidth=1.5)


# Left wing heat zone
start_angle_rad_lw = np.radians(107)
end_angle_rad_lw = np.radians(158)
angles_lw = np.linspace(start_angle_rad_lw, end_angle_rad_lw, 100)
x_lw = (23.75 * np.cos(angles_lw)) + 25
y_lw = (23.75 * np.sin(angles_lw)) + 5.1

arc_points_lw = np.column_stack((x_lw, y_lw))
straight_points_lw = [[3,14], [0,14], [0,50], [15, 50]]

left_wing_points = np.concatenate((arc_points_lw, straight_points_lw))

left_wing_heat_zone = patches.Polygon(xy=left_wing_points, closed=True, edgecolor='black', linewidth=1.5)

# Right wing heat zone
start_angle_rad_rw = np.radians(73)
end_angle_rad_rw = np.radians(22)
angles_rw = np.linspace(start_angle_rad_rw, end_angle_rad_rw, 100)
x_rw = (23.75 * np.cos(angles_rw)) + 25
y_rw = (23.75 * np.sin(angles_rw)) + 5.1

arc_points_rw = np.column_stack((x_rw, y_rw))
straight_points_rw = [[47,14], [50,14], [50,50], [35, 50]]

right_wing_points = np.concatenate((arc_points_rw, straight_points_rw))

right_wing_heat_zone = patches.Polygon(xy=right_wing_points, closed=True, edgecolor='black', linewidth=1.5)

# Top of key heat zone
start_angle_rad_tk = np.radians(73)
end_angle_rad_tk = np.radians(107)
angles_tk = np.linspace(start_angle_rad_tk, end_angle_rad_tk, 100)
x_tk = (23.75 * np.cos(angles_tk)) + 25
y_tk = (23.75 * np.sin(angles_tk)) + 5.1

arc_points_tk = np.column_stack((x_tk, y_tk))
straight_points_tk = [[15, 50], [35, 50]]

top_key_points = np.concatenate((arc_points_tk, straight_points_tk))
top_key_heat_zone = patches.Polygon(xy=top_key_points, closed=True, edgecolor='black', linewidth=1.5)

# Mid corner range right heat zone
start_angle_rad_mrci = np.radians(0)
end_angle_rad_mrci = np.radians(30)
angles_mrci = np.linspace(start_angle_rad_mrci, end_angle_rad_mrci, 100)
x_mrci = (16 * np.cos(angles_mrci)) + 25
y_mrci = (16 * np.sin(angles_mrci)) + 5

arc_points_mrci = np.column_stack((x_mrci, y_mrci))
straight_points_mrci = [[47, 14], [47, 0], [41, 0]]

right_corner_mid_points = np.concatenate((straight_points_mrci, arc_points_mrci))

right_corner_mid_heat_zone = patches.Polygon(xy=right_corner_mid_points, closed=True, edgecolor='black', linewidth=1.5)

# Mid right heat zone
start_angle_rad_mri = np.radians(30)
end_angle_rad_mri = np.radians(60)
angles_mri = np.linspace(start_angle_rad_mri, end_angle_rad_mri, 100)
x_mri = (16 * np.cos(angles_mri)) + 25
y_mri = (16 * np.sin(angles_mri)) + 5
arc_points_mri = np.column_stack((x_mri, y_mri))

right_mid_points = np.concatenate((arc_points_mri, [[33, 18.86]]))
right_mid_points = np.concatenate((right_mid_points, arc_points_rw))
right_mid_points = np.concatenate((right_mid_points, [[38.86, 13]]))

right_mid_heat_zone = patches.Polygon(xy=right_mid_points, closed=True, edgecolor='black', linewidth=1.5)


# Left mid heat zone 
start_angle_rad_mli = np.radians(150)
end_angle_rad_mli = np.radians(120)
angles_mli = np.linspace(start_angle_rad_mli, end_angle_rad_mli, 100)
x_mli = (16 * np.cos(angles_mli)) + 25
y_mli = (16 * np.sin(angles_mli)) + 5
arc_points_mli = np.column_stack((x_mli, y_mli))

left_mid_points = np.concatenate((arc_points_mli, [[18.06, 27.81]]))
left_mid_points = np.concatenate((left_mid_points, arc_points_lw))
left_mid_points = np.concatenate((left_mid_points, [[11.19, 13]]))

left_mid_heat_zone = patches.Polygon(xy=left_mid_points, closed=True, edgecolor='black', linewidth=1.5)


# Left corner mid range heat zone
start_angle_rad_mlci = np.radians(180)
end_angle_rad_mlci = np.radians(150)
angles_mlci = np.linspace(start_angle_rad_mlci, end_angle_rad_mlci, 100)
x_mlci = (16 * np.cos(angles_mlci)) + 25
y_mlci = (16 * np.sin(angles_mlci)) + 5

arc_points_mlci = np.column_stack((x_mlci, y_mlci))
straight_points_mlci = [[11.14, 13], [3,14], [3, 0], [9, 0]]

left_corner_mid_points = np.concatenate((straight_points_mlci, arc_points_mlci))

left_corner_mid_heat_zone = patches.Polygon(xy=left_corner_mid_points, closed=True, edgecolor='black', linewidth=1.5)


# Top mid range heat zone
start_angle_rad_mti = np.radians(120)
end_angle_rad_mti = np.radians(60)
angles_mti = np.linspace(start_angle_rad_mti, end_angle_rad_mti, 100)
x_mti = (16 * np.cos(angles_mti)) + 25
y_mti = (16 * np.sin(angles_mti)) + 5
arc_points_mti = np.column_stack((x_mti, y_mti))

top_mid_points = np.concatenate((arc_points_tk, [[17, 18.86]]))
top_mid_points = np.concatenate((top_mid_points, arc_points_mti))
top_mid_points = np.concatenate((top_mid_points, [[33, 18.86]]))
top_mid_heat_zone = patches.Polygon(xy=top_mid_points, closed=True, edgecolor='black', linewidth=1.5)


# Restricted area heat zone
start_angle_ra = np.radians(0)
end_angle_ra = np.radians(180)
angles_ra = np.linspace(start_angle_ra, end_angle_ra, 100)
x_ra = (8 * np.cos(angles_ra)) + 25
y_ra = (8 * np.sin(angles_ra)) + 5

arc_points_ra = np.column_stack((x_ra, y_ra))
straight_points_ra = [[17, 0], [33, 0]]
restricted_area_points = np.concatenate((arc_points_ra, straight_points_ra))

restricted_area_heat_zone = patches.Polygon(xy=restricted_area_points, closed=True, edgecolor='black', linewidth=1.5)


# Left close heat zone
straight_points_lc = [[17, 18.86], [17, 5], [17, 0], [9, 0]]
left_close_points = np.concatenate((arc_points_mlci, arc_points_mli))
left_close_points = np.concatenate((left_close_points, straight_points_lc))

left_close_heat_zone = patches.Polygon(xy=left_close_points, closed=True, edgecolor='black', linewidth=1.5)


# Right close heat zone
straight_points_rc = [[33, 18.86], [33, 5], [33, 0], [41, 0]]
right_close_points = np.concatenate((arc_points_mrci, arc_points_mri))
right_close_points = np.concatenate((right_close_points, straight_points_rc))

right_close_heat_zone = patches.Polygon(xy=right_close_points, closed=True, edgecolor='black', linewidth=1.5)


# Middle close heat zone
middle_close_points = np.concatenate((arc_points_ra, [[17, 18.86]]))
middle_close_points = np.concatenate((middle_close_points, arc_points_mti))
middle_close_points = np.concatenate((middle_close_points, [[33, 18.86]]))

middle_close_heat_zone = patches.Polygon(xy=middle_close_points, closed=True, edgecolor='black', linewidth=1.5)

class Zones:
    pass

Zones.left_corner_heat_zone = left_corner_heat_zone
Zones.left_wing_heat_zone = left_wing_heat_zone
Zones.top_key_heat_zone = top_key_heat_zone
Zones.right_wing_heat_zone = right_wing_heat_zone
Zones.right_corner_heat_zone = right_corner_heat_zone
Zones.left_mid_heat_zone = left_mid_heat_zone
Zones.right_corner_mid_heat_zone = right_corner_mid_heat_zone
Zones.left_corner_mid_heat_zone = left_corner_mid_heat_zone
Zones.top_mid_heat_zone = top_mid_heat_zone
Zones.right_mid_heat_zone = right_mid_heat_zone
Zones.left_close_heat_zone = left_close_heat_zone
Zones.middle_close_heat_zone = middle_close_heat_zone
Zones.right_close_heat_zone = right_close_heat_zone
Zones.restricted_area_heat_zone = restricted_area_heat_zone
Zones.three_pt_arc = three_pt_arc
Zones.paint = paint
Zones.paint2 = paint2
Zones.half_court_arc = half_court_arc
Zones.free_throw_arc1 = free_throw_arc1
Zones.free_throw_arc2 = free_throw_arc2
Zones.backboard = backboard
Zones.rim = rim
Zones.restricted_area = restricted_area

# free throw line tick marks
Zones.free_throw_tick1 = free_throw_tick1
Zones.free_throw_tick2 = free_throw_tick2
Zones.free_throw_tick3 = free_throw_tick3
Zones.free_throw_tick4 = free_throw_tick4
Zones.free_throw_tick5 = free_throw_tick5
Zones.free_throw_tick6 = free_throw_tick6
Zones.free_throw_tick7 = free_throw_tick7
Zones.free_throw_tick8 = free_throw_tick8
Zones.free_throw_tick9 = free_throw_tick9
Zones.free_throw_tick10 = free_throw_tick10

Zones.coach_box_tick1 = coach_box_tick1
Zones.coach_box_tick2 = coach_box_tick2