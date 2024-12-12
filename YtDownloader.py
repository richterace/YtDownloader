import yt_dlp

# input the yt lnk
link = input("Input the YouTube link: ")

while link != 'N':
    # Define options of downloads
    options = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video + audio quality
        'outtmpl': '%(title)s_%(id)s.%(ext)s',  # Save file as '<videotitle>.<extension>'
        'merge_output_format': 'mp4',          # Merge video and audio into MP4
    }

    try:
        print("Downloading...")
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([link])
        print("Download complete!")
        link = input("Input the YouTube link (type 'N' if you want to stop):")
    except Exception as e:
        print(f"An error occurred: {e}")
        link = input("Input the YouTube link (type 'N' if you want to stop):")
