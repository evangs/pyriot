# -*- coding: utf-8 -*-

import utils

class Summoner(object):
    """
    id              long        Summoner ID.
    name            string      Summoner name.
    profileIconId   int         ID of the summoner icon associated with the summoner.
    revisionDate    long        Date summoner was last modified specified as epoch milliseconds.
    summonerLevel   long        Summoner level associated with the summoner.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.profile_icon_id = kwargs['profileIconId']
        self.revision_date = utils.convert_epoch_millis_to_datetime(kwargs['revisionDate'])
        self.summoner_level = kwargs['summonerLevel']


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
    def __init__(self, **kwargs):
        self.active = kwargs['active']
        self.attack_rank = kwargs['attackRank']
        self.bot_enabled = kwargs['botEnabled']
        self.bot_mm_enabled = kwargs['botMmEnabled']
        self.defense_rank = kwargs['defenseRank']
        self.difficulty_rank = kwargs['difficultyRank']
        self.free_to_play = kwargs['freeToPlay']
        self.id = kwargs['id']
        self.magic_rank = kwargs['magicRank']
        self.name = kwargs['name']
        self.ranked_play_enabled = kwargs['rankedPlayEnabled']


class Game(object):
    """
    championId      int                 Champion ID associated with game.
    createDate      long                Date that end game data was recorded, specified as epoch milliseconds.
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
    def __init__(self, **kwargs):
        self.champion_id = kwargs['championId']
        self.create_date = utils.convert_epoch_millis_to_datetime(kwargs['createDate'])

        players = []
        for player in kwargs['fellowPlayers']:
            players.append(Player(**player))
        self.fellow_players = players

        self.game_id = kwargs['gameId']
        self.game_mode = kwargs['gameMode']
        self.game_type = kwargs['gameType']
        self.invalid = kwargs['invalid']
        self.level = kwargs['level']
        self.map_id = kwargs['mapId']
        self.spell1 = kwargs['spell1']
        self.spell2 = kwargs['spell2']

        stats = []
        for stat in kwargs['statistics']:
            stats.append(RawStat(**stat))
        self.statistics = stats

        self.sub_type = kwargs['subType']
        self.team_id = kwargs['teamId']


class Player(object):
    """
    championId  int     Champion id associated with player.
    summonerId  long    Summoner id associated with player.
    teamId      int     Team id associated with player.
    """
    def __init__(self, **kwargs):
        self.champion_id = kwargs['championId']
        self.summoner_id = kwargs['summonerId']
        self.team_id = kwargs['teamId']


