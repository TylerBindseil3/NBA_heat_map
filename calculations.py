import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.path import Path
from data import player_shot_data, leaguewide_data
from patches import Zones

# Heat zone colors
HOT = '#66FF0055'
NEUTRAL = '#FFFF0055'
COLD = '#FF000055'

# Player Name first param, season is in format of '2025-26'
shot_data = player_shot_data('Anthony Edwards', '2025-26')
leaguewide_df = leaguewide_data('2025-26')

# transforming coords to match our court
x_cords = (shot_data['LOC_X']).to_numpy()
y_cords = (shot_data['LOC_Y']).to_numpy()

x_cords = (x_cords * .1) + 25
y_cords = (y_cords * .1) + 5

shot_cords = np.column_stack((x_cords, y_cords))

ZONE_DEFS = [
    {"name": "left_corner", "patch": Zones.left_corner_heat_zone, "label": "Left Corner", "filters": [("Left Corner 3", "Left Side(L)", None)]},
    {"name": "left_wing", "patch": Zones.left_wing_heat_zone, "label": "Left Wing", "filters": [("Above the Break 3", "Left Side Center(LC)", None)]},
    {"name": "top_key", "patch": Zones.top_key_heat_zone, "label": "Top Key", "filters": [("Above the Break 3", "Center(C)", None)]},
    {"name": "right_wing", "patch": Zones.right_wing_heat_zone, "label": "Right Wing", "filters": [("Above the Break 3", "Right Side Center(RC)", None)]},
    {"name": "right_corner", "patch": Zones.right_corner_heat_zone, "label": "Right Corner", "filters": [("Right Corner 3", "Right Side(R)", None)]},
    {"name": "left_corner_mid", "patch": Zones.left_corner_mid_heat_zone, "label": "Left Corner Mid", "filters": [("Mid-Range", "Left Side(L)", "16-24 ft.")]},
    {"name": "left_mid", "patch": Zones.left_mid_heat_zone, "label": "Left Mid", "filters": [("Mid-Range", "Left Side Center(LC)", "16-24 ft.")]},
    {"name": "top_mid", "patch": Zones.top_mid_heat_zone, "label": "Top Mid", "filters": [("Mid-Range", "Center(C)", "16-24 ft.")]},
    {"name": "right_mid", "patch": Zones.right_mid_heat_zone, "label": "Right Mid", "filters": [("Mid-Range", "Right Side Center(RC)", "16-24 ft.")]},
    {"name": "right_corner_mid", "patch": Zones.right_corner_mid_heat_zone, "label": "Right Corner Mid", "filters": [("Mid-Range", "Right Side(R)", "16-24 ft.")]},
    {"name": "left_close", "patch": Zones.left_close_heat_zone, "label": "Left Close", "filters": [("Mid-Range", "Left Side(L)", "8-16 ft.")]},
    {"name": "middle_close", "patch": Zones.middle_close_heat_zone, "label": "Middle Close", 
    "filters": [("Mid-Range", "Center(C)", "8-16 ft."), ("In The Paint (Non-RA)", "Left Side(L)", "8-16 ft."), 
    ("In The Paint (Non-RA)", "Center(C)", "8-16 ft."), ("In The Paint (Non-RA)", "Right Side(R)", "8-16 ft.")]},
    {"name": "right_close", "patch": Zones.right_close_heat_zone, "label": "Right Close", "filters": [("Mid-Range", "Right Side(R)", "8-16 ft.")]},
    {"name": "restricted_area", "patch": Zones.restricted_area_heat_zone, "label": "Restricted Area",
    "filters": [("Restricted Area", "Center(C)", "Less Than 8 ft."), ("In The Paint (Non-RA)", "Center(C)", "Less Than 8 ft.")]}
    ]

# Checks heat level of given zone
def check_heat(zone_fgp, zone_std_dev, league_fgp):
    if zone_fgp - league_fgp > 1.28 * zone_std_dev:
        return HOT
    elif not(zone_fgp + (1.28 * zone_std_dev) < league_fgp): 
        return NEUTRAL
    else:
        return COLD

# Calculate league average fg pct of each zone
def league_fg_pct(leaguewide_df, filters):
    total_fgm = 0
    total_fga = 0
    
    for zone_basic, zone_area, zone_range in filters:
        mask = (leaguewide_df["SHOT_ZONE_BASIC"] == zone_basic) & (leaguewide_df["SHOT_ZONE_AREA"] == zone_area)
        
        if zone_range is not None:
            mask = mask & (leaguewide_df["SHOT_ZONE_RANGE"] == zone_range)
        
        fga_row = leaguewide_df["FGA"][mask].item()
        fgm_row = leaguewide_df["FGM"][mask].item()
        total_fga += fga_row
        total_fgm += fgm_row
    
    return total_fgm / total_fga

# Compute stats for the zones on our plot
def compute_zone_stats(shot_data, shot_cords, patch, filters, leaguewide_df):

    mask = patch.get_path().contains_points(shot_cords)
    zone_shot_data = shot_data[mask]
    attempts = len(zone_shot_data)
    made = (zone_shot_data["SHOT_MADE_FLAG"] == 1).sum()
    
    league_fgp = league_fg_pct(leaguewide_df, filters)
    
    if attempts == 0:
        fgp = float('nan')
        std_dev = float('nan')
        heat = NEUTRAL 
    else:
        fgp = made/attempts
        std_dev = sqrt(league_fgp * (1 - league_fgp) / attempts)
        heat = check_heat(fgp, std_dev, league_fgp)
    
    return {
        "attempts": attempts,
        "made": made,
        "fgp": fgp,
        "league_fgp": league_fgp,
        "std_dev": std_dev,
        "heat": heat,
    }

# Create dictionary containing data necessary to compute zone stats
results = {}
for zone in ZONE_DEFS:
    results[zone["name"]] = compute_zone_stats(
        shot_data, shot_cords, zone["patch"], zone["filters"], leaguewide_df
    )

# Hover text for cursor
zone_hover_text = {}
for name, r in results.items():
    # find the matching zone definition by name to get its label
    zone = next(z for z in ZONE_DEFS if z["name"] == name)
    
    zone_hover_text[zone["patch"]] = (
        f"{zone['label']}\n"
        f"FG%: {r['fgp']:.1%}\n"
        f"FGA: {r['attempts']}\n"
        f"League FG%: {r['league_fgp']:.1%}"
    )

# Set heat level for each zone
class Heat:
    pass

for name, r in results.items():
    setattr(Heat, f"{name}_heat", r["heat"])

