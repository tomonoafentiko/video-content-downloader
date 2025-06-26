import yt_dlp
import os

def download_facebook(url, download_path):
    try:
        if "web.facebook.com" in url:
            url = url.replace("web.facebook.com", "www.facebook.com")

        ydl_opts = {
            'outtmpl': os.path.join(download_path, 'facebook_downloads', '%(title)s.%(ext)s'),
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"Downloaded Facebook video: {info['title']}"
    except Exception as e:
        return f"Error downloading Facebook content: {e}"
