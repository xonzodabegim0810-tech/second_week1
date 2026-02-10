class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def display_info(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} min")
    def get_duration_seconds(self):
        seconds = self.duration * 60
        return seconds
song1 = Song("Yesterday", "The Beatles", 2.5)
song1.display_info()
print(song1.get_duration_seconds())

song2 = Song("Bohemian Rhapsody", "Queen", 6.0)
song2.display_info()
print(int(song2.get_duration_seconds()))

