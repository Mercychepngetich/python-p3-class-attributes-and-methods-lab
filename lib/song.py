class Song:
     
     count = 0
     genres = []
     artists= []
     genre_count = {}
     artist_count = {}

     def __init__(self, name, artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_genre_count(self)
        self.add_to_artists() 
        self.add_to_artist_count()
          
          
     @classmethod
     def add_song_to_count(cls, song):
          cls.count += 1

     @classmethod
     def add_to_genres(cls, song):
        if song.genre not in cls.genres:
            cls.genres.append(song.genre)
    
     @classmethod
     def add_to_genre_count(cls,song):
          if song.genre in cls.genre_count:
               cls.genre_count[song.genre] +=1
          else:
               cls.genre_count[song.genre] = 1
    
     def add_to_artists(self):
        if self.artist not in self.artists:
            self.artists.append(self.artist)          

 
     def add_to_artist_count(self):  # No need for class method
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

song1 = Song("Happy Soul", "Mercy", "Jazz")
song2 = Song("You are good", "Melon", "Bazz")
song3 = Song("Beautiful World", "Mercy", "Bazz")

print(Song.count)
print(Song.genre_count)
print(Song.artist_count)

               
          

