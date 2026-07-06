import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.path import Path
from data import player_shot_data, leaguewide_data
from patches import Zones

# Player Name first param, season is in format of '2025-26'
shot_data = player_shot_data('Shai Gilgeous-Alexander', '2025-26')

# transforming coords to match our court
x_cords = (shot_data['LOC_X']).to_numpy()
y_cords = (shot_data['LOC_Y']).to_numpy()

x_cords = (x_cords * .1) + 25
y_cords = (y_cords * .1) + 5

shot_cords = np.column_stack((x_cords, y_cords))

# Setting path which is used as boundaries for checking where shots fall
left_corner_zone = Zones.left_corner_heat_zone.get_path()
left_wing_zone = Zones.left_wing_heat_zone.get_path()
top_key_zone = Zones.top_key_heat_zone.get_path()
right_wing_zone = Zones.right_wing_heat_zone.get_path()
right_corner_zone = Zones.right_corner_heat_zone.get_path()
left_corner_mid_zone = Zones.left_corner_mid_heat_zone.get_path()
left_mid_zone = Zones.left_mid_heat_zone.get_path()
top_mid_zone = Zones.top_mid_heat_zone.get_path()
right_mid_zone = Zones.right_mid_heat_zone.get_path()
right_corner_mid_zone = Zones.right_corner_mid_heat_zone.get_path()
left_close_zone = Zones.left_close_heat_zone.get_path()
middle_close_zone = Zones.middle_close_heat_zone.get_path()
right_close_zone = Zones.right_close_heat_zone.get_path()
restricted_zone = Zones.restricted_area_heat_zone.get_path()

# Checking which shots fall in each zone
in_left_corner = left_corner_zone.contains_points(shot_cords)
in_left_wing = left_wing_zone.contains_points(shot_cords)
in_top_key = top_key_zone.contains_points(shot_cords)
in_right_wing = right_wing_zone.contains_points(shot_cords)
in_right_corner = right_corner_zone.contains_points(shot_cords)
in_left_mid = left_mid_zone.contains_points(shot_cords)
in_left_corner_mid = left_corner_mid_zone.contains_points(shot_cords)
in_top_mid = top_mid_zone.contains_points(shot_cords)
in_right_mid = right_mid_zone.contains_points(shot_cords)
in_right_corner_mid = right_corner_mid_zone.contains_points(shot_cords)
in_left_close = left_close_zone.contains_points(shot_cords)
in_middle_close = middle_close_zone.contains_points(shot_cords)
in_right_close = right_close_zone.contains_points(shot_cords)
in_restricted_area = restricted_zone.contains_points(shot_cords)

# Filtering shot events to shots that fall within each zone
left_corner_shots = shot_cords[in_left_corner]
left_wing_shots = shot_cords[in_left_wing]
top_key_shots = shot_cords[in_top_key]
right_wing_shots = shot_cords[in_right_wing]
right_corner_shots = shot_cords[in_right_corner]
left_mid_shots = shot_cords[in_left_mid]
left_corner_mid_shots = shot_cords[in_left_corner_mid]
top_mid_shots = shot_cords[in_top_mid]
right_mid_shots = shot_cords[in_right_mid]
right_corner_mid_shots = shot_cords[in_right_corner_mid]
left_close_shots = shot_cords[in_left_close]
middle_close_shots = shot_cords[in_middle_close]
right_close_shots = shot_cords[in_right_close]
restricted_area_shots = shot_cords[in_restricted_area]

# Filtering shot data which contains shot_made_flag to find how many shots were made
left_corner_shot_data = shot_data[in_left_corner]
left_corner_shots_made = (left_corner_shot_data['SHOT_MADE_FLAG'] == 1).sum()
left_wing_shot_data = shot_data[in_left_wing]
left_wing_shots_made = (left_wing_shot_data['SHOT_MADE_FLAG'] == 1).sum()
top_key_shot_data = shot_data[in_top_key]
top_key_shots_made = (top_key_shot_data['SHOT_MADE_FLAG'] == 1).sum()
right_wing_shot_data = shot_data[in_right_wing]
right_wing_shots_made = (right_wing_shot_data['SHOT_MADE_FLAG'] == 1).sum()
right_corner_shot_data = shot_data[in_right_corner]
right_corner_shots_made = (right_corner_shot_data['SHOT_MADE_FLAG'] == 1).sum()
left_mid_shot_data = shot_data[in_left_mid]
left_mid_shots_made = (left_mid_shot_data['SHOT_MADE_FLAG'] == 1).sum()
left_corner_mid_shot_data = shot_data[in_left_corner_mid]
left_corner_mid_shots_made = (left_corner_mid_shot_data['SHOT_MADE_FLAG'] == 1).sum()
top_mid_shot_data = shot_data[in_top_mid]
top_mid_shots_made = (top_mid_shot_data['SHOT_MADE_FLAG'] == 1).sum()
right_mid_shot_data = shot_data[in_right_mid]
right_mid_shots_made = (right_mid_shot_data['SHOT_MADE_FLAG'] == 1).sum()
right_corner_mid_shot_data = shot_data[in_right_corner_mid]
right_corner_mid_shots_made = (right_corner_mid_shot_data['SHOT_MADE_FLAG'] == 1).sum()
left_close_shot_data = shot_data[in_left_close]
left_close_shots_made = (left_close_shot_data['SHOT_MADE_FLAG'] == 1).sum()
middle_close_shot_data = shot_data[in_middle_close]
middle_close_shots_made = (middle_close_shot_data['SHOT_MADE_FLAG'] == 1).sum()
right_close_shot_data = shot_data[in_right_close]
right_close_shots_made = (right_close_shot_data['SHOT_MADE_FLAG'] == 1).sum()
restricted_area_shot_data = shot_data[in_restricted_area]
restricted_area_shots_made = (restricted_area_shot_data['SHOT_MADE_FLAG'] == 1).sum()

