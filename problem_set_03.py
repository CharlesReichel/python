# START PROBLEM SET 03

# Setup Code (DO NOT MODIFY)

tv_shows = [
    "Only Murders in the Building | Comedy | 2021 | 8.1 | 99 | Hulu",
    "Reservation Dogs | Crime  | 2021 | 8.1 | 99 | Hulu",
    "Suits | Drama | 2011 | 8.5 | 90 | Netflix",
    "Better Things | Comedy | 2016 | 7.8 | 98 | Hulu",
    "Grey's Anatomy | Drama | 2005 | 7.6 | 84 | hulu",
    "Atlanta | comedy  | 2016 | 8.6 | 99 | Hulu",
    "The Bold Type | Drama | 2017 | 7.8 | 89 | Hulu",
    "Virgin River | Drama | 2019 | 7.4 | 84 | Netflix",
    "What We Do in the Shadows | Horror | 2019 | 8.9 | 92 | Hulu",
    "American Horror Story | Horror | 2011 | 8.0 | 77 | Hulu",
    "Yellowjackets | Horror | 2021 | 7.9 | 100 | Hulu",
    "Bridgerton | Drama | 2020 | 7.3 | 82 | Netflix",
    "Stranger Things | Scifi | 2016 | 8.7 | 96 | Netflix",
    "Dark | Thriller | 2017 | 8.8 | 93 | Netflix",
    "The Queen's Gambit | Drama | 2020 | 8.6 | 92 | Netflix",
    "Mindhunter | Thriller | 2017 | 8.6 | 90 | Netflix",
    "Money Heist | Crime  | 2017 | 8.5 | 90 | Netflix",
    "The Umbrella Academy | Comedy | 2019 | 7.9 | 86 | Netflix",
    "The Witcher | Fantasy | 2019 | 8.2 | 89 | Netflix",
    "Ozark | Crime | 2017 | 8.4 | 89 | Netflix",
    "The Crown | Drama | 2016 | 8.6 | 89 | Netflix",
    "Cobra Kai | Comedy | 2018 | 8.6 | 89 | Netflix",
    "The Good Place | Comedy | 2016 | 8.2 | 97 | Netflix",
    "The Family Man | Thriller | 2019 | 8.7 | 100 | prime",
    "On My Block | Drama | 2018 | 7.9 | 93 | Netflix",
    "Band of Brothers | Drama | 2001 | 9.4 | 97 | Prime",
    "Breaking Bad | Crime | 2008 | 9.5 | 96 | Netflix",
    "Peaky Blinders | Crime  | 2013 | 8.8 | 93 | Netflix",
    "Lost in Space | Scifi | 2018 | 7.3 | 84 | Netflix",
    "The Marvelous Mrs. Maisel | Comedy | 2017 | 8.7 | 89 | Prime",
    "As We See It | Comedy | 2022 | 9.1 | 90 | Prime",
    "The Cleaning Lady | crime  | 2022 | 7.0 | 60 | Prime",
    "The Lord of the Rings: The Rings of Power | Fantasy | 2022 | 6.9 | 84 | Prime",
    "The Wheel of Time | Fantasy | 2021 | 7.1 | 82 | Prime",
    "Fleabag | Drama | 2016 | 8.7 | 100 | Prime",
    "Star Trek: The Next Generation | Scifi | 1987 | 8.7 | 92 | Prime",
    "Panchayat | Comedy | 2020 | 8.9 | 80 | Prime",
    "Severence | Thriller | 2022 | 8.7 | 97 | AppleTV",
    "Trying | Comedy | 2021 | 7.9 | 93 | AppleTV",
    "The Morning Show | Drama | 2019 | 8.2 | 64 | AppleTV",
    "For All Mankind | Scifi | 2019 | 8.0 | 90 | AppleTV",
    "Dickinson | Comedy | 2019 | 7.6 | 92 | AppleTV",
    "See | Scifi | 2019 | 7.6 | 63 | AppleTV",
]

