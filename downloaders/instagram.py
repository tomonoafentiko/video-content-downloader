import instaloader
import os

def download_instagram(url, download_path):
    loader = instaloader.Instaloader(dirname_pattern=os.path.join(download_path, 'instagram_downloads'))
    try:
        if "/reel/" in url:
            shortcode = url.split("/reel/")[1].split("/")[0]
        elif "/p/" in url:
            shortcode = url.split("/p/")[1].split("/")[0]
        else:
            return "Invalid Instagram URL."

        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=f"instagram_{shortcode}")
        return f"Downloaded Instagram content: {shortcode}"
    except Exception as e:
        return f"Error downloading Instagram content: {e}"
