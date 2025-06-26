from downloaders.instagram import download_instagram
from downloaders.youtube import download_youtube
from downloaders.tiktok import download_tiktok
from downloaders.facebook import download_facebook

def batch_download(urls, download_path):
    results = []
    for url in urls:
        if "instagram.com" in url:
            results.append(download_instagram(url, download_path))
        elif "youtube.com" in url or "youtu.be" in url:
            results.append(download_youtube(url, download_path))
        elif "tiktok.com" in url:
            results.append(download_tiktok(url, download_path))
        elif "facebook.com" in url:
            results.append(download_facebook(url, download_path))
        else:
            results.append(f"Unsupported URL: {url}")
    return results
