import yt_dlp
import tkinter

# Initialize the tkinter and some of its options
window = tkinter.Tk()
window.title("Yt Downloader")
window.geometry("360x150")
window.configure(bg='#333333')

# Center the window on the screen
def center_window():
    window.update_idletasks()  
    window_width = 360
    window_height = 150

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position for centering
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the geometry with the calculated position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def toDownload():
    # Get the text from the Entry widget
    link = input.get()  # Retrieve the input value
    
    # Define options for downloads
    options = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video + audio quality
        'outtmpl': '%(title)s_%(id)s.%(ext)s',  # Save file as '<videotitle>.<extension>'
        'merge_output_format': 'mp4',          # Merge video and audio into MP4
    }

    try:
        print("Downloading...")
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([link])  # Pass the link to the download method
        print("Download complete!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to center the window
center_window()

# Add widgets to the window
label = tkinter.Label(window, text="Enter the link to download", bg='#333333', fg='#FFFFFF')
label.pack(pady=10)

input = tkinter.Entry(window, width=40)  # Entry widget to take input
input.pack(pady=10)

click = tkinter.Button(window, text="Download", command=toDownload)  # Pass function reference
click.pack(pady=10)

window.mainloop()
