# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    '''
    Input: parameters title, genre, and rating
    Output: Returns a dictionary with the parameters as values, with
    each key defined as a string of the same parameter name.
    If a parameter is missing, no dictionary is created.
    '''
    new_movie = {"title" : title, "genre" : genre, "rating" : rating}
    if new_movie["title"] == None or new_movie["genre"] == None \
    or new_movie["rating"] == None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    '''
    Input: user_data (a dictionary with key "watched" and a list
    as the value), and movie (a dictionary)
    Output: Returns updated user_data dictionary, with the dictionary
    movie appended to the list in the value of "watched".
    '''
    user_data = {
        "watched": [movie]
    }
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Input: user_data (a dictionary with key "watchlist" and a list
    as the value), and movie (a dictionary)
    Output: Returns updated user_data dictionary, with the dictionary
    movie appended to the list in the value of "watchlist".
    '''
    user_data = {
        "watchlist": [movie]
    }
    return user_data

def watch_movie(user_data, movie_to_watch):
    '''
    Input: user_data (a dictionary with keys "watched" and "watchlist",
    with lists as their values, and movie-to-watch (a dictionary)
    Output: Returns updated user_data dictionary, with the dictionary
    movie-to-watch appended to "watched" and removed from the "watchlist".
    '''
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie_to_watch:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''
    Input: user_data (a dictionary with keys "watched" and "watchlist",
    with lists as their values). Each element of the lists "watched" 
    and "watchlist" is a dictionary that contains details about a movie.
    Output: Returns the average rating of all watched movies (a float).
    '''
    total_rating = 0
    average = 0
    watched_list_length = len(user_data["watched"])
    if watched_list_length == 0:
        return average
    else:
        for movie in range(watched_list_length):
            total_rating += user_data["watched"][movie]["rating"]
            average = total_rating / watched_list_length
    return average

def get_most_watched_genre(user_data):
    '''
    Input: user_data (a dictionary with keys "watched" and "watchlist",
    with lists as their values). Each element of the lists "watched" 
    and "watchlist" is a dictionary that contains details about a movie.
    Output: Returns the most commonly watched genre of the "watched" 
    list (a string). Does not account for two equally popular genres.
    '''
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_counting_dict = {}
        for movie in range(len(user_data["watched"])):
            if user_data["watched"][movie]["genre"] not in genre_counting_dict:
                genre_counting_dict[user_data["watched"][movie]["genre"]] = 1
            else:
                genre_counting_dict[user_data["watched"][movie]["genre"]] += 1
    popular_genre = max(genre_counting_dict, key = genre_counting_dict.get)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    '''
    Input: user_data (a dictionary with keys "watched" and "friends",
    with lists as their values). Elements of "watched" list are dictionaries
    of movies. Each element of "friends" list is a dictionary with key
    "watched" and a list of movies as a value. 
    Output: Returns a list of movies that the user has watched but 
    none of their friends have watched.
    '''
    friends_movies = []
    for friend_movie_dict_index in range(len(user_data["friends"])):
        friends_movies += user_data["friends"][friend_movie_dict_index]["watched"]

    users_unique_movies = []
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            users_unique_movies.append(movie)

    return users_unique_movies

def get_friends_unique_watched(user_data):
    '''
    Input: user_data (a dictionary with keys "watched" and "friends",
    with lists as their values). Elements of "watched" list are dictionaries
    of movies. Each element of "friends" list is a dictionary with key
    "watched" and a list of movies as a value. 
    Output: Returns a list of unique movies that the user's friends have watched
    but the user has not.
    '''
    friends_movies = []
    for friend_movie_dict_index in range(len(user_data["friends"])):
        friends_movies += user_data["friends"][friend_movie_dict_index]["watched"]

    friends_unique_watched = []
    for movie in friends_movies:
        if movie not in user_data["watched"] and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
        return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------