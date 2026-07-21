# MLMediaCompressor

ML‑based image and video color complexity compression library with CLI support.

---
# Features
- Image compression using KMeans color quantization

- Video compression (frame‑wise KMeans)

- Automatic .mov → .mp4 conversion for compatibility

- CLI support for quick usage from terminal

## 🚀 Installation

You can install directly using pip:

```bash
pip install MLMediaCompressor

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
### Common (Image & Video)
- path (str): Path to the input file.
    - For images: supported formats like .png, .jpeg.
    - For videos: supported formats .mp4 and .mov (MOV is auto‑converted to MP4).

- n_colors (int): Number of color clusters (KMeans) to reduce to. Default = 50 for images, 20 for videos.

- saveas (str): Output filename (without extension)
    - Default = "compressed_image" for images
    - Default = "compressed_video" for videos.

### Image‑specific
- quality (int): JPEG quality (1–95). Default = 50.
    - Only applies when saving compressed images.

## Returns:

- A PIL.Image.Image object representing the compressed image.
- A mp4 file representing the compressed video.

# Contributing
- github: https://github.com/1Nitin1/MLMediaCompressor
- Fork, branch, PR workflow
- For major changes, please open an issue first to discuss what you’d like to change.

# License
This project is licensed under the MIT License — see the LICENSE file for details.