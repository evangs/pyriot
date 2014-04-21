# -*- coding: utf-8 -*-

import requests
import api_classes

# API versions
# Change version as needed
CHAMPION_VERSION = 'v1.2'
GAME_VERSION = 'v1.3'
LEAGUE_VERSION = 'v2.3'
STATIC_VERSION = 'v1.2'
STATS_VERSION = 'v1.3'
SUMMONER_VERSION = 'v1.4'
TEAM_VERSION = 'v2.2'

NORTH_AMERICA = 'na'
EUROPE_WEST = 'euw'
EUROPE_EAST = 'eune'
BRAZIL = 'br'
TURKEY = 'tr'

class PyRiot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://prod.api.pvp.net/api/lol'

    def champions(self, region, free_to_play=False):
        """
        The list of champion information.

        region: Region where to retrieve the data. Use the constants included in this package.
        free_to_play: Optional filter param to retrieve only free to play champions.

        returns dictionary of champions keyed on champion id

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

        throws HTTPError
        """

        url = '{0}/{1}/{2}/champion?freeToPlay={3}&api_key={4}'.format(
                self.base_url, 
                region, 
                CHAMPION_VERSION, 
                free_to_play, 
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        champions = dict()
        for champion in content['champions']:
            champions[champion['id']] = api_classes.Champion(**champion)     

        return champions

    def recent_games(self, region, summoner_id):
        """
        List of recent games played (max 10).

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns list of recent games played by Summoner

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

        PlayerDto
        championId  int     Champion id associated with player.
        summonerId  long    Summoner id associated with player.
        teamId      int     Team id associated with player.

        RawStatDto
        id      int Raw     stat ID.
        name    string      Raw stat name.
        value   int Raw     stat value.

        throws HTTPError
        """

        url = '{0}/{1}/{2}/game/by-summoner/{3}/recent?api_key={4}'.format(
                self.base_url,
                region,
                GAME_VERSION,
                summoner_id,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        games = []
        for game in content['games']:
            games.append(api_classes.Game(**game))

        return games

    def leagues(self, region, summoner_id):
        """
        League information for summoner.

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns Map[string, LeagueDto]

        LeageDto
        entries     List[LeagueItemDto] 
        name        string  
        queue       string                  (legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)
        tier        string                  (legal values: CHALLENGER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)

        LeagueItemDto
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

        MiniSeriesDto
        losses                  int 
        progress                Array[char] 
        target                  int 
        timeLeftToPlayMillis    long    
        wins                    int

        throws HTTPError
        """

        url = '{0}/{1}/{2}/league/by-summoner/{3}?api_key={4}'.format(
                self.base_url,
                region,
                LEAGUE_VERSION,
                summoner_id,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        leagues = dict()
        for league_id in content:
            league = api_classes.League(**content[league_id])

            leagues[league_id] = league

        return leagues

    def stats_summary(self, region, summoner_id, season=None):
        """
        Summoner stat summary

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns list of player stat summaries

        playerStatSummaries     List[PlayerStatsSummaryDto]     List of player stats summaries associated with the summoner.
        summonerId              long                            Summoner ID.

        PlayerStatsSummaryDto
        aggregatedStats         AggregatedStatsDto      Aggregated stats.
        losses                  int                     Number of losses for this queue type. Returned for ranked queue types only.
        modifyDate              long                    Date stats were last modified specified as epoch milliseconds.
        playerStatSummaryType   string                  Player stats summary type. (legal values: AramUnranked5x5, CoopVsAI, OdinUnranked, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, Unranked, Unranked3x3, OneForAll5x5, FirstBlood1x1, FirstBlood2x2)
        wins                    int                     Number of wins for this queue type.

        AggregatedStatsDto
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

        throws HTTPError
        """

        url = '{0}/{1}/{2}/stats/by-summoner/{3}/summary?api_key={4}'.format(
                self.base_url,
                region,
                STATS_VERSION,
                summoner_id,
                self.api_key)

        if season:
            url += '&season=SEASON{0}'.format(season)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        player_stat_summaries = []
        for stat_summary in content['playerStatSummaries']:
            player_stat_summaries.append(api_classes.PlayerStatsSummary(**stat_summary))

        return player_stat_summaries

    def stats_ranked(self, region, summoner_id, season=None):
        """
        Summoner ranked stats

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns list of player ranked stats

        champions       List[ChampionStatsDto]      List of aggregated stats summarized by champion.
        modifyDate      long                        Date stats were last modified specified as epoch milliseconds.
        summonerId      long                        Summoner ID.

        ChampionStatsDto
        id          int                     Champion id.
        name        string                  Champion name.
        stats       AggregatedStatsDto      Aggregated stats associated with the champion.

        AggregatedStatsDto
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

        throws HTTPError
        """

        url = '{0}/{1}/{2}/stats/by-summoner/{3}/ranked?api_key={4}'.format(
                self.base_url,
                region,
                STATS_VERSION,
                summoner_id,
                self.api_key)

        if season:
            url += '&season=SEASON{0}'.format(season)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        return api_classes.PlayerRankedStats(**content)

    def summoner_masteries(self, region, summoner_id):
        """
        Summoner mastery pages

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns list of mastery pages associated with summoner

        pages           Set[MasteryPageDto]     List of mastery pages associated with the summoner.
        summonerId      long                    Summoner ID.

        MasteryPageDto
        current     boolean             Indicates if the mastery page is the current mastery page.
        id          long                Mastery page ID.
        name        string              Mastery page name.
        talents     List[TalentDto]     List of mastery page talents associated with the mastery page.

        TalentDto
        id      int         Talent id.
        name    string      Talent name.
        rank    int         Talent rank.

        throws HTTPError
        """

        url = '{0}/{1}/{2}/summoner/{3}/masteries?api_key={4}'.format(
                self.base_url,
                region,
                SUMMONER_VERSION,
                summoner_id,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        mastery_pages = []
        for page in content['pages']:
            mastery_pages.append(api_classes.MasteryPage(**page))

        return mastery_pages

    def summoner_runes(self, region, summoner_id):
        """
        Summoner rune pages

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns list of rune pages associated with summoner

        pages           Set[RunePageDto]    Set of rune pages associated with the summoner.
        summonerId      long                Summoner ID.

        RunePageDto
        current     boolean             Indicates if the page is the current page.
        id          long                Rune page ID.
        name        string              Rune page name.
        slots       List[RuneSlotDto]   List of rune slots associated with the rune page.

        RuneSlotDto
        rune            RuneDto     Rune associated with the rune slot.
        runeSlotId      int         Rune slot ID.

        RuneDto
        description     string      Rune description.
        id              int         Rune ID.
        name            string      Rune name.
        tier            int         Rune tier.

        throws HTTPError
        """

        url = '{0}/{1}/{2}/summoner/{3}/runes?api_key={4}'.format(
                self.base_url,
                region,
                SUMMONER_VERSION,
                summoner_id,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        rune_pages = []
        for page in content['pages']:
            rune_pages.append(api_classes.RunePage(**page))

        return rune_pages

    def summoner_get_by_name(self, region, summoner_name):
        """
        Get summoner by name

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_name: Summoner name.

        returns summoner information for summoner with specified name

        id              long        Summoner ID.
        name            string      Summoner name.
        profileIconId   int         ID of the summoner icon associated with the summoner.
        revisionDate    long        Date summoner was last modified specified as epoch milliseconds.
        summonerLevel   long        Summoner level associated with the summoner.

        throws HTTPError
        """

        url = '{0}/{1}/{2}/summoner/by-name/{3}?api_key={4}'.format(
                self.base_url,
                region,
                SUMMONER_VERSION,
                summoner_name,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        return api_classes.Summoner(**content.get(summoner_name))

    def summoner_get_by_id(self, region, summoner_id):
        """
        Get summoner names for list of summoner ids

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns summoner information for summoner with specified id

        id              long        Summoner ID.
        name            string      Summoner name.
        profileIconId   int         ID of the summoner icon associated with the summoner.
        revisionDate    long        Date summoner was last modified specified as epoch milliseconds.
        summonerLevel   long        Summoner level associated with the summoner.

        throws HTTPError
        """

        url = '{0}/{1}/{2}/summoner/{3}?api_key={4}'.format(
                self.base_url,
                region,
                SUMMONER_VERSION,
                summoner_id,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        return  api_classes.Summoner(**content.get('{0}'.format(summoner_id)))

    def summoner_get_names_for_ids(self, region, summoner_ids):
        """
        Get summoner names for list of summoner ids

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_ids: Comma separted string of summoner IDs.

        returns dictionary of summoner ids to names

        id      long        Summoner ID.
        name    string      Summoner name

        throws HTTPError
        """

        url = '{0}/{1}/{2}/summoner/{3}/name?api_key={4}'.format(
                self.base_url,
                region,
                SUMMONER_VERSION,
                summoner_ids,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        summoners = dict()
        for summoner in content['summoners']:
            summoners[summoner['id']] = summoner['name']

        return summoners

    def teams(self, region, summoner_id):
        """
        Get teams that summoner is in

        region: Region where to retrieve the data. Use the constants included in this package.
        summoner_id: Summoner ID.

        returns list of teams associated to a summoner

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

        MatchHistorySummaryDto
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

        MessageOfDayDto
        createDate      long    
        message         string  
        version         int

        RosterDto
        memberList      List[TeamMemberInfoDto] 
        ownerId         long

        TeamStatSummaryDto
        fullId              string  
        teamStatDetails     Set[TeamStatDetailDto]

        TeamMemberInfoDto
        inviteDate      Date    
        joinDate        Date    
        playerId        long    
        status          string

        TeamStatDetailDto
        averageGamesPlayed      int 
        fullId                  string  
        losses                  int 
        teamStatType            string  
        wins                    int
        """

        url = '{0}/{1}/{2}/team/by-summoner/{3}?api_key={4}'.format(
                self.base_url,
                region,
                TEAM_VERSION,
                summoner_id,
                self.api_key)

        response = requests.get(url)
        response.raise_for_status()
        content = response.json()

        teams = []
        for team in content:
            teams.append(api_classes.Team(**team))

        return teams