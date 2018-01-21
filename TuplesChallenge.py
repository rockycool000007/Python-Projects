imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
track1, track2, track3, track4 = imelda[3]
print(title, artist, year, tracks)
print(track1, track2, track3, track4)

print("The album is {} by {} released in {}.\nTracks include {}, {}, {}, {}".format(title, artist, year, track1[1], track2[1], track3[1], track4[1]))

# Another solution
print(title)
print(artist)
print(tracks)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))


