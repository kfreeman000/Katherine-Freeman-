import requests
from favs import AllMusic


class Music:

    def __init__(self, file):
        self.tracks = []
        self.artists = []
        self.artists_and_their_rating = {}
        for item in file:
            if "track_list" in item["message"]["body"]:  # consider making first dict path a variable
                for song in item["message"]["body"]["track_list"]:
                    self.artists.append(song["track"]["artist_name"])
                    self.tracks.append(song["track"]["track_name"])
            elif "track" in item["message"]["body"]:
                self.tracks.append(item["message"]["body"]["track"]["track_name"])
            elif "artist" in item["message"]["body"]:
                artist_in_json = item["message"]["body"]["artist"]["artist_name"]
                artist_rank = item["message"]["body"]["artist"]["artist_rating"]
                self.artists.append(artist_in_json)
                self.artists_and_their_rating[artist_in_json] = artist_rank
        self.my_music = []
        self.my_artists = []
        self.all_music = AllMusic()

    def __str__(self):
        return str("My favorites - ") + str(self.my_music)

    def get_artists_by_song(self, song):
        """
        Gets the artist for song name
        :param song:
        :return: artist who has a song with that title
        raise error if song is not found
        """
        if song not in self.tracks:
            raise ValueError("this song name is not found")
        organized = self.all_music.all_music(self.tracks, self.artists)  # here, self.all_music is an attribute of
        # Music that creates an object in AllMusic. with this AllMusic object, i'm calling an AllMusic method: all_music
        find = organized['Songs'].index(song)
        artist = organized['Artists'][find]
        return artist

    def see_rating(self, artist):
        """
        returns ranking/rating of artist on Musixmatch
        raises error if artist is not found
        """
        if artist not in self.artists_and_their_rating:
            raise ValueError("artist is not found")
        else:
            return artist + " is ranked " + str(self.artists_and_their_rating[artist]) + " on Musixmatch!"

    def favorites(self, fav):
        """
        adds to self.my_music list with new fav
        songs or artists
        also organizes favorite songs and artists in another class: AllMusic
        """
        if fav in self.tracks:
            self.my_music.append(fav)
            self.all_music.favorites["Songs"].append(fav)
        elif fav in self.artists or self.artists_and_their_rating:  # checking artists in two groups: one from songs
            # and one from artist data
            self.my_music.append(fav)
            self.all_music.favorites["Artists"].append(fav)
        else:
            raise ValueError("song or artist not found")
        return self.all_music.favorites

