class Song:
    song_count = 0
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.song_count += 1

        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        Song.artists_count[artist] = Song.artists_count.get(artist, 0) + 1

    @classmethod
    def count(cls):
        return cls.song_count

    @classmethod
    def genres(cls):
        return list(cls.genre_count.keys())

    @classmethod
    def artists(cls):
        return list(cls.artists_count.keys())


s1 = Song("Halo", "Beyonce", "Pop")
s2 = Song("Crazy in Love", "Beyonce", "R&B")

print(Song.count())  # Output: 2
print(Song.genres())  # Output: ['Pop', 'R&B']
print(Song.artists())  # Output: ['Beyonce']
print(Song.genre_count)  # Output: {'Pop': 1, 'R&B': 1}
