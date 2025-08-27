class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def __repr__(self):
        return f"<Song: {self.name} by {self.artist} ({self.genre})>"
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genres is None:
            cls.genres = []
        if cls.genre not in cls.genres:
            cls.genres.append(cls.genre 



