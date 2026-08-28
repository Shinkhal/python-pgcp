def movie_night():
    playlist = ["Inception", "TheMatrix", "Interstellar"]
    movie = input("Enter the movie name you want to add : ")
    
    if movie in playlist :
        print('Already added! ')

    else:
        print(f"Added {movie}")
        playlist.append(movie)
    
    sorted_playlist = sorted(playlist)   
    print(f"Alphabetical Playlist: {sorted_playlist}")


movie_night()