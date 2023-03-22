from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()

artist_repository.delete_all()

artist1 = Artist("Wu-Tang Clan")
artist_repository.save(artist1)

album1 = Album("36 Chambers", "Rap", artist1)
album_repository.save(album1)

result = album_repository.select_all()

for album in result:
    print(f"{album.title}")