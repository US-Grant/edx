def song_playlist(songs, max_size):
    playlist = []
    size = 0
    if songs[0][2] > max_size:
        return playlist
    playlist.append(songs[0][0])
    size += songs[0][2]
    if len(songs[1:]) > 0:
        while True:
            choosen_song = None
            for song in songs[1:]:
                if song[0] in playlist:
                    continue
                if choosen_song is None:
                    choosen_song = song
                elif song[2] < choosen_song[2]:
                    choosen_song = song
            if (size + choosen_song[2]) <= max_size:
                playlist.append(choosen_song[0])
                size += choosen_song[2]
            else:
                break
            if len(playlist) == len(songs):
                break
    return playlist


songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 12.2
print(song_playlist(songs, max_size))
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 11
print(song_playlist(songs, max_size))