import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mplcursors
from patches import Zones
from calculations import Heat, zone_hover_text

fig, ax = plt.subplots()
ax.grid(False)
ax.set_xlim(0, 50)
ax.set_ylim(0, 47)
lw = 2

court = patches.Rectangle(xy=[0, 0], width=50, height=47, color='white')
ax.add_patch(court)

plt.axis('off')

# Plotting Court

# Corners and Half court line
plt.plot([3, 3], [0, 14], color='black', linewidth=lw)
plt.plot([47, 47], [0, 14], color='black', linewidth=lw)
plt.plot([0, 50], [46.9, 46.9], linewidth=lw, color='black')

ax.add_patch(Zones.three_pt_arc)
ax.add_patch(Zones.paint)
ax.add_patch(Zones.paint2)
ax.add_patch(Zones.half_court_arc)
ax.add_patch(Zones.free_throw_arc1)
ax.add_patch(Zones.free_throw_arc2)
ax.add_patch(Zones.backboard)
ax.add_patch(Zones.rim)
ax.add_patch(Zones.restricted_area)

# free throw line tick marks
ax.add_patch(Zones.free_throw_tick1)
ax.add_patch(Zones.free_throw_tick2)
ax.add_patch(Zones.free_throw_tick3)
ax.add_patch(Zones.free_throw_tick4)
ax.add_patch(Zones.free_throw_tick5)
ax.add_patch(Zones.free_throw_tick6)
ax.add_patch(Zones.free_throw_tick7)
ax.add_patch(Zones.free_throw_tick8)
ax.add_patch(Zones.free_throw_tick9)
ax.add_patch(Zones.free_throw_tick10)

ax.add_patch(Zones.coach_box_tick1)
ax.add_patch(Zones.coach_box_tick2)


# Setting Heat Zones
Zones.left_corner_heat_zone.set_facecolor(Heat.left_corner_heat)
Zones.right_corner_heat_zone.set_facecolor(Heat.right_corner_heat)
Zones.left_wing_heat_zone.set_facecolor(Heat.left_wing_heat)
Zones.right_wing_heat_zone.set_facecolor(Heat.right_wing_heat)
Zones.top_key_heat_zone.set_facecolor(Heat.top_key_heat)
Zones.right_corner_mid_heat_zone.set_facecolor(Heat.right_corner_mid_heat)
Zones.right_mid_heat_zone.set_facecolor(Heat.right_mid_heat)
Zones.left_mid_heat_zone.set_facecolor(Heat.left_mid_heat)
Zones.left_corner_mid_heat_zone.set_facecolor(Heat.left_corner_mid_heat)
Zones.top_mid_heat_zone.set_facecolor(Heat.top_mid_heat)
Zones.left_close_heat_zone.set_facecolor(Heat.left_close_heat)
Zones.right_close_heat_zone.set_facecolor(Heat.right_close_heat)
Zones.middle_close_heat_zone.set_facecolor(Heat.middle_close_heat)
Zones.restricted_area_heat_zone.set_facecolor(Heat.restricted_area_heat)

# Plotting Zones
ax.add_patch(Zones.left_corner_heat_zone)
ax.add_patch(Zones.right_corner_heat_zone)
ax.add_patch(Zones.left_wing_heat_zone)
ax.add_patch(Zones.right_wing_heat_zone)
ax.add_patch(Zones.top_key_heat_zone)
ax.add_patch(Zones.right_corner_mid_heat_zone)
ax.add_patch(Zones.right_mid_heat_zone)
ax.add_patch(Zones.left_mid_heat_zone)
ax.add_patch(Zones.left_corner_mid_heat_zone)
ax.add_patch(Zones.top_mid_heat_zone)
ax.add_patch(Zones.restricted_area_heat_zone)
ax.add_patch(Zones.left_close_heat_zone)
ax.add_patch(Zones.right_close_heat_zone)
ax.add_patch(Zones.middle_close_heat_zone)

# Custom Cursor
def make_hover_handler(fig, ax, zone_hover_text):
    annotation = ax.annotate(
        "", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
        bbox=dict(boxstyle="round", fc="white", ec="gray"),
        visible=False
    )

    def on_move(event):
        if event.inaxes != ax:
            annotation.set_visible(False)
            fig.canvas.draw_idle()
            return

        found = False
        for patch, text in zone_hover_text.items():
            if patch.get_path().contains_point(
                (event.xdata, event.ydata),
                transform=patch.get_patch_transform()
            ):
                annotation.xy = (event.xdata, event.ydata)
                annotation.set_text(text)
                annotation.set_visible(True)
                found = True
                break

        if not found:
            annotation.set_visible(False)

        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_move)

make_hover_handler(fig, ax, zone_hover_text)

if __name__ == "__main__":
    plt.show()