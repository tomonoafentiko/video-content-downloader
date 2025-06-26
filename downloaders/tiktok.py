import yt_dlp
import os

def download_tiktok(url, download_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, 'tiktok_downloads', '%(title)s.%(ext)s'),
            'format': 'best',
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"Downloaded TikTok video: {info.get('title', 'Untitled')}"
    except Exception as e:
        return f"Error downloading TikTok content: {e}"
