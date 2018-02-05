import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for albums_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(albums_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]): # we want the path, not hte name of the album
            yield song


def filename(start):
    for path, directories, files in os.walk(start):
        if "emp3" in files:
            yield os.path.join(files, path)


def find_music(start, extenstion):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, "*.{}".format(extenstion)):
            yield os.path.join(path, file)

album_list = find_albums("music", "black*")
song_list = find_songs(album_list)
# filenames = filename("music")

# for s in song_list:
#     print(s)

# for file in filenames:
#     print(file)

for f in find_music("music", "emp3"):
    print(f)