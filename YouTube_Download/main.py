import yt_dlp

url = input("Enter video url: ")
print(url)

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    res = ydl.extract_info(url)
    print(res)

print("successfully!")