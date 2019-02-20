from youtube_dl import YoutubeDL

#sample 1
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=l2GS39yALxc"])

#sample 2
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=EdLRyVkI6KE", "https://www.youtube.com/watch?v=XSDb4xJPnHE"])

#sample 3
options = {
    "format" : "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=L0NZW6pgSLc"])

#sample 4
options = {
    "default_search" : "ytsearch",
    "max_downloads": 1
}
dl = YoutubeDL(options)
dl.download(["con điên TAMKA PKL"])

#sample 5
options = {
    "default_search" : "ytsearch",
    "max_downloads": 1,
    "format" : "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download = (["nhớ mưa sài gòn lam trường"])