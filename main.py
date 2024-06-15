#https://github.com/ONETAPL3G3ND
import mutagen

mfile = mutagen.File("example.mp3")
print(mfile.info.pprint())
