import json


class AllMusic:

    def __init__(self):
        self.favorites = {'Songs': [], 'Artists': []}
        self.my_playlists = []
        self.all_music_dict = {'Songs': [], 'Artists': []}

    def __str__(self):
        print("saved playlists:" + str(self.my_playlists))

    def playlist(self, song_list, playlist_name):  # idk if i'll just print object instead of writing to a file yet
        """
        creates new "playlist" from instance of Music object
        param includes name of playlist that user chooses
        :return: string saying what the vibe of your playlist is and string of Music object
        """
        if playlist_name in self.my_playlists:
            self.my_playlists[playlist_name].extend(song_list)
        else:
            new_playlist = {playlist_name: song_list}
            self.my_playlists.append(new_playlist)

    def add_to_file(self, song=None, artist=None):
        """
        adds to file 'favs_history.py' with updated favorite songs and artists
        :return: returns updated dict that is getting written to file in real time
        """
        if song is not None:
            self.favorites["Songs"].append(song)
        if artist is not None:
            self.favorites["Artists"].append(artist)
        return self.favorites

    def all_music(self, tracks, artists):
        """
        simply organizes all the music from Music
        :param tracks: track list from Music class
        :param artists: artist list from Music class
        :return: self.all_music dict
        """
        self.all_music_dict['Songs'] = tracks
        self.all_music_dict['Artists'] = artists
        return self.all_music_dict
