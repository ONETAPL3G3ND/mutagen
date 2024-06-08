import mutagen

mfile = mutagen.File("example.mp3")
print(mfile.info.pprint())
