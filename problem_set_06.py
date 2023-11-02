import csv
from pathlib import Path

# WARNING: Ensure that "import csv" and "from pathlib import Path" are at the top of the file.
# Setup Code (DO NOT MODIFY)

registered_voters_check = [
    ['county', 'city_township', 'voting_equipment',
        'precincts', 'registered_voters', 'active_voters'],
    ['Washtenaw', 'Ann Arbor', 'Hart Verity Scan/Touch Writer', '53', '110056', '76266']
]

election_results_check = [
    ['ElectionDate', 'OfficeCode(Text)', 'DistrictCode(Text)', 'StatusCode', 'CountyCode', 'CountyName',
        'OfficeDescription', 'PartyOrder', 'PartyName', 'PartyDescription', 'CandidateID', 'CandidateLastName',
        'CandidateFirstName', 'CandidateMiddleName', 'CandidateFormerName', 'CandidateVotes', 'WriteIn(W)/Uncommitted(Z)',
        'Recount(*)', 'Nominated(N)/Elected(E)'],
    ['11/8/22', '2', '0', '0', '81', 'WASHTENAW', 'Governor 4 Year Term (1) Position', '1', 'DEM',
        'Democratic', '518014', 'Whitmer', 'Gretchen', '', '', '135904', '', '', 'E']
]

election_results_check_2 = [
    ['11/8/22', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 1, 'DEM', 'Democratic',
     518014, 'Whitmer', 'Gretchen', '', '', 135904, '', '', 'E'],
    ['11/8/22', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 2, 'REP', 'Republican',
     520065, 'Dixon', 'Tudor', 'M.', '', 42804, '', '', '']
]

fewest_precincts_check = [
    ['Washtenaw', 'Bridgewater Township',
        'Hart Verity Scan/Touch Writer', 1, 1463, 1339],
    ['Washtenaw', 'Freedom Township', 'Hart Verity Scan/Touch Writer', 1, 1295, 1181],
    ['Washtenaw', 'Lyndon Township', 'Hart Verity Scan/Touch Writer', 1, 2269, 2160],
    ['Washtenaw', 'Milan city', 'Hart Verity Scan/Touch Writer', 1, 3140, 2877],
    ['Washtenaw', 'Saline Township', 'Hart Verity Scan/Touch Writer', 1, 1886, 1763],
    ['Washtenaw', 'Sharon Township', 'Hart Verity Scan/Touch Writer', 1, 1658, 1526],
    ['Washtenaw', 'Sylvan Township', 'Hart Verity Scan/Touch Writer', 1, 3029, 2790]
]

fewest_votes_check = [
    ['11/8/22', 8, 4800, 0, 81, 'WASHTENAW', '48th District Representative in State Legislature 2 Year Term (1) Position',
        6, 'GRN', 'Green', 520860, 'Borregard', 'Eric', '', '', 303, '', '', '']
]

most_active_unit_check = ['York Township']

percent_check = 98.0

vote_totals_check = [
    ['Governor', 2, 135904, 42804, 1277, 451],
    ['Representative in Congress', 6, 132859, 44782, 0, 0],
    ['State Senator', 7, 129330, 46288, 0, 0],
    ['District Representative in State Legislature', 8, 128806, 46342, 0, 303],
    ['Regent of the University of Michigan', 10, 238196, 84896, 4690, 5048]
]
# End of Setup Code

print("PROBLEM SET 6\n")


def clean_data(data, strip=False, character=None):
    """
    Receives a list of str elements and leverages two (2) utility
    functions (`trim_str()` and `convert_to_int()`) to clean the list elements.

    If strip=False, only convert the relevant str elements in the list to int.
    If strip=True, strip unnecessary characters from the str elements
        before converting to int.

    Parameters:
        data (list): A list of str elements that represent election result data.
        strip (Bool): Default False. If True, leverage the appropriate function to
                        remove any leading and trailing characters with spaces as
                        the default.
        character (str): Default None. When None, the trim_str() function
                         will strip leading and trailing spaces from each string element.
                         Otherwise, it will strip the passed in character.
    Returns:
        (list): A "cleaned" list of elements that represent election result data.
    """
    for i in range(len(data)):
        if strip:
            data[i] = trim_str(data[i], character)
        data[i] = convert_to_int(data[i])
    return data


