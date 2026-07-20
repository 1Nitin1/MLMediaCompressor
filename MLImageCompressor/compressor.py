import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def compress_image(url,n_colors=50,quality=50,saveas='compressed_image')->Image.Image:
    """
    Compress an image by reducing its color palette using KMeans clustering.

    Parameters:
        url (str): Path to the input image file.
        n_colors (int): Number of colors (clusters) to reduce to.
        quality (int): JPEG quality (1–95).
        saveas (str): Output filename (without extension).

    Returns:
        Image.Image: The compressed PIL image object.
    """
    try:
        img = Image.open(url).convert("RGB")
    except Exception as e:
        raise ValueError(f"Could not open image {url}: {e}")

    arr=np.array(img)
    r,c,_=arr.shape
    pixels=arr.reshape(r*c,3)
    
    km = KMeans(n_clusters=n_colors,random_state=42)
    km.fit(pixels)

    labels = km.predict(pixels)

    compressed_pixels=km.cluster_centers_[labels]

    compressed_array=compressed_pixels.reshape(r,c,3)

    final_array = np.clip(compressed_array,0,255).astype(np.uint8)
    img_file=Image.fromarray(final_array)

    img_file.save(f'{saveas}.jpeg',quality=quality)
    return img_file