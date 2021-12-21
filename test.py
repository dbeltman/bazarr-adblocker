from wordfilter import Wordfilter



naughtywordlist=["https",
    "www.",
    ".nl",
    "kasteel",
    "com",
    "facebook",
    "twitter",
    "youtube",]
wordfilter = Wordfilter()
wordfilter.clearList()
wordfilter.addWords(naughtywordlist)

subtitles=[
    "subcom",
    "facebook",
    "FACEBOOK",
    "faoe",
    "Twitter",
    "doiecom"
]

counter=0
finalsubs=subtitles.copy()
for string in subtitles:
    print("########## HANDLING STRING '" + string.lower() + "'")
    if wordfilter.blacklisted(string):
        # counter+=1
        print("String \n'" + string + "'\nwas declared ILLEGAL!\n##########\n")
        finalsubs.remove(string)
    else:
        print("String \n'" + string + "'\nwas NOT declared illegal\n##########\n")
print(finalsubs)