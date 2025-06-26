import yt_dlp
import os

def download_youtube(url, download_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, 'youtube_downloads', '%(title)s.%(ext)s'),
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"Downloaded YouTube video: {info['title']}"
    except Exception as e:
        return f"Error downloading YouTube content: {e}"