def convert_to_int(value):
    """
    Receives a str value and attempts to convert it to an integer. If possible, the value is converted and
    immediately returned. Otherwise, the value is immediately returned unchanged.

    Parameter:
        value (str): a str that represents an element of election data.
    Returns:
        value (str | int): a str or int that represents an element of election data.
    """
    try:
        return int(value)
    except ValueError:
        return value


def find_min_values(column, headers, data):
    """
    Receives a single column name, list of column headers, and a list of
    lists representing election data. Finds the list (or multiple lists in
    the case of a tie) with the smallest value for the specified column.

    Parameters:
        column (str): A str element representing a specified column name.
        headers (list): A list of str elements representing column headers.
        data (list): A list of nested lists that contain elements representing
                    election results data.
    Returns:
        smallest_unit (list): A list containing the list or lists that have
                              the smallest value for the column of interest.
    """
    column_index = headers.index(column)
    smallest_value = float("inf")
    smallest_unit = []

    for row in data:
        if row[column_index] < smallest_value:
            smallest_value = row[column_index]
            smallest_unit = [row]
        elif row[column_index] == smallest_value:
            smallest_unit.append(row)
    return smallest_unit


# TODO 6.1: Define a function
def get_active_voters(data, percent=False):
    """
    Calculates the percentage or decimal representation of active voters against total registered voters for a given city or township.

    Parameters:
        data (list): A list of elements representing voter registration data for a city or township.
        percent (Bool): Default False. If True, return the calculation as a percentage, otherwise, as a decimal.

    Returns:
        float: The percentage (if percent=True) or decimal (if percent=False) of active voters.
    """
    active_voters = int(data[-1])
    registered_voters = int(data[-2])

    ratio = active_voters / registered_voters

    if percent:
        return round(ratio * 100, 1)
    else:
        return round(ratio, 2)

# TODO 6.4: Define a function
def find_most_active_unit(data, percent=True):
    """
    Finds the city or township with the most active voters (as a percent of registered voters).

    Parameters:
        data (list): A list of lists, each representing voter registration data for a city or township.
        percent (Bool): Default True. If True, calculate active voters as a percentage, otherwise, as a decimal.

    Returns:
        tuple: A tuple comprising the name(s) of the city or township with the most active voters and the corresponding percentage.
    """
    highest_percent = 0
    most_active_unit = []

    for unit in data:
        percent_active = get_active_voters(unit, percent)

        if percent_active > highest_percent:
            highest_percent = percent_active
            most_active_unit = [unit[1]]
        elif percent_active == highest_percent:
            most_active_unit.append(unit[1])
    return most_active_unit, highest_percent

# TODO 7.1: Define a function
def get_votes_by_party(results, headers, office_code):
    office_code_index = headers.index('OfficeCode(Text)')
    party_name_index = headers.index('PartyName')
    vote_count_index = headers.index('CandidateVotes')

    democratic_votes = 0
    republican_votes = 0
    libertarian_votes = 0
    green_votes = 0

    for result in results:
        if result[office_code_index] == office_code:
            if result[party_name_index] == 'DEM':
                democratic_votes += int(result[vote_count_index])
            elif result[party_name_index] == 'REP':
                republican_votes += int(result[vote_count_index])
            elif result[party_name_index] == 'LIB':
                libertarian_votes += int(result[vote_count_index])
            elif result[party_name_index] == 'GRN':
                green_votes += int(result[vote_count_index])

    return democratic_votes, republican_votes, libertarian_votes, green_votes

