class Band:

    def __init__(self, band_name, music_genre):
        self.band_name = band_name
        self.music_genre = music_genre
        self.number_of_gold_records = 0
        self.number_of_platinum_records = 0

    #def describe_band(self, band_name, music_genre):
    #    print(f'Name: {self.band_name}, Genre: {self.music_genre}')

    def is_active(self):
        print(f'{self.band_name} is active.')

    # This method returns the object instance in string format
    def __str__(self):
        return f'Name: {self.band_name}, Genre: {self.music_genre}'
    
    def set_number_of_gold_records(self, number_of_gold_records):
        self.number_of_gold_records = number_of_gold_records
    
    def set_number_of_platinum_records(self, number_of_platinum_records):
        self.number_of_platinum_records = number_of_platinum_records
    


band = Band('System of a Down', 'Progressive Metal')

band.set_number_of_gold_records(5)
print(f'Gold records: {band.number_of_gold_records}')

band.set_number_of_platinum_records(5)
print(f'Platinum records: {band.number_of_platinum_records}')