new_tv_shows = [
    ["How I Caught My Killer", "Docu-series", "2023", "5.5", "40", "hulu"],
    ["The Dropout", "Drama", "2022", "7.5", "90", "hulu"],
    ["Inventing Anna", "Drama", "2022", "6.8", "64", "Netflix"],
    ["One Piece", "Action", "2023", "8.5", "85", "netflix"],
    ["The Ultimatum: Marry or Move On", "Reality", "2022", "5.5", "42", "Netflix"],
    ["The Lincoln Lawyer", "Drama", "2022", "7.7", "85", "Netflix"],
    ["Bel-Air", "Drama", "2022", "6.3", "65", "prime"],
    ["The Terminal List", "Drama", "2022", "7.9", "40", "prime"],
    ["The Real Housewives of Dubai", "Reality", "2022", "3.8", "74", "Appletv"],
    ["The Afterparty", "Comedy", "2022", "7.3", "92", "AppleTV"],
    ["Suspicion", "Drama", "2022", "6.2", "48", "AppleTV"],
    ["The Summer I Turned Pretty", "Drama", "2022", "7.4", "74", "Prime"],
    ["Pinecone & Pony", "Adventure", "2022", "8.1", "68", "AppleTV"],
    ["Extraordinary Attorney Woo", "Drama", "2022", "8.7", "100", "netflix"],
]

scifi_tv_shows_check = [
    "Stranger Things | Scifi | 2016 | 8.7 | 96 | Netflix",
    "Lost in Space | Scifi | 2018 | 7.3 | 84 | Netflix",
    "Star Trek: The Next Generation | Scifi | 1987 | 8.7 | 92 | Prime",
    "For All Mankind | Scifi | 2019 | 8.0 | 90 | AppleTV",
    "See | Scifi | 2019 | 7.6 | 63 | AppleTV",
]

netflix_new_tv_shows_check = [
    "Inventing Anna",
    "One Piece",
    "The Ultimatum: Marry or Move On",
    "The Lincoln Lawyer",
    "Extraordinary Attorney Woo",
]

