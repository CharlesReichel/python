# START PROBLEM SET 5

# Setup Code (DO NOT MODIFY)

# fmt: off
club_events = [
    "Host Organization; Event Name; Date; Start Time; Duration; Location; Theme",
    "Star Wars Fan Club; Star Wars Ahsoka Watch Party; 2023/9/28; 7 PM; 1.5 hours; Mason Hall; Social",
    "UNICEF at the University of Michigan; UNICEF at The University of Michigan General Meeting; 2023/10/3; 6 PM; 1 hour; Rackham; Community service",
    "Swing Ann Arbor; Swing Ann Arbor Swing 1: Lindy Hope Essentials; 2023/10/3; 7:15 PM; 1 hour; Mason Hall; Class/instruction",
    "Women's Ice Hockey; University of Michigan Women's Ice Hockey vs Lake State Superior University Weekend Series; 2023/10/7; 7 PM; 2 hours; Taffy Abel Arena; Sport event",
    "Shotokan Karate at University of Michigan; Karate Practice; 2023/10/8; 1 PM; 2 hours; Intramural Sports Building; Exercise/Fitness",
    "Society of Disabled and Neurodiverse Students; SDNS Support Group; 2023/10/9; 6 PM; 2 hours; Michigan Union; Social",
    "A2 Movimiento Latino; Bachata Class; 2023/10/10; 6:30 PM; 3 hours; Phoenix Center; Class/instruction",
    "Swing Ann Arbor; Swing Ann Arbor Swing 2: Swingout Bootcamp; 2023/10/10; 8:30 PM; 1 hour; Mason Hall; Class/instruction",
    "Bujinkan Budo Club; Bujinkan Budo Training Session; 2023/10/11; 8 PM; 1.5 hours; Intramural Sports Building; Exercise/Fitness",
    "One Thousand Schools; General Meeting!; 2023/10/11; 8 PM; 1 hour; East Quad; Community service",
    "Women's Ice Hockey; University of Michigan Women's Ice Hockey vs GVSU; 2023/10/13; 6:30 PM; 2 hours; Yost Ice Arena; Sport event",
    "Michigan Sailing Team; David Lee Arnoff; 2023/10/13; 8 AM; 5 hours; Geneva, NY; Sport event",
    "Club Tennis Team; Fall Break Dual Match; 2023/10/14; 12 PM; 4 hours; University of Tennessee-Knoxville; Sport event",
    "A2 Movimiento Latino; Casino Class; 2023/10/17; 6:30 PM; 3 hours; Phoenix Center; Class/instruction",
    "American Nuclear Society Student Chapter at the University of Michigan; ANS FermiLab Tour; 2023/10/21; 8 AM; 2 hours; Fermilab; Informational",
    "A2 Movimiento Latino; On 2 Class; 2023/10/24; 6:30 PM; 3 hours; Phoenix Center; Class/instruction",
    "Michigan Men's&Women's Club Wrestling; Fall Brawl; 2023/10/28; 11 AM; 4 hours; Mott Community College; Sport event",
    "Michigan Sailing Team; Cedar Fest; 2023/10/27; 12 PM; 1 hour; Lansing, MI; Sport event",
    "Men's Rowing; Bald Eagle Regatta; 2023/11/4; 9 AM; 9 hours; Eagle Creek Park; Sport event",
    "Society of Disabled and Neurodiverse Students; SDNS Crafting & Studying Night; 2023/11/30; 6 PM; 2 hours; Michigan Union; Social",
    "Women's Ice Hockey; University of Michigan Women's Ice Hockey vs MSU; 2024/1/20; 3:30 PM; 2.5 hours; Centre Ice Arena; Sport event",
]


