import srt, re
filepath='test.srt'
subtitle_generator = srt.parse(open(filepath))
subtitles= list(subtitle_generator)
urlregex='https?://\S+|WWW\.\S+'
for sub in subtitles:
    if re.search(urlregex, sub.content):
        print("FOUND ILLEGAL STRING: " + sub.content + " INDEX: " + str(sub.index))
        subtitles.pop(sub.index-1)
        print(srt.compose(subtitles))