cleaned_tv_shows_check = [
    ["Only Murders in the Building", "Comedy", "2021", 8.1, 99.0, "Hulu"],
    ["Reservation Dogs", "Crime ", "2021", 8.1, 99.0, "Hulu"],
    ["Suits", "Drama", "2011", 8.5, 90.0, "Netflix"],
    ["Better Things", "Comedy", "2016", 7.8, 98.0, "Hulu"],
    ["Grey's Anatomy", "Drama", "2005", 7.6, 84.0, "hulu"],
    ["Atlanta", "comedy ", "2016", 8.6, 99.0, "Hulu"],
    ["The Bold Type", "Drama", "2017", 7.8, 89.0, "Hulu"],
    ["Virgin River", "Drama", "2019", 7.4, 84.0, "Netflix"],
    ["What We Do in the Shadows", "Horror", "2019", 8.9, 92.0, "Hulu"],
    ["American Horror Story", "Horror", "2011", 8.0, 77.0, "Hulu"],
    ["Yellowjackets", "Horror", "2021", 7.9, 100.0, "Hulu"],
    ["Bridgerton", "Drama", "2020", 7.3, 82.0, "Netflix"],
    ["Stranger Things", "Scifi", "2016", 8.7, 96.0, "Netflix"],
    ["Dark", "Thriller", "2017", 8.8, 93.0, "Netflix"],
    ["The Queen's Gambit", "Drama", "2020", 8.6, 92.0, "Netflix"],
    ["Mindhunter", "Thriller", "2017", 8.6, 90.0, "Netflix"],
    ["Money Heist", "Crime ", "2017", 8.5, 90.0, "Netflix"],
    ["The Umbrella Academy", "Comedy", "2019", 7.9, 86.0, "Netflix"],
    ["The Witcher", "Fantasy", "2019", 8.2, 89.0, "Netflix"],
    ["Ozark", "Crime", "2017", 8.4, 89.0, "Netflix"],
    ["The Crown", "Drama", "2016", 8.6, 89.0, "Netflix"],
    ["Cobra Kai", "Comedy", "2018", 8.6, 89.0, "Netflix"],
    ["The Good Place", "Comedy", "2016", 8.2, 97.0, "Netflix"],
    ["The Family Man", "Thriller", "2019", 8.7, 100.0, "prime"],
    ["On My Block", "Drama", "2018", 7.9, 93.0, "Netflix"],
    ["Band of Brothers", "Drama", "2001", 9.4, 97.0, "Prime"],
    ["Breaking Bad", "Crime", "2008", 9.5, 96.0, "Netflix"],
    ["Peaky Blinders", "Crime ", "2013", 8.8, 93.0, "Netflix"],
    ["Lost in Space", "Scifi", "2018", 7.3, 84.0, "Netflix"],
    ["The Marvelous Mrs. Maisel", "Comedy", "2017", 8.7, 89.0, "Prime"],
    ["As We See It", "Comedy", "2022", 9.1, 90.0, "Prime"],
    ["The Cleaning Lady", "crime ", "2022", 7.0, 60.0, "Prime"],
    ["The Lord of the Rings: The Rings of Power", "Fantasy", "2022", 6.9, 84.0, "Prime"],
    ["The Wheel of Time", "Fantasy", "2021", 7.1, 82.0, "Prime"],
    ["Fleabag", "Drama", "2016", 8.7, 100.0, "Prime"],
    ["Star Trek: The Next Generation", "Scifi", "1987", 8.7, 92.0, "Prime"],
    ["Panchayat", "Comedy", "2020", 8.9, 80.0, "Prime"],
    ["Severence", "Thriller", "2022", 8.7, 97.0, "AppleTV"],
    ["Trying", "Comedy", "2021", 7.9, 93.0, "AppleTV"],
    ["The Morning Show", "Drama", "2019", 8.2, 64.0, "AppleTV"],
    ["For All Mankind", "Scifi", "2019", 8.0, 90.0, "AppleTV"],
    ["Dickinson", "Comedy", "2019", 7.6, 92.0, "AppleTV"],
    ["See", "Scifi", "2019", 7.6, 63.0, "AppleTV"],
    ["How I Caught My Killer", "Docu-series", "2023", 5.5, 40.0, "hulu"],
    ["The Dropout", "Drama", "2022", 7.5, 90.0, "hulu"],
    ["Inventing Anna", "Drama", "2022", 6.8, 64.0, "Netflix"],
    ["One Piece", "Action", "2023", 8.5, 85.0, "netflix"],
    ["The Ultimatum: Marry or Move On", "Reality", "2022", 5.5, 42.0, "Netflix"],
    ["The Lincoln Lawyer", "Drama", "2022", 7.7, 85.0, "Netflix"],
    ["Bel-Air", "Drama", "2022", 6.3, 65.0, "prime"],
    ["The Terminal List", "Drama", "2022", 7.9, 40.0, "prime"],
    ["The Real Housewives of Dubai", "Reality", "2022", 3.8, 74.0, "Appletv"],
    ["The Afterparty", "Comedy", "2022", 7.3, 92.0, "AppleTV"],
    ["Suspicion", "Drama", "2022", 6.2, 48.0, "AppleTV"],
    ["The Summer I Turned Pretty", "Drama", "2022", 7.4, 74.0, "Prime"],
    ["Pinecone & Pony", "Adventure", "2022", 8.1, 68.0, "AppleTV"],
    ["Extraordinary Attorney Woo", "Drama", "2022", 8.7, 100.0, "netflix"],
]

crime_genre_check = [
    ["Reservation Dogs", "2021", 99.0],
    ["Money Heist", "2017", 90.0],
    ["Ozark", "2017", 89.0],
    ["Breaking Bad", "2008", 96.0],
    ["Peaky Blinders", "2013", 93.0],
    ["The Cleaning Lady", "2022", 60.0],
]


# End setup code


# PROBLEM 1
print("\nPROBLEM 01")

# TODO 1.1
scifi_tv_shows = []

# TODO 1.2
for show in tv_shows:
    if "scifi" in show.lower():
        scifi_tv_shows.append(show)

#print(f"\n1.1: scifi_tv_shows = {scifi_tv_shows}")
#assert scifi_tv_shows == scifi_tv_shows_check

# TODO 1.3
netflix_new_tv_shows = []

# TODO 1.4
for i in range(len(new_tv_shows)):
    if "netflix" in new_tv_shows[i][5].lower():
        netflix_new_tv_shows.append(new_tv_shows[i][0])

#print(f"\n1.2: netflix_new_tv_shows = {netflix_new_tv_shows}")
#assert netflix_new_tv_shows == netflix_new_tv_shows_check


