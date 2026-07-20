# myimagecompressor

Image compression using **KMeans clustering**.  
This library reduces the color complexity of images by clustering pixel values into a limited palette, producing visually compressed images with fewer colors.

---

## 🚀 Installation

You can install directly from GitHub:

```bash
pip install git+https://github.com/1Nitin1/MLImageCompressor.git

```
# Usage
```python
from MLImageCompressor import compress_image

# Compress an image to 16 colors and save as "compressed.jpeg"
compress_image("butterfly.jpg", n_colors=16, saveas="compressed")
```
## Parameters
- url (str): Path to the input image file.

- n_colors (int): Number of colors (clusters) to reduce to. Default = 50.

- quality (int): JPEG quality (1–95). Default = 50.

- saveas (str): Output filename (without extension). Default = "compressed_image".

## Returns:

- A PIL.Image.Image object representing the compressed image

# Features
- Reduce image color palette using KMeans clustering.

- Adjustable number of colors and JPEG quality.

- Save compressed images easily with a single function call.

- Returns a PIL image object for further processing.

# Development
Clone the repo and install dependencies:
```bash
git clone https://github.com/yourusername/myimagecompressor.git
cd myimagecompressor
pip install -r requirements.txt
```
# Contributing
- Pull requests are welcome!
- For major changes, please open an issue first to discuss what you’d like to change.

# License
This project is licensed under the MIT License — see the LICENSE file for details.