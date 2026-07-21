# MLMediaCompressor

Image/Video compression using **KMeans clustering**.  
This library reduces the color complexity of images by clustering pixel values into a limited palette, producing visually compressed images with fewer colors.

---

## 🚀 Installation

You can install directly from GitHub:

```bash
pip install git+https://github.com/1Nitin1/MLMediaCompressor.git

```
# Usage
```python
from MLMediaCompressor import compress_image, compress_video

# Compress image
compress_image("input.png", n_colors=12, saveas="output")

# Compress video
compress_video("input.mov", n_colors=16, saveas="output_video")

```
## 🖥️ Command-Line Usage

After installing, you can run the compressor directly from the terminal:

```bash
# Image compression
mlcompress image input.png --n_colors 12 --quality 80 --saveas out

# Video compression (MOV auto-converts to MP4)
mlcompress video input.mov --n_colors 16 --saveas out


```
## Parameters
- url (str): Path to the input image file.

- n_colors (int): Number of colors (clusters) to reduce to. Default = 50.

- **Only for image** quality (int): JPEG quality (1–95). Default = 50.

- saveas (str): Output filename (without extension). Default = "compressed_image".

## Returns:

- A PIL.Image.Image object representing the compressed image.
- A mp4 file representing the compressed video.

# Features
- Image compression using KMeans color quantization

- Video compression (frame‑wise KMeans)

- Automatic .mov → .mp4 conversion for compatibility

- CLI support for quick usage from terminal

# Development
Clone the repo and install dependencies:
```bash
git clone https://github.com/yourusername/MLMediaCompressor.git
cd MLMediaCompressor
pip install -r requirements.txt
```
# Contributing
- Pull requests are welcome!
- For major changes, please open an issue first to discuss what you’d like to change.

# License
This project is licensed under the MIT License — see the LICENSE file for details.