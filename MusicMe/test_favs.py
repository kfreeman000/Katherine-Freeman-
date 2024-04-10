import unittest
import json
from music import Music


class TestAllMusic(unittest.TestCase):
    def test_object(self):        # simultaneously testing favorites method in Music as well as add_to_file in AllMusic
        with open("test_music.json",
                  'r') as file:
            ob = json.load(file)
        some_music = Music(ob)

        print(some_music.tracks)
        test = some_music.favorites("Mr.Kitty")
        self.assertEqual(test, {'Songs': [], 'Artists': ["Mr.Kitty"]})

        test_two = some_music.favorites("Grimes")
        self.assertEqual(test_two, {'Songs': [], 'Artists': ["Mr.Kitty", "Grimes"]})

        test_one_song_and_two_artists = some_music.favorites("After Dark")
        self.assertEqual(test_one_song_and_two_artists, {'Songs': ["After Dark"], 'Artists': ["Mr.Kitty", "Grimes"]})

    def test_playlist(self):
        with open("test_music.json",
                  'r') as file:
            ob = json.load(file)
        music = Music(ob)
        some_more_music = music.all_music  # have to create Music object before testing AllMusic methods
        some_more_music.playlist("[Whip, Lose Control]", 'short playlist')
        self.assertEqual(some_more_music.my_playlists, "[{'short playlist': '[Whip, Lose Control]'}]")



