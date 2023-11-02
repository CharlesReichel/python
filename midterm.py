import csv
from pathlib import Path


def calculate_shot_conversion_rate(goals, shots, precision=2):
    """Calculates the shot conversion rate (goals divided by shots). The number
    of decimal places to retain when rounding the quotient is specified by the
    < precision > argument. If the < try > block raises an exception (i.e., a
    ZeroDivisionError) the function returns 0.0.

    Parameters:
        goals (int): number of goals scored
        shots (int): number of shots taken
        precision (int): number of decimal places to retain

    Returns:
        float: shot conversion rate
    """
    try:
        return round(goals / shots, precision)
    except ZeroDivisionError:
        return 0.0


def clean_squad(squad):
    """Converts a player's "Squad" value (e.g. "es Spain") to a two-item tuple
    comprising the following items:

    1  Upper case two-letter country abbreviation (e.g., "ES")
    2. squad name (e.g., "Spain")

    Parameters:
        squad (str): comprises a two-letter country abbreviation and squad name

    Returns:
        tuple: "Squad" element converted to a two-item tuple
    """
    return (squad[:2].upper(), squad[3:])


def format_player_position(position):
    """Reformats player's position string by converting the comma (",") delimiter that
    separates multiple positions to a pipe (|), e.g., "MF,DF" -> "MF|DF". This change
    eliminates the need to surround the position string with double quotes when writing the
    value to a CSV file.

    Parameters:
        position (str): player's position string

    Returns:
        str: reformatted position string
    """

    return position.replace(",", "|")  # TODO Implement


def get_multi_position_players(players, pos_idx):
    """Returns players who play multiple positions. Evaluates the "Pos" element
    for the presence of multiple positions (e.g., "DF", "FW", "GK", "MF").

    Parameters:
        players (list): nested list of player data
        pos_idx (int): index value of the "Pos" element

    Returns:
        list: nested list of players who play multiple positions
    """
    multi_position_players = []
    for player in players:  # iterate over each player in the players list
        positions = player[pos_idx].split("|")  # split player's position by pipe
        if len(positions) > 1:  # if player has more than one position
            multi_position_players.append(
                player
            )  # append player to the list of players who play multiple positions

    return multi_position_players


def get_player_shooting_numbers(player, slice_):
    """Returns a player's shots, shots on target, and goals scored. All values
    are converted from strings to integers before being returned to the caller.

    Parameters:
        player (list): a list containing player data
        slice_ (slice): slice() instance required to access the shooting-related
                        elements in the player list.

    Returns:
        list: player's shooting statistics (shots, shots on target, and goals)
    """

    shooting_numbers = player[slice_]  # get the shooting numbers

    for i in range(len(shooting_numbers)):  # iterate over the sequence
        shooting_numbers[i] = int(
            shooting_numbers[i]
        )  # convert string to integer and assign it back

    return shooting_numbers  # return the shooting numbers


def get_team(players, squad_idx, squad):
    """Returns members of a country's team.

    Parameters:
        players (list): nested list of player data
        squad_idx (int): index value of the "Squad" element
        squad (str): country/squad name

    Returns:
        list: team members who represent the < squad >
    """

    team_players = []  # empty list to accumulate players who belong to a certain team

    for player in players:  # iterate over each player in the players list
        if (
            player[squad_idx].lower() == squad.lower()
        ):  # if player's team matches the specified team
            team_players.append(player)  # append player to the list of players in the team

    return team_players


def get_team_names(players, squad_idx):
    """Returns a list of team/squad names that correspond to the countries participating
    in the World Cup. Duplicate names are filtered out of the list returned to the caller.

    Parameters:
        players (list): nested list of player data
        squad_idx (int): index value of the "Squad" element

    Returns:
        list: countries represented by the players in the < players > list
    """

    team_names = []  # create an empty list to accumulate team names

    for player in players:  # loop through each player in the list
        if player[squad_idx] not in team_names:  # if the team name has not been added before
            team_names.append(player[squad_idx])  # add it to the list

    return team_names  # return the list of unique team names


