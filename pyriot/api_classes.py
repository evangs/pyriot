# -*- coding: utf-8 -*-

class Summoner(object):
    """
    id              long        Summoner ID.
    name            string      Summoner name.
    profileIconId   int         ID of the summoner icon associated with the summoner.
    revisionDate    long        Date summoner was last modified specified as epoch milliseconds.
    summonerLevel   long        Summoner level associated with the summoner.
    """
    def __init__(self, summoner_id, name, profile_icon_id, revision_date, summoner_level):
        self.id = summoner_id
        self.name = name
        self.profile_icon_id = profile_icon_id
        self.revision_date = revision_date
        self.summoner_level = summoner_level


class Champion(object):
    """
    active              boolean     Indicates if the champion is active.
    attackRank          int         Champion attack rank.
    botEnabled          boolean     Bot enabled flag (for custom games).
    botMmEnabled        boolean     Bot Match Made enabled flag (for Co-op vs. AI games).
    defenseRank         int         Champion defense rank.
    difficultyRank      int         Champion difficulty rank.
    freeToPlay          boolean     Indicates if the champion is free to play. Free to play champions are rotated periodically.
    id                  long        Champion ID.
    magicRank           int         Champion magic rank.
    name                string      Champion name.
    rankedPlayEnabled   boolean     Ranked play enabled flag.
    """
    def __init__(self, active, attack_rank, bot_enabled, 
            bot_mm_enabled, defense_rank, difficulty_rank, 
            free_to_play, champion_id, magic_rank, name,
            ranked_play_enabled):
        self.active = active
        self.attack_rank = attack_rank
        self.bot_enabled = bot_enabled
        self.bot_mm_enabled = bot_mm_enabled
        self.defense_rank = defense_rank
        self.difficulty_rank = difficulty_rank
        self.free_to_play = free_to_play
        self.id = champion_id
        self.magic_rank = magic_rank
        self.name = name
        self.ranked_play_enabled = ranked_play_enabled


class Game(object):
    """
    championId      int                 Champion ID associated with game.
    createDate      long                Date that end game data was recorded, specified as epoch milliseconds.
    createDateStr   Date                Human readable string representing date that end game data was recorded.
    fellowPlayers   List[PlayerDto]     Other players associated with the game.
    gameId          long                Game ID.
    gameMode        string              Game mode.
    gameType        string              Game type.
    invalid         boolean             Invalid flag.
    level           int                 Level.
    mapId           int                 Map ID.
    spell1          int                 ID of first summoner spell.
    spell2          int                 ID of second summoner spell.
    statistics      List[RawStatDto]    Statistics associated with the game for this summoner.
    subType         string              Game sub-type.
    teamId          int                 Team ID associated with game.
    """
    def __init__(self, champion_id, create_date, fellow_players, 
            game_id, game_mode, game_type, invalid, level, map_id,
            spell1, spell2, statistics, sub_type, team_id):
        self.champion_id = champion_id
        self.create_date = create_date
        self.fellow_players = fellow_players
        self.game_id = game_id
        self.game_mode = game_mode
        self.game_type = game_type
        self.invalid = invalid
        self.level = level
        self.map_id = map_id
        self.spell1 = spell1
        self.spell2 = spell2
        self.statistics = statistics
        self.sub_type = sub_type
        self.team_id = team_id


class Player(object):
    """
    championId  int     Champion id associated with player.
    summonerId  long    Summoner id associated with player.
    teamId      int     Team id associated with player.
    """
    def __init__(self, champion_id, summoner_id, team_id):
        self.champion_id = champion_id
        self.summoner_id = summoner_id
        self.team_id = team_id


class RawStat(object):
    """
    id      int Raw     stat ID.
    name    string      Raw stat name.
    value   int Raw     stat value.
    """
    def __init__(self, stat_id, name, value):
        self.id = stat_id
        self.name = name
        self.value = value


class League(object):
    """
    entries     List[LeagueItemDto] 
    name        string  
    queue       string                  (legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)
    tier        string                  (legal values: CHALLENGER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)
    """
    def __init__(self, entries, name, queue, tier):
        self.entries = entries
        self.name = name
        self.queue = queue
        self.tier = tier


