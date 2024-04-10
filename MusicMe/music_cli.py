from music import Music
import json
import pprint


def what_data():
    """
    asks initial questions about what data to fetch from API
    :return:
    """
    print("---------------------")
    print("1. see currently downloaded data")
    print("2. playlists")
    print("3. favorites")
    print("4. get artist ranking\n")
    first = input("\nenter a number to interact.\nenter 'quit' to stop the interface.\n")
    print('\n')
    return first


def all_data(all_music_class, music_class):
    """
    displays all data fetched from API             # currently just songs and artists
    :param all_music_class: object of AllMusic
    :param music_class: object of Music
    """""
    dump = all_music_class.all_music(music_class.tracks, music_class.artists)
    with open("history.py", 'w') as file:
        file.write(json.dumps(dump))
    pprint.pprint(dump)
    print("---------------------")
    print("---------------------")


def playlists(all_music_class):
    """
    gives option to either view all playlists of this object or create a new playlist
    :param all_music_class: object of AllMusic
    """
    choice1 = input("would you like to -\n1. see all playlists\n2. make a new playlist\n")
    if choice1 == "1":
        print(all_music_class.my_playlists)
        print("\n")
    elif choice1 == "2":
        songs = input("enter a list of songs for your playlist.\nseparate each song with a comma.")
        print("\nsweet!")
        title = input("now, give your playlist a title.")
        print("\ncool!\n")
        print("..........creating playlist...........\n")
        all_music_class.playlist(songs, title)
        print("\nplaylist is now stored successfully!\n")


def favorites(music_class, all_music_class):
    """
    updates favorites list
    :param all_music_class:
    :param music_class: object of Music
    """
    try:
        choice1 = input("would you like to -\n1. see your favorites\n2. update your list\n")
        choices = ["1", "2"]
        if choice1 == "1":
            if all_music_class.favorites == {'Songs': [], 'Artists': []}:
                print("\n")
                print("you have not yet added anything to favorites.")
                print(all_music_class.favorites)
                print("\n")
            else:
                print(all_music_class.favorites)
                print("\n")
        elif choice1 == "2":
            new = input("what would you like to add to your list?")
            music_class.favorites(new)
            print("looks good. here are your favorites:\n")
            print(all_music_class.favorites)
        elif choice1 not in choices:
            raise ValueError
    except ValueError:
        print("invalid input. please only input a number")


def see_ratings(music_class):
    """
    uses Music to get the rating of an artist
    :param music_class:
    :return:
    """
    artist = input("who would you like to see the Musixmatch rating of?")
    the_string = music_class.see_rating(artist)
    print("\n")
    print(the_string)


def main():
    print("\n")
    print("\n")
    print("Welcome to Kat's MusixMatch API.\n")
    with open('test_music.json', 'r') as f:
        data = json.load(f)
    music_class = Music(data)
    all_music_class = music_class.all_music
    answers = ["1", "2", "3", "4", "quit"]
    while True:
        try:
            first = what_data()
            if first == '1':
                all_data(all_music_class, music_class)
            elif first == '2':
                playlists(all_music_class)
            elif first == '3':
                favorites(music_class, all_music_class)
            elif first == '4':
                see_ratings(music_class)
            elif first == 'quit' or first == 'Quit':
                break
            elif first not in answers:
                raise ValueError
        except ValueError:
            print("invalid input. please only input a number, or 'quit' to stop the interface.\n")


if __name__ == "__main__":
    main()