# FG% Calculations
left_corner_shot_FGP = left_corner_shots_made / len(left_corner_shots)
left_wing_shot_FGP = left_wing_shots_made / len(left_wing_shots)
top_key_shot_FGP = top_key_shots_made / len(top_key_shots)
right_wing_shot_FGP = right_wing_shots_made / len(right_wing_shots)
right_corner_shot_FGP = right_corner_shots_made / len(right_corner_shots)
left_mid_shot_FGP = left_mid_shots_made / len(left_mid_shots)
left_corner_mid_shot_FGP = left_corner_mid_shots_made / len(left_corner_mid_shots)
top_mid_shot_FGP = top_mid_shots_made / len(top_mid_shots)
right_mid_shot_FGP = right_mid_shots_made / len(right_mid_shots)
right_corner_mid_shot_FGP = right_corner_mid_shots_made / len(right_corner_mid_shots)
left_close_shot_FGP = left_close_shots_made / len(left_close_shots)
middle_close_shot_FGP = middle_close_shots_made / len(middle_close_shots)
right_close_shot_FGP = right_close_shots_made / len(right_close_shots)
restricted_area_shot_FGP = restricted_area_shots_made / len(restricted_area_shots)
print(left_corner_shot_FGP)
print(left_wing_shot_FGP)
print(top_key_shot_FGP)
print(right_wing_shot_FGP)
print(right_corner_shot_FGP)



# League wide FG PCT for heat zones
leaguewide_df = leaguewide_data('2025-26')
 
league_left_corner_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Left Corner 3') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side(L)')].item()
league_left_wing_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Above the Break 3') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side Center(LC)')].item()
league_top_key_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Above the Break 3') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)')].item()
league_right_wing_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Above the Break 3') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side Center(RC)')].item()
league_right_corner_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Right Corner 3') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side(R)')].item()
league_left_corner_mid_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side(L)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '16-24 ft.')].item()
league_left_mid_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side Center(LC)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '16-24 ft.')].item()
league_top_mid_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '16-24 ft.')].item()
league_right_mid_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side Center(RC)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '16-24 ft.')].item()
league_right_corner_mid_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side(R)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '16-24 ft.')].item()
league_left_close_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side(L)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_right_close_shot_FGP = leaguewide_df['FG_PCT'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side(R)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()

# Restricted area
league_restricted_area_shot_FGA1 = leaguewide_df['FGA'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Restricted Area') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)')].item()
league_restricted_area_shot_FGA2 = leaguewide_df['FGA'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == 'Less Than 8 ft.')].item()
league_restricted_area_shot_FGM1 = leaguewide_df['FGM'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Restricted Area') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)')].item()
league_restricted_area_shot_FGM2 = leaguewide_df['FGM'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == 'Less Than 8 ft.')].item()

