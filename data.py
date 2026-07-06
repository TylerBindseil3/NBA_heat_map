# Practice with NBA API
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playervsplayer
from nba_api.stats.endpoints import leagueseasonmatchups
from nba_api.stats.endpoints import leaguedashptdefend
from nba_api.stats.endpoints import shotchartleaguewide
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonallplayers

def leaguewide_data(target_season):
    leaguewide = shotchartleaguewide.ShotChartLeagueWide(season=target_season)
    leaguewide_df = leaguewide.get_data_frames()[0]
    return leaguewide_df

    
def get_player_id(player):
    player_info = players.find_players_by_full_name(player)
    player_id = player_info[0]['id']
    return player_id

def get_player_team_id(player_name, target_season):
    # Get nba api objectt
    all_players_data = commonallplayers.CommonAllPlayers(
    is_only_current_season=0,
    season=target_season,
    league_id='00'
    )
    # Get player team id
    df = all_players_data.get_data_frames()[0]
    target_player = df[df['DISPLAY_FIRST_LAST'] == player_name]
    team_id = target_player['TEAM_ID'].values[0]

    return team_id

def player_shot_data(player, season):
    players_id = get_player_id(player)
    players_team = get_player_team_id(player, season)
    shot_data = shotchartdetail.ShotChartDetail(player_id=players_id, team_id=players_team, season_nullable=season, context_measure_simple='FGA')
    shot_data_df = shot_data.get_data_frames()[0]
    return shot_data_df