def read_csv(filepath, encoding="utf-8-sig"):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a
    list of lists, wherein each nested list represents a single row from the
    input file.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file

    Returns:
        data (list): list of nested "row" lists
    """
    with open(filepath, "r", encoding=encoding) as file_obj:
        data = []
        reader = csv.reader(file_obj)
        for row in reader:
            data.append(row)
        return data


def trim_str(value, substring=None):
    """
    This function receives a string with election
    information. The function checks if the optional argument substring has been
    passed. If the default parameter is kept (substring=None), then extra spaces
    on either side of the string are stripped. If a different substring is
    passed as an argument, that substring is stripped from the strings
    instead.

    Parameters:
        value (str): a str that represents an element of election data.
        substring (str): Default=None; a string to be passed to .strip().
                         Indicates which substring(s) should be stripped from
                         the strings in unit_data.
    Returns:
        None
    """
    try:
        return value.strip(substring)
    except TypeError:
        return value


def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be
                        created)
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
    """
    Serves as the main entry point of the program.
    """

    print("\nProblem 1\n")
    # PROBLEM 1

    # TODO 1.4 1.5
    parent_path = Path().resolve()
    voters_path = parent_path / 'data-washtenaw_registered_voters.csv'

    # TODO 1.6
    registered_voters = read_csv(voters_path)
    assert registered_voters[:2] == registered_voters_check
    print(f"Registered Voters in Washtenaw County: {registered_voters[:5]}")

    # TODO 1.7
    election_path = parent_path / 'data-washtenaw_2022_election_results.csv'

    # TODO 1.8
    election_results = read_csv(election_path)
    assert election_results[:2] == election_results_check
    print(f"\n2022 General Election Results for Washtenaw County: {election_results[:5]}")

    # TODO 1.9
    registered_headers = registered_voters[0]
    registered_voters = registered_voters[1:]
    print(f"\nRegistered Voters: {registered_voters[:5]}")
    assert registered_headers not in registered_voters

    # TODO 1.10
    election_headers = election_results[0]
    election_results = election_results[1:]
    print(f"\nElection Results: {election_results[:5]}")
    assert election_headers not in election_results

    print("\nProblem 2\n")
    # PROBLEM 2

    # TODO 2.2
    assert convert_to_int("45") == 45
    assert convert_to_int("2000") == 2000

    print("\nProblem 3\n")
    # PROBLEM 3

    # TODO 3.2
    assert trim_str("  Gretchen   ") == "Gretchen"
    assert trim_str("$ELECTION$", "$") == "ELECTION"

    print("\nProblem 4\n")
    # PROBLEM 4

    # TODO 4.4: call function
    for i in range(len(registered_voters)):
        registered_voters[i] = clean_data(registered_voters[i])
    # TODO 4.5: call function
    for i in range(len(election_results)):
        election_results[i] = clean_data(election_results[i], strip=True, character="-")
    assert election_results[:2] == election_results_check_2
    print(f"\nClean Election Results Data: {election_results[:5]}")

    print("\nProblem 5\n")
    # PROBLEM 5

    # TODO 5.3, 5.4
    fewest_precincts = find_min_values("precincts", registered_headers, registered_voters)
    print(f"The gov unit(s) with the fewests precincts: {fewest_precincts}")
    assert fewest_precincts == fewest_precincts_check

    # TODO 5.5, 5.6
    fewest_votes = find_min_values("CandidateVotes", election_headers, election_results)
    print(f"\nThe candidate(s) with the fewest votes: {fewest_votes}")
    assert fewest_votes == fewest_votes_check

    print("\nProblem 6\n")
    # PROBLEM 6

    # TODO 6.3
    assert get_active_voters(registered_voters[2]) == 0.91
    assert get_active_voters(registered_voters[10], True) == 95.2
    assert get_active_voters(registered_voters[16], True) == 89.8

    # TODO 6.6, 6.7
    most_active_unit, percent = find_most_active_unit(registered_voters)
    print(f"The unit(s) with the highest percentage of active voters: {most_active_unit}.")
    print(f"{percent}% of registered voters in that unit are active.")
    assert most_active_unit == most_active_unit_check
    assert percent == percent_check

    print("\nProblem 7\n")
    # PROBLEM 7

    # WARNING: Do not edit the two lists below
    vote_totals_headers = [
        "Office Name",
        "Office Code",
        "Votes for Democrat",
        "Votes for Republican",
        "Votes for Libertarian",
        "Votes for Green",
    ]
    vote_totals = [
        ["Governor", 2],
        ["Representative in Congress", 6],
        ["State Senator", 7],
        ["District Representative in State Legislature", 8],
        ["Regent of the University of Michigan", 10],
    ]

    # TODO 7.3, 7.4
    for i in range(len(vote_totals)):
        office_name, office_code = vote_totals[i]
        dem_votes, rep_votes, lib_votes, green_votes = get_votes_by_party(election_results, election_headers, office_code)
        vote_totals[i].extend([dem_votes, rep_votes, lib_votes, green_votes])
    print(f"7.3: The vote totals by party and office: {vote_totals}")
    assert vote_totals == vote_totals_check

    print("\nProblem 8\n")
    # PROBLEM 8

    # TODO 8.2
    write_csv("stu-election_votes_by_party.csv", vote_totals, headers=vote_totals_headers)
# WARN: do not modify or remove the following if statement.

if __name__ == "__main__":
    main()