league_restricted_area_shot_FGP = (league_restricted_area_shot_FGM1 + league_restricted_area_shot_FGM2) / (league_restricted_area_shot_FGA1 + league_restricted_area_shot_FGA2)
# Middle Close area
league_middle_close_shot_FGA1 = leaguewide_df['FGA'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGA2 = leaguewide_df['FGA'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGA3 = leaguewide_df['FGA'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side(L)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGA4 = leaguewide_df['FGA'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side(R)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGM1 = leaguewide_df['FGM'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'Mid-Range') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGM2 = leaguewide_df['FGM'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Center(C)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGM3 = leaguewide_df['FGM'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Left Side(L)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()
league_middle_close_shot_FGM4 = leaguewide_df['FGM'][(leaguewide_df['SHOT_ZONE_BASIC'] == 'In The Paint (Non-RA)') & (leaguewide_df['SHOT_ZONE_AREA'] == 'Right Side(R)') & (leaguewide_df['SHOT_ZONE_RANGE'] == '8-16 ft.')].item()

league_middle_close_shot_FGP = (league_middle_close_shot_FGM1 + league_middle_close_shot_FGM2 + league_middle_close_shot_FGM3 + league_middle_close_shot_FGM4) / (league_middle_close_shot_FGA1 + league_middle_close_shot_FGA2 + league_middle_close_shot_FGA3 + league_middle_close_shot_FGA4)
print(league_left_corner_shot_FGP)
print(league_left_wing_shot_FGP)
print(league_top_key_shot_FGP)
print(league_right_wing_shot_FGP)
print(len(left_corner_shots))
# Calculating std dev for zones
left_corner_std_dev = sqrt(league_left_corner_shot_FGP * (1 - league_left_corner_shot_FGP) / len(left_corner_shots))
left_wing_std_dev = sqrt(league_left_wing_shot_FGP * (1 - league_left_wing_shot_FGP) / len(left_wing_shots))
top_key_std_dev = sqrt(league_top_key_shot_FGP * (1 - league_top_key_shot_FGP) / len(top_key_shots))
right_wing_std_dev = sqrt(league_right_wing_shot_FGP * (1 - league_right_wing_shot_FGP) / len(right_wing_shots))
right_corner_std_dev = sqrt(league_right_corner_shot_FGP * (1 - league_right_corner_shot_FGP) / len(right_corner_shots))
left_corner_mid_std_dev = sqrt(league_left_corner_mid_shot_FGP * (1 - league_left_corner_mid_shot_FGP) / len(left_corner_mid_shots))
left_mid_std_dev = sqrt(league_left_mid_shot_FGP * (1 - league_left_mid_shot_FGP) / len(left_mid_shots))
top_mid_std_dev = sqrt(league_top_mid_shot_FGP * (1 - league_top_mid_shot_FGP) / len(top_mid_shots))
right_mid_std_dev = sqrt(league_right_mid_shot_FGP * (1 - league_right_mid_shot_FGP) / len(right_mid_shots))
right_corner_mid_std_dev = sqrt(league_right_corner_mid_shot_FGP * (1 - league_right_corner_mid_shot_FGP) / len(right_corner_mid_shots))
left_close_std_dev = sqrt(league_left_close_shot_FGP * (1 - league_left_close_shot_FGP) / len(left_close_shots))
middle_close_std_dev = sqrt(league_middle_close_shot_FGP * (1 - league_middle_close_shot_FGP) / len(middle_close_shots))
right_close_std_dev = sqrt(league_right_close_shot_FGP * (1 - league_right_close_shot_FGP) / len(right_close_shots))
restricted_area_std_dev = sqrt(league_restricted_area_shot_FGP * (1 - league_restricted_area_shot_FGP) / len(restricted_area_shots))

def check_heat(zone_fgp, zone_std_dev, league_fgp):
    if zone_fgp - league_fgp > zone_std_dev:
        return '#66FF0055'
    elif not(zone_fgp + zone_std_dev < league_fgp): 
        return '#FFFF0055'
    else:
        return '#FF000055'
    
class Heat:
    pass

Heat.left_corner_heat = check_heat(left_corner_shot_FGP, left_corner_std_dev, league_left_corner_shot_FGP)
Heat.left_wing_heat = check_heat(left_wing_shot_FGP, left_wing_std_dev, league_left_wing_shot_FGP)
Heat.top_key_heat = check_heat(top_key_shot_FGP, top_key_std_dev, league_top_key_shot_FGP)
Heat.right_wing_heat = check_heat(right_wing_shot_FGP, right_wing_std_dev, league_right_wing_shot_FGP)
Heat.right_corner_heat = check_heat(right_corner_shot_FGP, right_corner_std_dev, league_right_corner_shot_FGP)
Heat.left_corner_mid_heat = check_heat(left_corner_mid_shot_FGP, left_corner_mid_std_dev, league_left_corner_mid_shot_FGP)
Heat.left_mid_heat = check_heat(left_mid_shot_FGP, left_mid_std_dev, league_left_mid_shot_FGP)
Heat.top_mid_heat = check_heat(top_mid_shot_FGP, top_mid_std_dev, league_top_mid_shot_FGP)
Heat.right_mid_heat = check_heat(right_mid_shot_FGP, right_mid_std_dev, league_right_mid_shot_FGP)
Heat.right_corner_mid_heat = check_heat(right_corner_mid_shot_FGP, right_corner_mid_std_dev, league_right_corner_mid_shot_FGP)
Heat.left_close_heat = check_heat(left_close_shot_FGP, left_close_std_dev, league_left_close_shot_FGP)
Heat.middle_close_heat = check_heat(middle_close_shot_FGP, middle_close_std_dev, league_middle_close_shot_FGP)
Heat.right_close_heat = check_heat(right_close_shot_FGP, right_close_std_dev, league_right_close_shot_FGP)
Heat.restricted_area_heat = check_heat(restricted_area_shot_FGP, restricted_area_std_dev, league_restricted_area_shot_FGP)

# Building hover text for each zone
zone_hover_text = {
    Zones.left_corner_heat_zone: (
        f"Left Corner\n"
        f"FG%: {left_corner_shot_FGP:.1%}\n"
        f"FGA: {len(left_corner_shots)}\n"
        f"League FG%: {league_left_corner_shot_FGP:.1%}"
    ),
    Zones.right_corner_heat_zone: (
        f"Right Corner\n"
        f"FG%: {right_corner_shot_FGP:.1%}\n"
        f"FGA: {len(right_corner_shots)}\n"
        f"League FG%: {league_right_corner_shot_FGP:.1%}"
    ),
    Zones.left_wing_heat_zone: (
        f"Left Wing\n"
        f"FG%: {left_wing_shot_FGP:.1%}\n"
        f"FGA: {len(left_wing_shots)}\n"
        f"League FG%: {league_left_wing_shot_FGP:.1%}"
    ),
    Zones.right_wing_heat_zone: (
        f"Right Wing\n"
        f"FG%: {right_wing_shot_FGP:.1%}\n"
        f"FGA: {len(right_wing_shots)}\n"
        f"League FG%: {league_right_wing_shot_FGP:.1%}"
    ),
    Zones.top_key_heat_zone: (
        f"Top of Key\n"
        f"FG%: {top_key_shot_FGP:.1%}\n"
        f"FGA: {len(top_key_shots)}\n"
        f"League FG%: {league_top_key_shot_FGP:.1%}"
    ),
    Zones.right_corner_mid_heat_zone: (
        f"Right Corner Mid\n"
        f"FG%: {right_corner_mid_shot_FGP:.1%}\n"
        f"FGA: {len(right_corner_mid_shots)}\n"
        f"League FG%: {league_right_corner_mid_shot_FGP:.1%}"
    ),
    Zones.right_mid_heat_zone: (
        f"Right Mid\n"
        f"FG%: {right_mid_shot_FGP:.1%}\n"
        f"FGA: {len(right_mid_shots)}\n"
        f"League FG%: {league_right_mid_shot_FGP:.1%}"
    ),
    Zones.left_mid_heat_zone: (
        f"Left Mid\n"
        f"FG%: {left_mid_shot_FGP:.1%}\n"
        f"FGA: {len(left_mid_shots)}\n"
        f"League FG%: {league_left_mid_shot_FGP:.1%}"
    ),
    Zones.left_corner_mid_heat_zone: (
        f"Left Corner Mid\n"
        f"FG%: {left_corner_mid_shot_FGP:.1%}\n"
        f"FGA: {len(left_corner_mid_shots)}\n"
        f"League FG%: {league_left_corner_mid_shot_FGP:.1%}"
    ),
    Zones.top_mid_heat_zone: (
        f"Top Mid\n"
        f"FG%: {top_mid_shot_FGP:.1%}\n"
        f"FGA: {len(top_mid_shots)}\n"
        f"League FG%: {league_top_mid_shot_FGP:.1%}"
    ),
    Zones.left_close_heat_zone: (
        f"Left Close\n"
        f"FG%: {left_close_shot_FGP:.1%}\n"
        f"FGA: {len(left_close_shots)}\n"
        f"League FG%: {league_left_close_shot_FGP:.1%}"
    ),
    Zones.right_close_heat_zone: (
        f"Right Close\n"
        f"FG%: {right_close_shot_FGP:.1%}\n"
        f"FGA: {len(right_close_shots)}\n"
        f"League FG%: {league_right_close_shot_FGP:.1%}"
    ),
    Zones.middle_close_heat_zone: (
        f"Middle Close\n"
        f"FG%: {middle_close_shot_FGP:.1%}\n"
        f"FGA: {len(middle_close_shots)}\n"
        f"League FG%: {league_middle_close_shot_FGP:.1%}"
    ),
    Zones.restricted_area_heat_zone: (
        f"Restricted Area\n"
        f"FG%: {restricted_area_shot_FGP:.1%}\n"
        f"FGA: {len(restricted_area_shots)}\n"
        f"League FG%: {league_restricted_area_shot_FGP:.1%}"
    ),
}

