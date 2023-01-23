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
            songsSameLength.insert(j, songs[j]) # setur lög af sömu lengd í annan lisat
    sameLengthSongs.insert(i, songsSameLength) # setur þann lista inní annan lista
    

for l in range(t): # prentar út í lokinn
    print(artists[l] + ":") # prentar út nafn listamanns
    sameLengthSongs[l].sort() # sorterar listann inní listanum 
    for m in range(len(sameLengthSongs[l])): # prentar út lögin inní listanum inní listanum
        print(sameLengthSongs[l][m])


