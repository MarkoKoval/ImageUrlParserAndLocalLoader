import random
import urllib.request

def save_images_by_url_locally(image_urls ,  local_pc_path_to_save):
    for url in image_urls:
        name = url.split("/")[-1]
        urllib.request.urlretrieve(url,local_pc_path_to_save+name)