club_events_check = [['Host Organization', 'Event Name', 'Date', 'Start Time', 'Duration', 'Location', 'Theme'], ['Star Wars Fan Club', 'Star Wars Ahsoka Watch Party', '2023/9/28', '7 PM', '1.5 hours', 'Mason Hall', 'Social'], ['UNICEF at the University of Michigan', 'UNICEF at The University of Michigan General Meeting', '2023/10/3', '6 PM', '1 hour', 'Rackham', 'Community service'], ['Swing Ann Arbor', 'Swing Ann Arbor Swing 1: Lindy Hope Essentials', '2023/10/3', '7:15 PM', '1 hour', 'Mason Hall', 'Class/instruction'], ["Women's Ice Hockey", "University of Michigan Women's Ice Hockey vs Lake State Superior University Weekend Series", '2023/10/7', '7 PM', '2 hours', 'Taffy Abel Arena', 'Sport event'], ['Shotokan Karate at University of Michigan', 'Karate Practice', '2023/10/8', '1 PM', '2 hours', 'Intramural Sports Building', 'Exercise/Fitness'], ['Society of Disabled and Neurodiverse Students', 'SDNS Support Group', '2023/10/9', '6 PM', '2 hours', 'Michigan Union', 'Social'], ['A2 Movimiento Latino', 'Bachata Class', '2023/10/10', '6:30 PM', '3 hours', 'Phoenix Center', 'Class/instruction'], ['Swing Ann Arbor', 'Swing Ann Arbor Swing 2: Swingout Bootcamp', '2023/10/10', '8:30 PM', '1 hour', 'Mason Hall', 'Class/instruction'], ['Bujinkan Budo Club', 'Bujinkan Budo Training Session', '2023/10/11', '8 PM', '1.5 hours', 'Intramural Sports Building', 'Exercise/Fitness'], ['One Thousand Schools', 'General Meeting!', '2023/10/11', '8 PM', '1 hour', 'East Quad', 'Community service'], ["Women's Ice Hockey", "University of Michigan Women's Ice Hockey vs GVSU", '2023/10/13', '6:30 PM', '2 hours', 'Yost Ice Arena', 'Sport event'], ['Michigan Sailing Team', 'David Lee Arnoff', '2023/10/13', '8 AM', '5 hours', 'Geneva, NY', 'Sport event'], ['Club Tennis Team', 'Fall Break Dual Match', '2023/10/14', '12 PM', '4 hours', 'University of Tennessee-Knoxville', 'Sport event'], ['A2 Movimiento Latino', 'Casino Class', '2023/10/17', '6:30 PM', '3 hours', 'Phoenix Center', 'Class/instruction'], ['American Nuclear Society Student Chapter at the University of Michigan', 'ANS FermiLab Tour', '2023/10/21', '8 AM', '2 hours', 'Fermilab', 'Informational'], ['A2 Movimiento Latino', 'On 2 Class', '2023/10/24', '6:30 PM', '3 hours', 'Phoenix Center', 'Class/instruction'], ["Michigan Men's&Women's Club Wrestling", 'Fall Brawl', '2023/10/28', '11 AM', '4 hours', 'Mott Community College', 'Sport event'], ['Michigan Sailing Team', 'Cedar Fest', '2023/10/27', '12 PM', '1 hour', 'Lansing, MI', 'Sport event'], ["Men's Rowing", 'Bald Eagle Regatta', '2023/11/4', '9 AM', '9 hours', 'Eagle Creek Park', 'Sport event'], ['Society of Disabled and Neurodiverse Students', 'SDNS Crafting & Studying Night', '2023/11/30', '6 PM', '2 hours', 'Michigan Union', 'Social'], ["Women's Ice Hockey", "University of Michigan Women's Ice Hockey vs MSU", '2024/1/20', '3:30 PM', '2.5 hours', 'Centre Ice Arena', 'Sport event']]

# fmt: on
get_duration_check = 1.5

get_event_location_check = "Mason Hall"

shortest_club_event_check = [
    ("UNICEF at The University of Michigan General Meeting", 1.0),
    ("Swing Ann Arbor Swing 1: Lindy Hope Essentials", 1.0),
    ("Swing Ann Arbor Swing 2: Swingout Bootcamp", 1.0),
    ("General Meeting!", 1.0),
    ("Cedar Fest", 1.0),
]

intramural_events_check = ["Karate Practice", "Bujinkan Budo Training Session"]

# fmt: off
specified_theme_events_check = [['Karate Practice', 'Bujinkan Budo Training Session'], ['Star Wars Ahsoka Watch Party', 'SDNS Support Group', 'SDNS Crafting & Studying Night'], ["University of Michigan Women's Ice Hockey vs Lake State Superior University Weekend Series", "University of Michigan Women's Ice Hockey vs GVSU", 'David Lee Arnoff', 'Fall Break Dual Match', 'Fall Brawl', 'Cedar Fest', 'Bald Eagle Regatta', "University of Michigan Women's Ice Hockey vs MSU"]]
# fmt: on

evening_events_check = [
    "Star Wars Ahsoka Watch Party",
    "University of Michigan Women's Ice Hockey vs Lake State Superior University Weekend Series",
]

num_events_for_a2_check = 3

social_event_1_check = ("Star Wars Ahsoka Watch Party", "2023/9/28", "Social")
social_event_2_check = ("SDNS Support Group", "2023/10/9", "Social")
social_event_3_check = ("SDNS Crafting & Studying Night", "2023/11/30", "Social")

# End setup code