class LeagueItem(object):
    """
    isFreshBlood        boolean 
    isHotStreak         boolean 
    isInactive          boolean 
    isVeteran           boolean 
    lastPlayed          long    
    leagueName          string  
    leaguePoints        int 
    miniSeries          MiniSeriesDto   
    playerOrTeamId      string  
    playerOrTeamName    string  
    queueType           string  
    rank                string  
    tier                string  
    wins                int
    """
    def __init__(self, is_fresh_blood, is_hot_streak, is_inactive, 
            is_veteran, last_played, league_name, league_points,
            mini_series, player_or_team_id, player_or_team_name,
            queue_type, rank, tier, wins):
        self.is_fresh_blood = is_fresh_blood
        self.is_hot_streak = is_hot_streak
        self.is_inactive = is_inactive
        self.is_veteran = is_veteran
        self.last_played = last_played
        self.league_name = league_name
        self.league_points = league_points
        self.mini_series = mini_series
        self.player_or_team_id = player_or_team_id
        self.player_or_team_name = player_or_team_name
        self.queue_type = queue_type
        self.rank = rank
        self.tier = tier
        self.wins = wins


class MiniSeries(object):
    """
    losses                  int 
    progress                Array[char] 
    target                  int 
    timeLeftToPlayMillis    long    
    wins                    int
    """
    def __init__(self, losses, progress, target, time_left_to_play_millis, wins):
        self.losses = losses
        self.progress = progress
        self.target = target
        self.time_left_to_play_millis = time_left_to_play_millis
        self.wins = wins


class PlayerStatsSummary(object):
    """
    aggregatedStats         AggregatedStatsDto      Aggregated stats.
    losses                  int                     Number of losses for this queue type. Returned for ranked queue types only.
    modifyDate              long                    Date stats were last modified specified as epoch milliseconds.
    playerStatSummaryType   string                  Player stats summary type. (legal values: AramUnranked5x5, CoopVsAI, OdinUnranked, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, Unranked, Unranked3x3, OneForAll5x5, FirstBlood1x1, FirstBlood2x2)
    wins                    int                     Number of wins for this queue type.
    """
    def __init__(self, aggregated_stats, losses, modify_date, player_stat_summary_type, wins):
        self.aggregated_stats = aggregated_stats
        self.losses = losses
        self.modify_date = modify_date
        self.player_stat_summary_type = player_stat_summary_type
        self.wins = wins


class PlayerRankedStats(object):
    """
    champions       List[ChampionStatsDto]      List of aggregated stats summarized by champion.
    modifyDate      long                        Date stats were last modified specified as epoch milliseconds.
    summonerId      long                        Summoner ID.
    """
    def __init__(self, champions, modify_date, summoner_id):
        self.champions = champions
        self.modify_date = modify_date
        self.summoner_id = summoner_id


class ChampionStats(object):
    """
    id          int                     Champion id.
    name        string                  Champion name.
    stats       AggregatedStatsDto      Aggregated stats associated with the champion.
    """
    def __init__(self, champion_id, name, stats):
        self.id = champion_id
        self.name = name
        self.stats = stats


