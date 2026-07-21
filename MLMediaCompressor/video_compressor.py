import numpy as np
from sklearn.cluster import KMeans
import cv2
import os
import subprocess
def convert_mov_to_mp4(path):
    if path.lower().endswith(".mov"):
        mp4_path = os.path.splitext(path)[0] + ".mp4"
        cmd = ["ffmpeg", "-i", path, "-c:v", "libx264", "-c:a", "aac", mp4_path]
        subprocess.run(cmd, check=True)
        return mp4_path
    return path
    
def compress_frame(frame, k=8):
    # reshape to (num_pixels, 3)
    data = frame.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data)
    new_colors = kmeans.cluster_centers_[kmeans.labels_]
    compressed = new_colors.reshape(frame.shape).astype(np.uint8)
    return compressed
    
def compress_video(path,n_colors=20,saveas='compressed_video'):
    path= convert_mov_to_mp4(path)
    capt = cv2.VideoCapture(path)
    fps=int(capt.get(cv2.CAP_PROP_FPS))
    width=int(capt.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(capt.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(fps,width,height)
    out=cv2.VideoWriter(f'{saveas}.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps,(width,height))
    if not out.isOpened():
        print("Error: VideoWriter not opened")

    i=0
    while True:
        i+=1
        ret, frame = capt.read()
        if i%fps==0:
            print(f'{i//fps} seconds compressed successfully')
        if not ret:
            break
        compressed = compress_frame(frame,n_colors)
        out.write(compressed)

    capt.release()
    out.release()
    print("Video saved as compressed_video.mp4")