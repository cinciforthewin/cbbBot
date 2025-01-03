#!/Usr/bin/python3
import datetime
import pytz

tz = pytz.timezone('US/Eastern')

tv_flairs = {'BTN':'[Big Ten Network](#l/btn)', 'CBS':'[CBS](#l/cbs)', 'CBSSN':'[CBS Sports Network](#l/cbssn)', 'ESPN':'[ESPN](#l/espn)', 'ESPN2':'[ESPN2](#l/espn2)', 'ESPN3':'[ESPN3](#l/espn3)', 'ESPNU':'[ESPNU](#l/espnu)', 'FOX':'[Fox](#l/fox)', 'FS1':'[Fox Sports 1](#l/fs1)', 'FSN':'[Fox Sports Network](#l/fsn)', 'LHN':'[Longhorn Network](#l/lhn)', 'NBC':'[NBC](#l/nbc)', 'NBCSN':'[NBC Sports Network](#l/nbcsn)', 'PAC12':'[Pac-12 Network](#l/p12n)', 'SEC Network':'[SEC Network](#l/secn)', 'TBS':'[TBS](#l/tbs)', 'TNT':'[TNT](#l/tnt)', 'truTV':'[truTV](#l/trutv)', 'ACC Network':'[ACC Network](#l/accn)', 'ACCNE':'[ACC Network Extra](#l/accne)', 'ACCNX':'[ACC Network Extra](#l/accne)', 'ESPNN':'[ESPNews](#l/espnews)', 'FS2':'[Fox Sports 2](#l/fs2)', 'ABC':'[ABC](#l/abc)', 'ESPN+':'[ESPN+](#l/espnplus)', 'BIG12|ESPN+': '[ESPN+](#l/espnplus)', 'Peacock': '[Peacock](#l/peacock)', 'Paramount+': '[Paramount+](#l/paramountplus)', 'Big Ten Plus': '[B1G+](#l/bigtenplus)', 'Fox App': '[Fox Sports Network](#l/fsn)', 'CW NETWORK': '[The CW](#l/cw)', 'BTN+':'[Big Ten Plus](#l/bigtenplus)'}

tv_stream_links = {'BTN':'[BTN](https://www.fox.com/live/channel/BTN/)', 'CBS':'[CBS](https://www.cbssports.com/college-basketball/cbk-live/)', 'CBSSN':'[CBSSN](https://www.cbssports.com/cbs-sports-network/)', 'ESPN':'[WatchESPN](https://www.espn.com/watch/)', 'ESPN2':'[WatchESPN](https://www.espn.com/watch/)', 'ESPN3':'[WatchESPN](https://www.espn.com/watch/)', 'ESPNU':'[WatchESPN](https://www.espn.com/watch/)', 'ESPNN':'[WatchESPN](https://www.espn.com/watch/)', 'FOX':'[FOX](https://www.foxsports.com/live/)', 'FS1':'[FS1](https://www.foxsports.com/live/fs1)', 'FSN':'[FOX Sports](https://www.foxsports.com/live)', 'LHN':'[WatchESPN](https://www.espn.com/watch/)', 'NBC':'[NBC Sports](http://www.nbcsports.com/live)', 'USA Net':'[NBC Sports](http://www.nbcsports.com/live)', 'PAC12':'[PAC12](https://pac-12.com/live)', 'SEC Network':'[WatchESPN](https://www.espn.com/watch/)', 'ACC Network':'[WatchESPN](https://www.espn.com/watch/)', 'ACCNE':'[WatchESPN](https://www.espn.com/watch/)', 'ACCNX':'[WatchESPN](https://www.espn.com/watch/)', 'ESPN+':'[ESPN+](https://plus.espn.com/)', 'BIG12|ESPN+':'[ESPN+](https://plus.espn.com/)', 'FS2':'[FS2](https://www.foxsports.com/live/fs2)', 'ABC':'[WatchESPN](https://www.espn.com/watch/', 'Fox App': '[Fox Sports](https://www.foxsports.com/live)', 'Peacock': '[Peacock](https://www.peacocktv.com/)', 'BTN+':'[BTN+](https://www.bigtenplus.com/)'}

