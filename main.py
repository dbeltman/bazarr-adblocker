from distutils.command.clean import clean
import srt
import re
import argparse
from wordfilter import Wordfilter
import os    
from chardet import detect
# Main Args
parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=str, metavar='filepath', help="Path of subtitle file")
parser.add_argument("-rw", "--writemode", action='store_true', help="Write mode, `true` or `false`")
parser.add_argument("-v", "--verbose", action='store_true', help="Verbose mode, prints the SRT to console")
parser.add_argument("-vv", "--superverbose", action='store_true', help="SuperVerbose mode, prints all handled strings to conolse")

#filepath='test/srt/test.nl.srt'dd

args= parser.parse_args()

naughtywordlist=["https",
    "www.",
    ".nl",
    ".com",
    "facebook",
    "twitter",
    "youtube",
    "8k",
    "kodi"]
wordfilter = Wordfilter()
wordfilter.clearList()
wordfilter.addWords(naughtywordlist)
# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

from_codec = get_encoding_type(args.filepath)
print("CODEC: " + str(from_codec))
# add try: except block for reliability
try: 
    with open(args.filepath, 'r', encoding=from_codec) as f, open(args.filepath + ".utf8", 'w', encoding='utf-8') as e:
        text = f.read() # for small files, for big use chunks
        e.write(text)

    #os.rename(trgfile, srcfile) # rename new encoding
except UnicodeDecodeError:
    print('Decode Error')
except UnicodeEncodeError:
    print('Encode Error')
#exit (1)
subtitle_generator = srt.parse(open(args.filepath + ".utf8"))
dirtysubs = list(subtitle_generator)


# counter=0
cleansubs=dirtysubs.copy()

for sub in dirtysubs:
    if args.verbose:    
        print("\n##########   HANDLING SUBTITLE ID " + str(sub.index))
    if wordfilter.blacklisted(sub.content.lower()):
        # counter+=1
        print("String \n\n'" + sub.content + "'\n\nwas declared ILLEGAL!\n########## \n")
        # print("\nFOUND ILLEGAL STRING: \n`" + sub.content + "`\nINDEX: " + str(sub.index))
        cleansubs.remove(sub)
    else:
        if args.superverbose:
            print("String \n\n'" + sub.content + "'\n\nwas declared OKAY!\n########## \n")
            # print("String \n'" + sub.content + "'\n##########   was declared OKAY!\n")

if args.verbose:
    print("### COMPOSED SRT ###")
    print(srt.compose(cleansubs))

if args.writemode:
    print("Writing file")
    finalfile = open("{}.forced.srt".format(args.filepath.split(".srt")[0]), "w")
    finalfile.write(srt.compose(dirtysubs))
    os.remove(args.filepath) # remove old encoding file
    finalfile = open(args.filepath, "w")
    finalfile.write(srt.compose(cleansubs))
    os.remove(args.filepath + ".utf8") # remove old encoding file
else:
    print("\nWrite mode not set, NOT writing to file.")