class AggregatedStats(object):
    """
    averageAssists                  int     Dominion only.
    averageChampionsKilled          int     Dominion only.
    averageCombatPlayerScore        int     Dominion only.
    averageNodeCapture              int     Dominion only.
    averageNodeCaptureAssist        int     Dominion only.
    averageNodeNeutralize           int     Dominion only.
    averageNodeNeutralizeAssist     int     Dominion only.
    averageNumDeaths                int     Dominion only.
    averageObjectivePlayerScore     int     Dominion only.
    averageTeamObjective            int     Dominion only.
    averageTotalPlayerScore         int     Dominion only.
    botGamesPlayed                  int 
    killingSpree                    int 
    maxAssists                      int     Dominion only.
    maxChampionsKilled              int     
    maxCombatPlayerScore            int     Dominion only.
    maxLargestCriticalStrike        int 
    maxLargestKillingSpree          int 
    maxNodeCapture                  int     Dominion only.
    maxNodeCaptureAssist            int     Dominion only.
    maxNodeNeutralize               int     Dominion only.
    maxNodeNeutralizeAssist         int     Dominion only.
    maxObjectivePlayerScore         int     Dominion only.
    maxTeamObjective                int     Dominion only.
    maxTimePlayed                   int 
    maxTimeSpentLiving              int 
    maxTotalPlayerScore             int     Dominion only.
    mostChampionKillsPerSession     int 
    mostSpellsCast                  int 
    normalGamesPlayed               int 
    rankedPremadeGamesPlayed        int 
    rankedSoloGamesPlayed           int 
    totalAssists                    int 
    totalChampionKills              int 
    totalDamageDealt                int 
    totalDamageTaken                int 
    totalDoubleKills                int 
    totalFirstBlood                 int 
    totalGoldEarned                 int 
    totalHeal                       int 
    totalMagicDamageDealt           int 
    totalMinionKills                int 
    totalNeutralMinionsKilled       int 
    totalNodeCapture                int     Dominion only.
    totalNodeNeutralize             int     Dominion only.
    totalPentaKills                 int 
    totalPhysicalDamageDealt        int 
    totalQuadraKills                int 
    totalSessionsLost               int 
    totalSessionsPlayed             int 
    totalSessionsWon                int 
    totalTripleKills                int 
    totalTurretsKilled              int 
    totalUnrealKills                int
    """
    def __init__(self, average_assists, average_champions_killed, average_combat_player_score,
            average_node_capture, average_node_capture_assist, average_node_neutralize, average_node_neutralize_assist,
            average_num_deaths, average_objective_player_score, average_team_objective, average_total_player_score,
            bot_games_played, killing_spree, max_assists, max_champions_killed, max_combat_player_score,
            max_largest_critical_strike, max_largest_killing_spree, max_node_capture, max_node_capture_assist,
            max_node_neutralize, max_node_neutralize_assist, max_objective_player_score, max_team_objective,
            max_time_played, max_time_spent_living, max_total_player_score, most_champion_kills_per_session,
            most_spells_cast, normal_games_played, ranked_premade_games_played, ranked_solo_games_played,
            total_assists, total_champion_kills, total_damage_dealt, total_damage_taken, total_double_kills,
            total_first_blood, total_gold_earned, total_heal, total_magic_damage_dealt, total_minion_kills,
            total_neutral_minions_killed, total_node_capture, total_node_neutralize, total_penta_kills,
            total_physical_damage_dealt, total_quadra_kills, total_sessions_lost, total_sessions_played,
            total_sessions_won, total_triple_kills, total_turrets_killed, total_unreal_kills):
        self.average_assists = average_assists
        self.average_champions_killed = average_champions_killed
        self.average_combat_player_score = average_combat_player_score
        self.average_node_capture = average_node_capture
        self.average_node_capture_assist = average_node_capture_assist
        self.average_node_neutralize = average_node_neutralize
        self.average_node_neutralize_assist = average_node_neutralize_assist
        self.average_num_deaths = average_num_deaths
        self.average_objective_player_score = average_objective_player_score
        self.average_team_objective = average_team_objective
        self.average_total_player_score = average_total_player_score
        self.bot_games_played = bot_games_played
        self.killing_spree = killing_spree
        self.max_assists = max_assists
        self.max_champions_killed = max_champions_killed
        self.max_combat_player_score = max_combat_player_score
        self.max_largest_critical_strike = max_largest_critical_strike
        self.max_largest_killing_spree = max_largest_killing_spree
        self.max_node_capture = max_node_capture
        self.max_node_capture_assist = max_node_capture_assist
        self.max_node_neutralize = max_node_neutralize
        self.max_node_neutralize_assist = max_node_neutralize_assist
        self.max_objective_player_score = max_objective_player_score
        self.max_team_objective = max_team_objective
        self.max_time_played = max_time_played
        self.max_time_spent_living = max_time_spent_living
        self.max_total_player_score = max_total_player_score
        self.most_champion_kills_per_session = most_champion_kills_per_session
        self.most_spells_cast = most_spells_cast
        self.normal_games_played = normal_games_played
        self.ranked_premade_games_played = ranked_premade_games_played
        self.ranked_solo_games_played = ranked_solo_games_played
        self.total_assists = total_assists
        self.total_champion_kills = total_champion_kills
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_taken = total_damage_taken
        self.total_double_kills = total_double_kills
        self.total_first_blood = total_first_blood
        self.total_gold_earned = total_gold_earned
        self.total_heal = total_heal
        self.total_magic_damage_dealt = total_magic_damage_dealt
        self.total_minion_kills = total_minion_kills
        self.total_neutral_minions_killed = total_neutral_minions_killed
        self.total_node_capture = total_node_capture
        self.total_node_neutralize = total_node_neutralize
        self.total_penta_kills = total_penta_kills
        self.total_physical_damage_dealt = total_physical_damage_dealt
        self.total_quadra_kills = total_quadra_kills
        self.total_sessions_lost = total_sessions_lost
        self.total_sessions_played = total_sessions_played
        self.total_sessions_won = total_sessions_won
        self.total_triple_kills = total_triple_kills
        self.total_turrets_killed = total_turrets_killed
        self.total_unreal_kills = total_unreal_kills


class MasteryPage(object):
    """
    current     boolean             Indicates if the mastery page is the current mastery page.
    id          long                Mastery page ID.
    name        string              Mastery page name.
    talents     List[TalentDto]     List of mastery page talents associated with the mastery page.
    """
    def __init__(self, current, page_id, name, talents):
        self.current = current
        self.id = page_id
        self.name = name
        self.talents = talents


