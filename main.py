from pytube import YouTube

def main():
    link, path = getLink()
    youtube = connection(link)
    if youtube == None:
        print("Connection Failed")
    else:
        downLoad(youtube, path)


def getLink():
    videoURL = input("Link of the video: ")
    path = input("Create a Folder: ")
    return videoURL, path

# Connection with YouTube
def connection(link):
    try:
        youtube = YouTube(link)
        return youtube
    except:
        return None

def downLoad(youtube, path):
    try:
        youtube.streams.get_highest_resolution().download(path)
        print('Donloaded 😊 👍')
        return True
    except:
        print("Can't download... 😢 ")
        return False


if __name__ == "__main__":
    main()