# PROBLEM 01
# 1.1
def convert_str_to_list(element, separator):
    return element.split(separator)

# TODO 1.2
for i in range(len(club_events)):
    club_events[i] = convert_str_to_list(club_events[i], '; ')


# print(f"\n1.2 club_events = {club_events}")
# assert club_events == club_events_check


# PROBLEM 02
# TODO 2.1
def get_duration(event_info):
    duration_str = event_info[4]  # duration information is at index 4 of event_info list
    duration_float = float(duration_str.split()[0])  # split the string and convert the first part to float
    return duration_float

# TODO 2.2
def get_event_location(event_info):
    location_str = event_info[5]  # location information is at index 5 of event_info list
    return location_str

# print(f"\n2.1 First club duration is {get_duration(club_events[1])}")
# print(f"\n2.2 First club event location is {get_event_location(club_events[1])}")

# assert get_duration(club_events[1]) == get_duration_check
# assert get_event_location(club_events[1]) == get_event_location_check


# PROBLEM 03
# TODO 3.1
def event_with_shortest_duration(club_events):
    shortest_event = []
    shortest_duration = 100
    for event in club_events[1:]:  # skip the header
        duration = get_duration(event)
        if duration < shortest_duration:
            shortest_duration = duration
            shortest_event = [(event[1], duration)]  # event[1] is event name
        elif duration == shortest_duration:
            shortest_event.append((event[1], duration))
    return shortest_event
# TODO 3.2
shortest_club_event = event_with_shortest_duration(club_events)

# print(f"\n3.2 Shortest duration event(s): {shortest_club_event}")
# assert shortest_club_event == shortest_club_event_check


# PROBLEM 04
# TODO 4.1
def categorize_events_by_location(club_events, location):
    events_by_location = []

    for event in club_events[1:]:  # skip the header
        event_location = get_event_location(event)
        if event_location == location:
            events_by_location.append(event[1])  # append the event name
    return events_by_location

# TODO 4.2
intramural_events = categorize_events_by_location(club_events, "Intramural Sports Building")

# print(f"\n4.2 Intramural Events = {intramural_events}")
# assert intramural_events == intramural_events_check


# PROBLEM 05
# TODO 5.1
def has_theme(event, theme):
    if theme.lower() in event[-1].lower():
        return True
    else:
        return False

# TODO 5.2
def categorize_events_by_theme(club_events, theme):
    events_by_theme = []

    for event in club_events[1:]:
        if has_theme(event, theme):
            events_by_theme.append(event[1])

    return events_by_theme

themes = ["exercise/fitness", "Social", "sport event"]

# TODO 5.3
specified_theme_events = []

# TODO 5.4
for theme in themes:
    specified_theme_events.append(categorize_events_by_theme(club_events, theme))

# print(f"\n5.4 List of events for specified themes = {specified_theme_events}")
# assert specified_theme_events == specified_theme_events_check


# PROBLEM 06
# TODO 6.1
def categorize_events_by_time(club_events, time='7 PM', duration=1):
    events_by_time = []
    for event in club_events[1:]:
        if event[3] == time and get_duration(event) >= duration:
            events_by_time.append(event[1])
    return events_by_time

# TODO 6.2
evening_events = categorize_events_by_time(club_events)

# print(f"\n6.2 Events in the evening = {evening_events}")
# assert evening_events == evening_events_check


# PROBLEM 07
# TODO 7.1
def calculate_num_events(club_events, host_org):
    num_events = 0
    for event in club_events[1:]:
        if event[0] == host_org:
            num_events += 1
    return num_events

# TODO 7.2
num_events_for_a2 = calculate_num_events(club_events, "A2 Movimiento Latino")

# print(f"\n7.2 Number of events by A2 Movimiento Latino = {num_events_for_a2}")
# assert num_events_for_a2 == num_events_for_a2_check


# PROBLEM 08
# TODO 8.1
def categorize_events_by_specific_theme(club_events, theme):
    events_at_theme = []

    for event in club_events[1:]:
        event_theme = event[-1]
        if event_theme.lower() == theme.lower():
            events_at_theme.append((event[1], event[2], event[-1]))

    return events_at_theme

# TODO 8.2
social_events = categorize_events_by_specific_theme(club_events, "social")

# TODO 8.3
social_event_1, social_event_2, social_event_3 = social_events

# print(f"\n8.3 Social events are {social_event_1}, {social_event_2} and {social_event_3}")
# assert social_event_1 == social_event_1_check
# assert social_event_2 == social_event_2_check
# assert social_event_3 == social_event_3_check

# END PROBLEM SET
