class Band:

    def __init__(self, band_name, music_genre, status):
        self.band_name = band_name
        self.music_genre = music_genre
        self.status = status

    def describe_band(self, band_name, music_genre):
        print(f'{band_name} is a {music_genre} band.')

    def is_active(self, band_name, status):
        print(f'{band_name} is {status}.')

    # This method returns the object instance in string format
    def __str__(self):
        return self.band_name, self.music_genre


band1 = Band('band1', 'rock', 'active')

print(f'Describe band: {band1.__str__()}')