def get_team_shooting_numbers(team, slice_):
    """Returns a team's shot production: shots, shots on target, and goals. All values
    are converted from strings to integers.

    Parameters:
        team (list): nested list containing team/country player data
        slice_ (slice): slice() instance required to access the shooting-related
                        elements in the player list.

    Returns:
        tuple: team's shot production (shots, shots on target, and goals)
    """

    goals_count = 0
    shot_count = 0
    shots_on_target_count = 0

    for player in team:
        goals, shots, shots_on_target = get_player_shooting_numbers(player, slice_)
        goals_count += goals
        shot_count += shots
        shots_on_target_count += shots_on_target

    return goals_count, shot_count, shots_on_target_count


def get_top_scorer(players, gls_idx):
    """Returns the top scorer from the < players > list. Filters out players
    that did not score a goal and excludes them from consideration. Ties between
    top scorers are accommodated.

    Parameters:
        players (list): nested list of player data
        gls_idx (int): index value of a nested list's "Gls" element

    Returns:
        list: nested list of one or more top scorers
    """

    top_scorers = []  # Initialize the accumulator list
    high_score = 0  # Initialize variable for the most goals scored

    for player in players:  # Iterate over the players list
        goals = int(player[gls_idx])  # Convert player's goal score to integer

        if (
            goals > high_score and goals > 0
        ):  # Check if player's goals are the highest and more than zero
            high_score = goals  # Update high_score
            top_scorers = [player]  # Replace the top_scorers list with this player
        elif (
            goals == high_score and goals > 0
        ):  # Check if goals match the high score and are more than zero
            top_scorers.append(player)  # Add this player to the list of top scorers

    return top_scorers  # Return the list of top goal scorers


