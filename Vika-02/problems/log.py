t = int(input()) # fjöldi atvika
artists = []
sameLengthSongs = []

for i in range(t):
    songs = [] # nafnið á lögunum
    songsSameLength = []
    n = int(input()) # fjöldi laga per listamann
    artists.insert(i, input()) # setur nafnið á listamanninum í listamannalistann
    for j in range(n):
        songs.insert(j, input()) # inserts songs into list
        if(len(songs[j].replace(" ", "")) == len(artists[i].replace(" ", ""))): # athugar hvort lengd á lagi sé sama og lengd á listamanni
            songsSameLength.insert(j, songs[j])
    sameLengthSongs.insert(i, songsSameLength)
    

for l in range(t):
    print(artists[l] + ":")
    sameLengthSongs[l].sort()
    for m in range(len(sameLengthSongs[l])):
        print(sameLengthSongs[l][m])