class RawStat(object):
    """
    id      int Raw     stat ID.
    name    string      Raw stat name.
    value   int Raw     stat value.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.value = kwargs['value']


class League(object):
    """
    entries     List[LeagueItemDto] 
    name        string  
    queue       string                  (legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)
    tier        string                  (legal values: CHALLENGER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)
    """
    def __init__(self, **kwargs):
        entries = []
        for entry in kwargs['entries']:
            entries.append(LeagueItem(**entry))
        self.entries = entries

        self.name = kwargs['name']
        self.queue = kwargs['queue']
        self.tier = kwargs['tier']


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
    def __init__(self, **kwargs):
        self.is_fresh_blood = kwargs['isFreshBlood']
        self.is_hot_streak = kwargs['isHotStreak']
        self.is_inactive = kwargs['isInactive']
        self.is_veteran = kwargs['isVeteran']
        self.last_played = kwargs['lastPlayed']
        self.league_name = kwargs['leagueName']
        self.league_points = kwargs['leaguePoints']

        if 'miniSeries' in kwargs:
            self.mini_series = MiniSeries(**kwargs['miniSeries'])

        self.player_or_team_id = kwargs['playerOrTeamId']
        self.player_or_team_name = kwargs['playerOrTeamName']
        self.queue_type = kwargs['queueType']
        self.rank = kwargs['rank']
        self.tier = kwargs['tier']
        self.wins = kwargs['wins']


class MiniSeries(object):
    """
    losses                  int 
    progress                Array[char] 
    target                  int 
    timeLeftToPlayMillis    long    
    wins                    int
    """
    def __init__(self, **kwargs):
        self.losses = kwargs['losses']
        self.progress = kwargs['progress']
        self.target = kwargs['target']
        self.time_left_to_play_millis = kwargs['timeLeftToPlayMillis']
        self.wins = kwargs['wins']


class PlayerStatsSummary(object):
    """
    aggregatedStats         AggregatedStatsDto      Aggregated stats.
    losses                  int                     Number of losses for this queue type. Returned for ranked queue types only.
    modifyDate              long                    Date stats were last modified specified as epoch milliseconds.
    playerStatSummaryType   string                  Player stats summary type. (legal values: AramUnranked5x5, CoopVsAI, OdinUnranked, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, Unranked, Unranked3x3, OneForAll5x5, FirstBlood1x1, FirstBlood2x2)
    wins                    int                     Number of wins for this queue type.
    """
    def __init__(self, **kwargs):
        self.aggregated_stats = AggregatedStats(**kwargs['aggregatedStats'])
        self.losses = kwargs['losses']
        self.modify_date = utils.convert_epoch_millis_to_datetime(kwargs['modifyDate'])
        self.player_stat_summary_type = kwargs['playerStatSummaryType']
        self.wins = kwargs['wins']


class PlayerRankedStats(object):
    """
    champions       List[ChampionStatsDto]      List of aggregated stats summarized by champion.
    modifyDate      long                        Date stats were last modified specified as epoch milliseconds.
    summonerId      long                        Summoner ID.
    """
    def __init__(self, **kwargs):
        champions = []
        for champion in kwargs['champions']:
            champions.append(ChampionStats(**champion))
        self.champions = champions

        self.modify_date = utils.convert_epoch_millis_to_datetime(kwargs['modifyDate'])
        self.summoner_id = kwargs['summonerId']


class ChampionStats(object):
    """
    id          int                     Champion id.
    name        string                  Champion name.
    stats       AggregatedStatsDto      Aggregated stats associated with the champion.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.stats = AggregatedStats(**kwargs['stats'])


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
    def __init__(self, **kwargs):
        if 'averageAssists' in kwargs:
            self.average_assists = kwargs['averageAssists']
        if 'averageChampionsKilled' in kwargs:
            self.average_champions_killed = kwargs['averageChampionsKilled']
        if 'averageCombatPlayerScore' in kwargs:
            self.average_combat_player_score = kwargs['averageCombatPlayerScore']
        if 'averageNodeCapture' in kwargs:
            self.average_node_capture = kwargs['averageNodeCapture']
        if 'averageNodeCaptureAssist' in kwargs:
            self.average_node_capture_assist = kwargs['averageNodeCaptureAssist']
        if 'averageNodeNeutralize' in kwargs:
            self.average_node_neutralize = kwargs['averageNodeNeutralize']
        if 'averageNodeNeutralizeAssist' in kwargs:
            self.average_node_neutralize_assist = kwargs['averageNodeNeutralizeAssist']
        if 'averageNumDeaths' in kwargs:
            self.average_num_deaths = kwargs['averageNumDeaths']
        if 'averageObjectivePlayerScore' in kwargs:
            self.average_objective_player_score = kwargs['averageObjectivePlayerScore']
        if 'averageTeamObjective' in kwargs:
            self.average_team_objective = kwargs['averageTeamObjective']
        if 'averageTotalPlayerScore' in kwargs:
            self.average_total_player_score = kwargs['averageTotalPlayerScore']
        if 'botGamesPlayed' in kwargs:
            self.bot_games_played = kwargs['botGamesPlayed']
        if 'killingSpree' in kwargs:
            self.killing_spree = kwargs['killingSpree']
        if 'maxAssists' in kwargs:
            self.max_assists = kwargs['maxAssists']
        if 'maxChampionsKilled' in kwargs:
            self.max_champions_killed = kwargs['maxChampionsKilled']
        if 'maxCombatPlayerScore' in kwargs:
            self.max_combat_player_score = kwargs['maxCombatPlayerScore']
        if 'maxLargestCriticalStrike' in kwargs:
            self.max_largest_critical_strike = kwargs['maxLargestCriticalStrike']
        if 'maxLargestKillingSpree' in kwargs:
            self.max_largest_killing_spree = kwargs['maxLargestKillingSpree']
        if 'maxNodeCapture' in kwargs:
            self.max_node_capture = kwargs['maxNodeCapture']
        if 'maxNodeCaptureAssist' in kwargs:
            self.max_node_capture_assist = kwargs['maxNodeCaptureAssist']
        if 'maxNodeNeutralize' in kwargs:
            self.max_node_neutralize = kwargs['maxNodeNeutralize']
        if 'maxNodeNeutralizeAssist' in kwargs:
            self.max_node_neutralize_assist = kwargs['maxNodeNeutralizeAssist']
        if 'maxObjectivePlayerScore' in kwargs:
            self.max_objective_player_score = kwargs['maxObjectivePlayerScore']
        if 'maxTeamObjective' in kwargs:
            self.max_team_objective = kwargs['maxTeamObjective']
        if 'maxTimePlayed' in kwargs:
            self.max_time_played = kwargs['maxTimePlayed']
        if 'maxTimeSpentLiving' in kwargs:
            self.max_time_spent_living = kwargs['maxTimeSpentLiving']
        if 'maxTotalPlayerScore' in kwargs:
            self.max_total_player_score = kwargs['maxTotalPlayerScore']
        if 'mostChampionKillsPerSession' in kwargs:
            self.most_champion_kills_per_session = kwargs['mostChampionKillsPerSession']
        if 'mostSpellsCast' in kwargs:
            self.most_spells_cast = kwargs['mostSpellsCast']
        if 'normalGamesPlayed' in kwargs:
            self.normal_games_played = kwargs['normalGamesPlayed']
        if 'rankedPremadeGamesPlayed' in kwargs:
            self.ranked_premade_games_played = kwargs['rankedPremadeGamesPlayed']
        if 'rankedSoloGamesPlayed' in kwargs:
            self.ranked_solo_games_played = kwargs['rankedSoloGamesPlayed']
        if 'totalAssists' in kwargs:
            self.total_assists = kwargs['totalAssists']
        if 'totalChampionKills' in kwargs:
            self.total_champion_kills = kwargs['totalChampionKills']
        if 'totalDamageDealt' in kwargs:
            self.total_damage_dealt = kwargs['totalDamageDealt']
        if 'totalDamageTaken' in kwargs:
            self.total_damage_taken = kwargs['totalDamageTaken']
        if 'totalDoubleKills' in kwargs:
            self.total_double_kills = kwargs['totalDoubleKills']
        if 'totalFirstBlood' in kwargs:
            self.total_first_blood = kwargs['totalFirstBlood']
        if 'totalGoldEarned' in kwargs:
            self.total_gold_earned = kwargs['totalGoldEarned']
        if 'totalHeal' in kwargs:
            self.total_heal = kwargs['totalHeal']
        if 'totalMagicDamageDealt' in kwargs:
            self.total_magic_damage_dealt = kwargs['totalMagicDamageDealt']
        if 'totalMinionKills' in kwargs:
            self.total_minion_kills = kwargs['totalMinionKills']
        if 'totalNeutralMinionsKilled' in kwargs:
            self.total_neutral_minions_killed = kwargs['totalNeutralMinionsKilled']
        if 'totalNodeCapture' in kwargs:
            self.total_node_capture = kwargs['totalNodeCapture']
        if 'totalNodeNeutralize' in kwargs:
            self.total_node_neutralize = kwargs['totalNodeNeutralize']
        if 'totalPentaKills' in kwargs:
            self.total_penta_kills = kwargs['totalPentaKills']
        if 'totalPhysicalDamageDealt' in kwargs:
            self.total_physical_damage_dealt = kwargs['totalPhysicalDamageDealt']
        if 'totalQuadraKills' in kwargs:
            self.total_quadra_kills = kwargs['totalQuadraKills']
        if 'totalSessionsLost' in kwargs:
            self.total_sessions_lost = kwargs['totalSessionsLost']
        if 'totalSessionsPlayed' in kwargs:
            self.total_sessions_played = kwargs['totalSessionsPlayed']
        if 'totalSessionsWon' in kwargs:
            self.total_sessions_won = kwargs['totalSessionsWon']
        if 'totalTripleKills' in kwargs:
            self.total_triple_kills = kwargs['totalTripleKills']
        if 'totalTurretsKilled' in kwargs:
            self.total_turrets_killed = kwargs['totalTurretsKilled']
        if 'totalUnrealKills' in kwargs:
            self.total_unreal_kills = kwargs['totalUnrealKills']


