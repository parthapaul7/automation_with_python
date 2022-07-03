import os

os.chdir("../../../Downloads")
file = os.listdir()

dirs = ["apps", "docs", "videos", "images", "music","zip"]
# time = datetime.fromtimestamp(file)
for elem in dirs:
    if elem not in file:
        os.mkdir(elem)
for elem in file:
    if (".svg") in elem or (".png") in elem or (".jpg") in elem:
        print(elem, "\n")
        os.rename(elem, "images/"+elem)
    if (".mp4") in elem or (".avi") in elem or (".mkv") in elem:
        print(elem, "\n")
        os.rename(elem, "videos/"+elem)
    if (".mp3") in elem or (".wav") in elem or (".flac") in elem:
        print(elem, "\n")
        os.rename(elem, "music/"+elem)
    if (".pdf") in elem or (".doc") in elem or (".docx") in elem:
        print(elem, "\n")
        os.rename(elem, "docs/"+elem)
    if (".exe")  in elem:
        print(elem, "\n")
        os.rename(elem, "apps/"+elem)
    if(".zip") in elem or (".rar") in elem:
        print(elem, "\n")
        os.rename(elem, "zip/"+elem)