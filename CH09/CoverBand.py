from Band import Band

class CoverBand(Band):

    def __init__ (self, band_name, music_genre, covered_bands_and_performers):
        super().__init__(band_name, music_genre)
        self.covered_bands_and_performers = covered_bands_and_performers

    
    def get_covered_bands(self):
        covered_bands = []
        for band in self.covered_bands_and_performers:
            covered_bands.append(band.band_name)
        
        return covered_bands

band1 = Band('Metallica', 'Heavy Metal')
band2 = Band('Rammstein', 'Industrial Metal')

cover_band = CoverBand('We Do Covers', 'Varied', [band1, band2])
print(cover_band)
print(f'Covered bands: {cover_band.get_covered_bands()}')  