import json
import unittest
from music import Music
import requests


class TestMusicMethods(unittest.TestCase):
    def test_get_any_data(self):
        key = "bb0ae5a7f6c3c3a2a1c90e24035e59c3"

        url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get"
        params = {
            "apikey": key,
            "page": 1,
            "page_size": 5,
            "country": "us",
            "f_has_lyrics": 1
        }
        response = requests.get(url, params=params)
        data1 = response.json()

        url2 = "https://api.musixmatch.com/ws/1.1/artist.get"
        params2 = {
            "apikey": key,
            "artist_mbid": "de0748c9-ed32-4a7c-aaaa-cfac23ec5299",
            "page": 1,
        }
        response = requests.get(url2, params=params2)
        data2 = response.json()

        url3 = "https://api.musixmatch.com/ws/1.1/artist.get"
        params3 = {
            "apikey": key,
            "artist_mbid": "7e5a2a59-6d9f-4a17-b7c2-e1eedb7bd222",
            "page": 1,
        }
        response = requests.get(url3, params=params3)
        data3 = response.json()

        params4 = {
            "apikey": key,
            "artist_mbid": "4be3b2fa-0b31-445c-babf-475944be8971",
            "page": 1,
        }
        response = requests.get(url3, params=params4)
        data4 = response.json()

        url4 = "https://api.musixmatch.com/ws/1.1/track.get"
        params4 = {
            "apikey": key,
            "track_isrc": "USY251943264",
            "page": 1,
        }
        response = requests.get(url4, params=params4)
        data5 = response.json()

        params5 = {
            "apikey": key,
            "track_isrc": "USY251943249",
            "page": 1,
        }
        response = requests.get(url4, params=params5)
        data6 = response.json()

        params6 = {
            "apikey": key,
            "track_isrc": "USY251660155",
            "page": 1,
        }

        response = requests.get(url4, params=params6)
        data7 = response.json()

        params7 = {
            "apikey": key,
            "track_isrc": "USSM12305004",
            "page": 1,
        }

        response = requests.get(url4, params=params7)
        data8 = response.json()

        apis = [data1, data2, data3, data4, data5, data6, data7, data8]

        with open("test_music.json", 'w') as test_file:
            json_string = json.dumps(apis, indent=4)
            test_file.write(json_string)

    def test_get_artists_by_song(self):
        with open("test_music.json",
                  'r') as file:
            test1 = json.load(file)
        obj1 = Music(test1)
        self.assertEqual(obj1.get_artists_by_song("Lose Control"), "Teddy Swims")
        with self.assertRaises(ValueError):
            obj1.get_artists_by_song("1234")

    def test_see_rating(self):
        with open("test_music.json",
                  'r') as file:
            test2 = json.load(file)
        obj2 = Music(test2)
        self.assertEqual(obj2.see_rating("Mr.Kitty"), "Mr.Kitty is ranked 34 on Musixmatch!")
        with self.assertRaises(ValueError):
            obj2.see_rating("Travis  Scott")

    def test_favorites(self):
        with open("test_music.json",
                  'r') as file:
            test3 = json.load(file)
        obj3 = Music(test3)
        obj3.favorites("Mr.Kitty")
        self.assertEqual(obj3.my_music, ["Mr.Kitty"])

    if __name__ == '__main__':
        unittest.main()
