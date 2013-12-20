PyRiot
======

This is a simple wrapper to make calling the Riot League of Legends api extremely easy within a python app.

Installation
------------
pip install pyriot

Example
-------
	from pyriot.wrapper import PyRiot, NORTH_AMERICA
	priot = PyRiot('your_riot_api_key')

	priot.summoner_get_by_name(NORTH_AMERICA, 'evangs')

	{u'id': 24915110,
	 u'name': u'evangs',
	 u'profileIconId': 547,
	 u'revisionDate': 1387485731000,
	 u'summonerLevel': 30}

Wrapper Functions
-----------------
For more in-depth documentation, look at the source code pyriot/wrapper.py

*champions(region, free_to_play=False)*
+ region - use the region constants in wrapper.py
+ free_to_play - flag when set to true only returns free to play champions

*recent_games(region, summoner_id)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function

*leagues(region, summoner_id)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function

*stats_summary(region, summoner_id, season=None)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function
+ season - integer representation of the season (1, 2, 3, etc)

*stats_ranked(region, summoner_id, season=None)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function
+ season - integer representation of the season (1, 2, 3, etc)

*summoner_masteries(region, summoner_id)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function

*summoner_runes(region, summoner_id)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function

*summoner_get_by_name(region, summoner_name)*
+ region - use the region constants in wrapper.py
+ summoner_name - name of the summoner

*summoner_get_by_id(region, summoner_id)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function

*summoner_get_names_for_ids(region, summoner_ids)*
+ region - use the region constants in wrapper.py
+ summoner_ids - comma separated string of summoner ids

*teams(region, summoner_id)*
+ region - use the region constants in wrapper.py
+ summoner_id - the summoner id can be obtained by calling the summoner_get_by_name function

License
-------
This code is licensed under the MIT License, but to use the Riot api you must also agree to their terms of use found at https://developer.riotgames.com/terms