class Talent(object):
    """
    id      int         Talent id.
    name    string      Talent name.
    rank    int         Talent rank.
    """
    def __init__(self, talent_id, name, rank):
        self.id = talent_id
        self.name = name
        self.rank = rank


class RunePage(object):
    """
    current     boolean             Indicates if the page is the current page.
    id          long                Rune page ID.
    name        string              Rune page name.
    slots       List[RuneSlotDto]   List of rune slots associated with the rune page.
    """
    def __init__(self, current, page_id, name, slots):
        self.current = current
        self.id = page_id
        self.name = name
        self.slots = slots


class RuneSlot(object):
    """
    rune            RuneDto     Rune associated with the rune slot.
    runeSlotId      int         Rune slot ID.
    """
    def __init__(self, rune, rune_slot_id):
        self.rune = rune
        self.id = rune_slot_id


class Rune(object):
    """
    description     string      Rune description.
    id              int         Rune ID.
    name            string      Rune name.
    tier            int         Rune tier.
    """
    def __init__(self, description, rune_id, name, tier):
        self.description = description
        self.id = rune_id
        self.name = name
        self.tier = tier


class Team(object):
    """
    createDate                      Date    
    fullId                          string  
    lastGameDate                    Date    
    lastJoinDate                    Date    
    lastJoinedRankedTeamQueueDate   Date    
    matchHistory                    List[MatchHistorySummaryDto]    
    messageOfDay                    MessageOfDayDto 
    modifyDate                      Date    
    name                            string  
    roster                          RosterDto   
    secondLastJoinDate              Date    
    status                          string  
    tag                             string  
    teamStatSummary                 TeamStatSummaryDto  
    thirdLastJoinDate               Date
    """
    def __init__(self, create_date, full_id, last_game_date, last_join_date,
            last_joined_ranked_team_queue_date, match_history, message_of_day,
            modify_date, name, roster, second_last_join_date, status, tag,
            team_stat_summary, third_last_join_date):
        self.create_date = create_date
        self.full_id = full_id
        self.last_game_date = last_game_date
        self.last_join_date = last_join_date
        self.last_joined_ranked_team_queue_date = last_joined_ranked_team_queue_date
        self.match_history = match_history
        self.message_of_day = message_of_day
        self.modify_date = modify_date
        self.name = name
        self.roster = roster
        self.second_last_join_date = second_last_join_date
        self.status = status
        self.tag = tag
        self.team_stat_summary = team_stat_summary
        self.third_last_join_date = third_last_join_date


class MatchHistorySummary(object):
    """
    assists             int 
    deaths              int 
    gameId              long    
    gameMode            string  
    invalid             boolean 
    kills               int 
    mapId               int 
    opposingTeamKills   int 
    opposingTeamName    string  
    win                 boolean
    """
    def __init__(self, assists, deaths, game_id, game_mode, invalid, kills,
            map_id, opposing_team_kills, opposing_team_name, win):
        self.assists = assists
        self.deaths = deaths
        self.game_id = game_id
        self.game_mode = game_mode
        self.invalid = invalid
        self.kills = kills
        self.map_id = map_id
        self.opposing_team_kills = opposing_team_kills
        self.opposing_team_name = opposing_team_name
        self.win = win


class MessageOfDay(object):
    """
    createDate      long    
    message         string  
    version         int
    """
    def __init__(self, create_date, message, version):
        self.create_date = create_date
        self.message = message
        self.version = version


class Roster(object):
    """
    memberList      List[TeamMemberInfoDto] 
    ownerId         long
    """
    def __init__(self, member_list, owner_id):
        self.member_list = member_list
        self.owner_id = owner_id


class TeamStatSummary(object):
    """
    fullId              string  
    teamStatDetails     Set[TeamStatDetailDto]
    """
    def __init__(self, full_id, team_stat_details):
        self.full_id = full_id
        self.team_stat_details = team_stat_details


class TeamMemberInfo(object):
    """
    inviteDate      Date    
    joinDate        Date    
    playerId        long    
    status          string
    """
    def __init__(self, invite_date, join_date, player_id, status):
        self.invite_date = invite_date
        self.join_date = join_date
        self.player_id = player_id
        self.status = status


class TeamStatDetail(object):
    """
    averageGamesPlayed      int 
    fullId                  string  
    losses                  int 
    teamStatType            string  
    wins                    int
    """
    def __init__(self, average_games_played, full_id, losses, team_stat_type, wins):
        self.average_games_played = average_games_played
        self.full_id = full_id
        self.losses = losses
        self.team_stat_type = team_stat_type
        self.wins = wins