class MasteryPage(object):
    """
    current     boolean             Indicates if the mastery page is the current mastery page.
    id          long                Mastery page ID.
    name        string              Mastery page name.
    talents     List[TalentDto]     List of mastery page talents associated with the mastery page.
    """
    def __init__(self, **kwargs):
        self.current = kwargs['current']
        self.id = kwargs['id']
        self.name = kwargs['name']

        if 'talents' in kwargs:
            talents = []
            for talent in kwargs['talents']:
                talents.append(Talent(**talent))
            self.talents = talents


class Talent(object):
    """
    id      int         Talent id.
    name    string      Talent name.
    rank    int         Talent rank.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.rank = kwargs['rank']


class RunePage(object):
    """
    current     boolean             Indicates if the page is the current page.
    id          long                Rune page ID.
    name        string              Rune page name.
    slots       List[RuneSlotDto]   List of rune slots associated with the rune page.
    """
    def __init__(self, **kwargs):
        self.current = kwargs['current']
        self.id = kwargs['id']
        self.name = kwargs['name']

        if 'slots' in kwargs:
            slots = []
            for slot in kwargs['slots']:
                slots.append(RuneSlot(**slot))
            self.slots = slots


class RuneSlot(object):
    """
    rune            RuneDto     Rune associated with the rune slot.
    runeSlotId      int         Rune slot ID.
    """
    def __init__(self, **kwargs):
        self.rune = Rune(**kwargs['rune'])
        self.id = kwargs['runeSlotId']


class Rune(object):
    """
    description     string      Rune description.
    id              int         Rune ID.
    name            string      Rune name.
    tier            int         Rune tier.
    """
    def __init__(self, **kwargs):
        self.description = kwargs['description']
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.tier = kwargs['tier']


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
    def __init__(self, **kwargs):
        self.create_date = utils.convert_epoch_millis_to_datetime(kwargs['createDate'])
        self.full_id = kwargs['fullId']
        self.last_game_date = utils.convert_epoch_millis_to_datetime(kwargs['lastGameDate'])
        self.last_join_date = utils.convert_epoch_millis_to_datetime(kwargs['lastJoinDate'])
        self.last_joined_ranked_team_queue_date = utils.convert_epoch_millis_to_datetime(kwargs['lastJoinedRankedTeamQueueDate'])
        
        match_history = []
        for match in kwargs['matchHistory']:
            match_history.append(MatchHistorySummary(**match))
        self.match_history = match_history

        if 'messageOfDay' in kwargs:
            self.message_of_day = MessageOfDay(**kwargs['messageOfDay'])
        self.modify_date = utils.convert_epoch_millis_to_datetime(kwargs['modifyDate'])
        self.name = kwargs['name']
        self.roster = Roster(**kwargs['roster'])
        self.second_last_join_date = utils.convert_epoch_millis_to_datetime(kwargs['secondLastJoinDate'])
        self.status = kwargs['status']
        self.tag = kwargs['tag']
        self.team_stat_summary = TeamStatSummary(**kwargs['teamStatSummary'])
        self.third_last_join_date = utils.convert_epoch_millis_to_datetime(kwargs['thirdLastJoinDate'])


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
    def __init__(self, **kwargs):
        self.assists = kwargs['assists']
        self.deaths = kwargs['deaths']
        self.game_id = kwargs['gameId']
        self.game_mode = kwargs['gameMode']
        self.invalid = kwargs['invalid']
        self.kills = kwargs['kills']
        self.map_id = kwargs['mapId']
        self.opposing_team_kills = kwargs['opposingTeamKills']
        self.opposing_team_name = kwargs['opposingTeamName']
        self.win = kwargs['win']


class MessageOfDay(object):
    """
    createDate      long    
    message         string  
    version         int
    """
    def __init__(self, **kwargs):
        self.create_date = utils.convert_epoch_millis_to_datetime(kwargs['createDate'])
        self.message = kwargs['message']
        self.version = kwargs['version']


class Roster(object):
    """
    memberList      List[TeamMemberInfoDto] 
    ownerId         long
    """
    def __init__(self, **kwargs):
        member_list = []
        for member in kwargs['memberList']:
            member_list.append(TeamMemberInfo(**member))
        self.member_list = member_list

        self.owner_id = kwargs['ownerId']


class TeamStatSummary(object):
    """
    fullId              string  
    teamStatDetails     Set[TeamStatDetailDto]
    """
    def __init__(self, **kwargs):
        self.full_id = kwargs['fullId']

        team_stat_details = []
        for team_stat_detail in kwargs['teamStatDetails']:
            team_stat_details.append(TeamStatDetail(**team_stat_detail))
        self.team_stat_details = team_stat_details


class TeamMemberInfo(object):
    """
    inviteDate      Date    
    joinDate        Date    
    playerId        long    
    status          string
    """
    def __init__(self, **kwargs):
        self.invite_date = utils.convert_epoch_millis_to_datetime(kwargs['inviteDate'])
        self.join_date = utils.convert_epoch_millis_to_datetime(kwargs['joinDate'])
        self.player_id = kwargs['playerId']
        self.status = kwargs['status']


class TeamStatDetail(object):
    """
    averageGamesPlayed      int 
    fullId                  string  
    losses                  int 
    teamStatType            string  
    wins                    int
    """
    def __init__(self, **kwargs):
        self.average_games_played = kwargs['averageGamesPlayed']
        self.full_id = kwargs['fullId']
        self.losses = kwargs['losses']
        self.team_stat_type = kwargs['teamStatType']
        self.wins = kwargs['wins']
