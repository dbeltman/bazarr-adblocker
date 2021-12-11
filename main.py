import srt
import re
import argparse

# Main Args
parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=str, metavar='filepath', help="Path of subtitle file")
#filepath='test/srt/test.nl.srt'dd

args= parser.parse_args()

subtitle_generator = srt.parse(open(args.filepath))
subtitles= list(subtitle_generator)
urlregex='https?://\S+|WWW\.\S+|\.nl\S+'
counter=0
for sub in subtitles:
    if re.search(urlregex, sub.content):
        counter+=1
        print("FOUND ILLEGAL STRING: " + sub.content + " INDEX: " + str(sub.index))
        subtitles.pop(sub.index-counter)

print(srt.compose(subtitles))
finalfile = open("{}.forced.srt".format(args.filepath.split(".srt")[0]), "w")
finalfile.write(srt.compose(subtitles))