# PROBLEM 2
print("\nPROBLEM 02")

# TODO 2.1
cleaned_tv_shows = []

# TODO 2.2
for show in tv_shows:
    show_info = show.split(" | ")
    cleaned_tv_shows.append(show_info)

#print(f"\n2.2: cleaned_tv_shows (first 5 elements) = {cleaned_tv_shows[:5]}")

# TODO 2.3
for i in range(len(cleaned_tv_shows)):
    cleaned_tv_shows[i][3] = float(cleaned_tv_shows[i][3])
    cleaned_tv_shows[i][4] = float(cleaned_tv_shows[i][4])


# print(f"\n2.3: cleaned_tv_shows (first 5 elements) = {cleaned_tv_shows[:5]}")

# TODO 2.4
for i in range(len(new_tv_shows)):
    new_tv_shows[i][3] = float(new_tv_shows[i][3])
    new_tv_shows[i][4] = float(new_tv_shows[i][4])

cleaned_tv_shows.extend(new_tv_shows)

# print(f"\n2.4: new_tv_shows (first 5 elements) = {new_tv_shows[:5]}")

# print(f"\n2.4: cleaned_tv_shows (first 5 elements) = {cleaned_tv_shows[:5]}")
# assert cleaned_tv_shows == cleaned_tv_shows_check

# PROBLEM 3
print("\nPROBLEM 03")

# TODO 3.1
crime_genre = []

# TODO 3.2
for i in cleaned_tv_shows:
    crime = i[1].lower().strip()
    if crime == "crime":
        info = [i[0],i[2],i[4]]
        crime_genre.append(info)
print(f"\n3.2: crime genre = {crime_genre}")
# assert crime_genre == crime_genre_check

# PROBLEM 4
print("\nPROBLEM 04")

# TODO 4.1
total_rotten_tomato_ratings = 0

# TODO 4.2
for i in cleaned_tv_shows:
    total_rotten_tomato_ratings += i[4]
#print(f"\n4.2: total_ratings = {total_rotten_tomato_ratings}")

# TODO 4.3
avg_rotten_tomato_ratings = round(total_rotten_tomato_ratings / len(cleaned_tv_shows),1)

print(f"\n4.3: average rating = {avg_rotten_tomato_ratings}")

# PROBLEM 5
print("\nPROBLEM 05")

# TODO 5.1
above_avg_rotten_tomato_ratings = []
# TODO 5.2
for i in cleaned_tv_shows:
    if i[4] > avg_rotten_tomato_ratings:
        above_avg_rotten_tomato_ratings.append(i[0])
# print(f"\n5.2: above average shows (first 5 elements) = {above_avg_rotten_tomato_ratings[:5]}")


# PROBLEM 6
print("\nPROBLEM 06")

# TODO 6.1
select_content = []
non_select_content = []
# TODO 6.2
for i in range(len(cleaned_tv_shows)):
    if cleaned_tv_shows[i][5].lower() == "netflix":
        select_content.append(cleaned_tv_shows[i])
    else:
        non_select_content.append(cleaned_tv_shows[i])
# print(f"\n6.2: select_content (first 5 elements) = {select_content[:5]}")
# print(f"\n6.2: non_select_content (first 5 elements) = {non_select_content[:5]}")


# PROBLEM 7
print("\nPROBLEM 07")

# TODO 7.1
max_year = 0
min_year = 3000

newest_show = None
oldest_show = None

# TODO 7.2
for i in cleaned_tv_shows:
    if int(i[2]) > max_year:
        max_year = int(i[2])
        newest_show = i[0]
    if int(i[2]) < min_year:
        min_year = int(i[2])
        oldest_show = i[0]
# print(f"\n7.2: The oldest show is {oldest_show} and the newest show is {newest_show}.")

# PROBLEM 8
print("\nPROBLEM 08")

# TODO 8.1
genres = []
# TODO 8.2
for i in range(len(cleaned_tv_shows)):
    genre = cleaned_tv_shows[i][1].lower().strip()
    if genre not in genres:
        genres.append(genre)
#print(f"\n8.2: unique genres list = {genres}")


# END PROBLEM SET 03