def read_csv(filepath, encoding="utf-8", newline="", delimiter=","):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """

    with open(filepath, "r", encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data


def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    # 1.1
    filepath = Path("data-2023-fifa_wwc-players.csv").resolve()
    # 1.2
    data = read_csv(filepath)
    # 1.3
    for i in range(len(data)):
        data[i] = data[i][:10]
    1.4
    print(f"\n1.4 data[0] = {data[0]}")  # headers
    print(f"\n1.4 data[-1] = {data[-1]}")  # last player
    assert data[0] == ["Rk", "Player", "Pos", "Squad", "Age", "Born", "90s", "Gls", "Sh", "SoT"]
    assert data[-1] == [
        "619",
        "Claudia Zornoza",
        "MF",
        "es Spain",
        "32",
        "1990",
        "0.4",
        "0",
        "0",
        "0",
    ]

    # 1.5
    headers = data[0]
    players = data[1:]
    # CHALLENGE 02

    # 2.1
    assert "MF|DF" == format_player_position("MF,DF")
    assert "GK" == format_player_position("GK")

    # 2.2
    assert ("NG", "Nigeria") == clean_squad("ng Nigeria")
    assert ("ZA", "South Africa") == clean_squad("za South Africa")

    # CHALLENGE 03

    # 3.1
    pos_idx = headers.index("Pos")
    squad_idx = headers.index("Squad")
    # 3.2
    for player in players:
        player[pos_idx] = format_player_position(player[pos_idx])
        code, squad = clean_squad(player[squad_idx])
        player.insert(squad_idx, code)
        new_squad_idx = squad_idx + 1
        player[new_squad_idx] = squad
    # 3.3
    headers.insert(squad_idx, "Country_Code")
    # 3.4
    squad_idx += 1
    write_csv("stu-players.csv", players, headers)
    # CHALLENGE 04

    # 4.2
    multi_position_players = get_multi_position_players(players, pos_idx)
    # 4.3
    write_csv("stu-players-multi_position.csv", multi_position_players, headers)

    # CHALLENGE 05

    # 5.2
    team_china = get_team(players, squad_idx, "China PR")
    # 5.3
    write_csv("stu-team-china.csv", team_china, headers)
    # 5.5
    team_morocco = get_team(squad="Morocco", squad_idx=squad_idx, players=players)
    # 5.6
    write_csv("stu-team-morocco.csv", team_morocco, headers)

    # CHALLENGE 06

    # 6.2
    countries = get_team_names(players, squad_idx)
    # 6.3
    countries.sort()
    # 6.4
    print(f"\n6.4 countries = {countries}")
    assert len(countries) == 32

    # CHALLENGE 07

    # 7.2
    gls_idx = headers.index("Gls")
    # 7.3
    top_scorers = get_top_scorer(players, gls_idx)
    # 7.4
    print(f"\n7.4 top scorer(s) (n={len(top_scorers)}) = {top_scorers}")

    # CHALLENGE 08

    # 8.1-5
    team_top_scorers = []
    for country in countries:
        team = get_team(players, squad_idx, country)
        top_scorers = get_top_scorer(team, gls_idx)
        team_top_scorers.append(top_scorers)
    # 8.6
    write_csv("stu-team-top_scorers.csv", team_top_scorers, headers)
    # CHALLENGE 09

    # 9.2 UNCOMMENT: built-in slice(< start >, < start >, < step >=None) object in action!
    slice_ = slice(gls_idx, len(headers))  #  equivalent to slice(8, 11)

    # 9.3
    goals, shots, shots_on_target = get_player_shooting_numbers(players[0], slice_)
    # 9.4
    print(
        f"\n9.4 goals = {goals}",
        f"shots = {shots}",
        f"shots_on_target = {shots_on_target}",
        sep="\n",
    )
    assert goals == 1
    assert shots == 10
    assert shots_on_target == 4

    # CHALLENGE 10

    # 10.2-4
    for player in players:
        goals, shots, shots_on_target = get_player_shooting_numbers(player, slice_)

        conversion_rate = calculate_shot_conversion_rate(goals, shots, 3)
        player.append(conversion_rate)

        on_target_conversion_rate = calculate_shot_conversion_rate(
            goals=goals, shots=shots_on_target, precision=3
        )
        player.append(on_target_conversion_rate)
    # 10.5
    headers.extend(["shots_conv_rate", "shots_on_target_conv_rate"])
    # 10.6
    write_csv("stu-players-shooting_efficiency.csv", players, headers)
    # CHALLENGE 11

    # 11.2
    team_headers = [
        "country",
        "goals",
        "shots",
        "shots_on_target",
        "shots_conv_rate",
        "shots_on_target_conv_rate",
    ]
    # 11.3-7
    teams = []

    for country in get_team_names(players, squad_idx):
        # retrieve the current country's team of players
        team = get_team(players, squad_idx, country)

        # retrieve the team's shooting numbers
        goals, shots, shots_on_target = get_team_shooting_numbers(team, slice_)

        # create a list of team's metrics
        team_metrics = [
            country,
            goals,
            shots,
            shots_on_target,
            calculate_shot_conversion_rate(goals, shots, 3),
            calculate_shot_conversion_rate(goals, shots_on_target, 3),
        ]
        # append the team metrics to the teams list
        teams.append(team_metrics)
    # 11.8
    write_csv("stu-team-shooting_efficiency.csv", teams, team_headers)
    # CHALLENGE 12

    # 12.1-2
    for team in teams:
        # convert shots on target conversion rate to float
        conv_rate = float(team[-1])

        # determine rating based on conversion rate
        if conv_rate >= 0.4:
            rating = "Top Tier"
        elif conv_rate >= 0.3:
            rating = "Upper Middle Tier"
        elif conv_rate >= 0.2:
            rating = "Lower Middle Tier"
        else:
            rating = "Bottom Tier"

        # append rating to the team list
        team.append(rating)
    # 12.3
    team_headers.append("efficiency_rating")
    # 12.4 UNCOMMENT: sort by shots on target conversion rate (descending), squad name (ascending)
    teams = sorted(teams, key=lambda x: (-float(x[-2]), x[0]))

    # 12.5
    write_csv("stu-team-shooting-efficiency_ratings.csv", teams, team_headers)


if __name__ == "__main__":
    main()
