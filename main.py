import srt, re
filepath='test/srt/test.nl.srt'
subtitle_generator = srt.parse(open(filepath))
subtitles= list(subtitle_generator)
urlregex='https?://\S+|WWW\.\S+'
counter=0
for sub in subtitles:
    if re.search(urlregex, sub.content):
        counter+=1
        print("FOUND ILLEGAL STRING: " + sub.content + " INDEX: " + str(sub.index))
        subtitles.pop(sub.index-counter)

print(srt.compose(subtitles))
finalfile = open("{}.forced.srt".format(filepath.split(".srt")[0]), "w")
finalfile.write(srt.compose(subtitles))