msg_success = 'Thanks for your message. The game you requested has been successfully added to the queue and will be created within an hour of the scheduled game time. If the game has already started, the thread will be created momentarily. If the game is over, no thread will be created.'
msg_fail = 'Thanks for your message. If you are trying to submit a game thread request, please make sure your title is "request" (case-insensitive) and the body contains only the ESPN game ID. If your request is successful, you will get a confirmation reply. If you have a question or comment about the bot, please send to u/Ike348.'
msg_young = 'Thanks for your message. Unfortunately, your account does not currently meet the minimum requirements to request a thread.'
msg_stopped = 'Successfully blocked this game thread!'
msg_success_pg = 'Thanks for your message. A post-game thread will be created for this game upon its conclusion.'
msg_spam = 'Thanks for your message. Unfortunately, you have already requested the maximum of 2 game threads today, so the bot will not consider any additional requests from this account until tomorrow.'
msg_duplicate = 'Thanks for your message. This game has already been added to the queue, so a game thread will be posted one hour prior to tipoff, if one has not been posted already.'

with open('./data/index_thread.txt', 'r') as f:
    index_permalink = f.read()

def if_exists(dct, key, value):
    if key in dct:
        return dct[key]
    return value

def make_game_thread(game_id, game_data, comment_stream_link = ''):
    thread = game_data['awayFlair']

    if game_data['gameClock'] != '':
        thread = thread + ' ' + '**' + str(game_data['awayScore']) + '**' + ' @ **' + str(game_data['homeScore']) + '** '
    else:
        thread = thread + ' @ '

    thread = thread + game_data['homeFlair']

    if game_data['gameClock'] != '':
        thread = thread + ' - **' + game_data['gameClock'].upper() + '**'

    thread = thread + '\n\n\n###NCAA Basketball'
    #thread = thread + '\n [**^Click ^here ^to ^request ^a ^Game ^Thread**](https://www.reddit.com/r/CollegeBasketball/comments/5o5at9/introducing_ucbbbot_an_easier_way_of_making_game/)\n\n---\n '

    thread = thread + '\n [**^' + ' ^'.join(('Index Thread for ' + game_data['startTime'].strftime('%B %d, %Y')).split()) + '**](https://www.reddit.com' + index_permalink + ')\n\n---\n '
    if game_data['awayRecord'] == '':
        game_data['awayRecord'] = '--'
    if game_data['homeRecord'] == '':
        game_data['homeRecord'] = '--'
    if game_data['awayRank'] != '':
        game_data['awayRank'] = '#' + str(game_data['awayRank']) + ' '
    if game_data['homeRank'] != '':
        game_data['homeRank'] = '#' + str(game_data['homeRank']) + ' '

    if game_data['awayFlair'] == game_data['awayTeam']:
        thread = thread + ' **' + game_data['awayRank'] + game_data['awayTeam'] + '** (' + game_data['awayRecord'] + ') @ '
    else:
        thread = thread + game_data['awayFlair'] + ' **' + game_data['awayRank'] + game_data['awayTeam'] + '** (' + game_data['awayRecord'] + ') @ '

    if game_data['homeFlair'] == game_data['homeTeam']:
        thread = thread + ' **' + game_data['homeRank'] + game_data['homeTeam'] + '** (' + game_data['homeRecord'] + ')\n\nTip-Off: '
    else:
        thread = thread + game_data['homeFlair'] + ' **' + game_data['homeRank'] + game_data['homeTeam'] + '** (' + game_data['homeRecord'] + ')\n\nTip-Off: '

    time = game_data['startTime'].strftime('%I:%M %p') + ' ET'
    if game_data['network'] == '':
        game_data['network'] = 'Check local listings or other streaming platforms.'
    network_flair = game_data['network']
    if game_data['network'] in tv_flairs.keys():
        network_flair = tv_flairs[game_data['network']]

    #\n\n###[](#l/discord) [Join Our Discord](https://discord.gg/redditcbb)
    thread = thread + time + '\n\nVenue: ' + game_data['venue'] + ', ' + game_data['city'] + ', ' + game_data['state']

    if game_data['spread'] or game_data['overUnder']:
        thread = thread + '\n\nSpread: ' + game_data['spread'] + ' | O/U: ' + str(game_data['overUnder'])

    thread = thread + "\n\nGame Info: [ESPN](http://www.espn.com/mens-college-basketball/game?gameId=" + game_id + ")"

    thread = thread + '\n\n-----------------------------------------------------------------\n\n**Television:** \n' + network_flair + '\n\n\n**Streams:**\n'
    if game_data['network'] in tv_stream_links.keys():
        thread = thread + tv_stream_links[game_data['network']] + '\n'

    thread = thread + "\n\n-----------------------------------------------------------------"

    if game_data['plays']:
        thread = thread + '\n**Recent Plays:**\n\n' + format_plays(game_data)

    thread = thread + format_boxscore(game_data)
    thread = thread + "\n\n-----------------------------------------------------------------\n\n**Thread Notes:**\n\n- I'm a bot! Don't be afraid to leave feedback!\n\n- Discuss whatever you wish. You can trash talk, but keep it civil.\n\n- Try [reddit stream](" + comment_stream_link + ") to keep up with comments.\n\n- Show your team affiliation - get a team logo by clicking 'Select Flair' on the right."

    thread = thread + " \n\n-----------------------------------------------------------------\n\n###[](#l/twitter) [Follow Our Twitter](https://twitter.com/redditcbb)"
    thread = thread + '\n\n^' + ' ^'.join(('Last Updated: ' + datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')).split())

    title = '[Game Thread] ' + game_data['awayRank'] + game_data['awayTeam'] + ' @ ' + game_data['homeRank'] + game_data['homeTeam'] + ' (' + time + ')'
    return title, thread

def format_plays(game_data):
    away_id = game_data['boxscore']['teams'][0]['team']['id']
    home_id = game_data['boxscore']['teams'][1]['team']['id']

    plays_string = '\n\n'

    plays_header = ['Time', game_data['awayFlair'], game_data['homeFlair'], 'Play']

    plays_string = plays_string + ' | '.join(plays_header) + '\n'
    plays_string = plays_string + '----|' * (len(plays_header)) + '\n'

    for play in game_data['plays']:
        text = play['text']
        away_score = str(play['awayScore'])
        home_score = str(play['homeScore'])
        game_clock = play['clock']['displayValue']

        team_id, flair = '', ''
        if 'team' in play:
            team_id = play['team']['id']

        plays_string = plays_string + ' | '.join([game_clock, away_score, home_score, text]) + '\n'

    return plays_string

def format_boxscore(game_data):
    is_pregame = False
    boxscore = {}

    for team in game_data['boxscore']['teams']:
        name = team['team']['location']
        boxscore[name] = {}
        for data_point in team['statistics']:
            if 'label' in data_point:
                boxscore[name][data_point['label']] = data_point['displayValue']
            if 'abbreviation' in data_point:
                boxscore[name][data_point['abbreviation']] = data_point['displayValue']

        # Not sure if there's a better way to check if this is pre-game or not, but it definitely works!
        is_pregame = 'Streak' in boxscore[name].keys()

    if is_pregame:
        game_stats = ['STRK', 'PTS', 'PA', 'FG%', '3P%', 'REB', 'AST', 'BLK', 'STL', 'ToTO']
    else:
        game_stats = ['FG%', '3P%', 'FT%', 'REB', 'OR', 'AST', 'STL', 'BLK', 'TO', 'PF']

    boxscore_string = '\n\n'
    # Add 'Team' column to beginning of list
    boxscore_string = boxscore_string + 'Team | ' + ' | '.join(game_stats) + '\n'
    # Add the reddit table separator, length of stats + 1 due to manually adding 'Team'
    boxscore_string = boxscore_string + '----|' * (len(game_stats) + 1) + '\n'

    # Doing it this way allows us to keep home/away in order
    boxscore_line = [game_data['awayFlair']]
    for stat in game_stats:
        value = if_exists(boxscore[game_data['awayTeam']], stat, '')
        boxscore_line.append(value)
    boxscore_string = boxscore_string + ' | '.join(boxscore_line) + '\n'

    boxscore_line = [game_data['homeFlair']]
    for stat in game_stats:
        value = if_exists(boxscore[game_data['homeTeam']], stat, '')
        boxscore_line.append(value)
    boxscore_string = boxscore_string + ' | '.join(boxscore_line)

    return boxscore_string

def make_pg_thread(game_id, game_data):
    if game_data['awayRank'] != '':
        game_data['awayRank'] = '#' + str(game_data['awayRank']) + ' '
    if game_data['homeRank'] != '':
        game_data['homeRank'] = '#' + str(game_data['homeRank']) + ' '

    home_won = game_data['homeScore'] > game_data['awayScore']
    ot = ''
    if '/' in game_data['gameClock']:
        ot = ' in ' + game_data['gameClock'].split('/')[-1]

    if home_won:
        title = '[Post Game Thread] ' + game_data['homeRank'] + game_data['homeTeam'] + ' defeats ' + game_data['awayRank'] + game_data['awayTeam'] + ', ' + str(game_data['homeScore']) + '-' + str(game_data['awayScore']) + ot
    else:
        title = '[Post Game Thread] ' + game_data['awayRank'] + game_data['awayTeam'] + ' defeats ' + game_data['homeRank'] + game_data['homeTeam'] + ', ' + str(game_data['awayScore']) + '-' + str(game_data['homeScore']) + ot

    thread = '[Box Score](https://www.espn.com/mens-college-basketball/boxscore?gameId=' + str(game_id) + ')'
    thread = thread + format_linescores(game_data)
    thread = thread + '\n\n[**^' + ' ^'.join(('Index Thread for ' + game_data['startTime'].strftime('%B %d, %Y')).split()) + '**](https://www.reddit.com' + index_permalink + ')'

    return title, thread

def format_linescores(game_data):
    periods = ['1H', '2H'] + [str(i) + 'OT' for i in range(1, len(game_data['awayLinescore']) - 1)] + ['Total']

    linescore_string = '\n\n'
    # Add 'Team' column to beginning of list
    linescore_string = linescore_string + 'Team | ' + ' | '.join(periods) + '\n'
    # Add the reddit table separator, length of stats + 1 due to manually adding 'Team'
    linescore_string = linescore_string + '----|' * (len(periods) + 1) + '\n'

    linescore_string = linescore_string + game_data['awayFlair'] + ' | ' + ' | '.join(game_data['awayLinescore']) + ' | ' + str(sum([int(x) for x in game_data['awayLinescore']])) + '\n'
    linescore_string = linescore_string + game_data['homeFlair'] + ' | ' + ' | '.join(game_data['homeLinescore']) + ' | ' + str(sum([int(x) for x in game_data['homeLinescore']]))

    return linescore_string

def index_thread(games):
    games['order'] = 3
    tv = ['ESPN', 'ESPN2', 'ESPNU', 'ESPNN', 'ACC Network', 'SEC Network', 'FS1', 'FS2', 'ABC', 'BTN', 'CBSSN', 'FOX', 'CBS', 'PAC12', 'NBC', 'TBS', 'TNT', 'truTV', 'USA Net', 'CW NETWORK']
    games.loc[games['network'].isin(tv), 'order'] = 2
    games.loc[games['top25'] == 1, 'order'] = 1
    heading_dict = {1: 'Ranked Games', 2: 'Nationally Televised Games', 3: 'Other Games'}

    index_string = ''
    for order in [1, 2, 3]:
        if (games['order'] == order).sum() == 0:
            continue
        index_string = index_string + '# ' + heading_dict[order] + '\n\n'
        index_string = index_string + ' | '.join(['Time', 'TV', 'KP', 'Away', 'Home', 'KP', 'GT', 'PGT']) + '\n'
        index_string = index_string + '----|' * (8) + '\n'

        for game, row in games[games['order'] == order].iterrows():
            time = row['date'].strftime('%H:%M')

            network_flair = row['network'].replace('|','')
            if row['network'] in tv_flairs.keys():
                network_flair = tv_flairs[row['network']]

            if row['awayRank'] != '':
                row['awayRank'] = '#' + str(row['awayRank']) + ' '
            if row['homeRank'] != '':
                row['homeRank'] = '#' + str(row['homeRank']) + ' '

            if row['gamethread'] == '':
                gamethread = '[Request](https://www.reddit.com/message/compose/?to=cbbBot&subject=request&message=' + game + ')'
                if row['requested'] == 1:
                    gamethread = 'Requested'
                if any([desc in row['status'] for desc in ['FINAL', 'CANCELED', 'POSTPONED', 'FORFEIT']]):
                    gamethread = ''
            else:
                gamethread = '[Thread](https://www.reddit.com' + row['gamethread'] + ')'
            if row['pgthread'] == '':
                pgthread = ''
                #pgthread = '[Request](https://www.reddit.com/message/compose/?to=cbbBot&subject=pgrequest&message=' + game + ')'
            else:
                pgthread = '[Thread](https://www.reddit.com' + row['pgthread'] + ')'

            index_string = index_string + ' | '.join([row['status'], network_flair, row['awayKenpomRank'], row['awayRank'] + row['awayTeam'], row['homeRank'] + row['homeTeam'], row['homeKenpomRank'], gamethread, pgthread]) + '\n'

    index_string = index_string + '\n\n^' + ' ^'.join(('Last Updated: ' + datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')).split())
    return index_string
