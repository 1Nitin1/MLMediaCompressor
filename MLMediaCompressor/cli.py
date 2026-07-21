import argparse
from .image_compressor import compress_image
from .video_compressor import compress_video   

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="MLMediaCompressor: Compress images and videos using KMeans clustering"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Image CLI
    img_parser = subparsers.add_parser("image", help="Compress an image")
    img_parser.add_argument("input_file", help="Path to the input image file")
    img_parser.add_argument("--n_colors", type=int, default=50, help="Number of colors to use (default: 50)")
    img_parser.add_argument("--quality", type=int, default=50, help="JPEG quality from 1 to 95 (default: 50)")
    img_parser.add_argument("--saveas", default="compressed_image", help="Output filename without extension (default: compressed_image)")

    # Video CLI
    vid_parser = subparsers.add_parser("video", help="Compress a video")
    vid_parser.add_argument("input_file", help="Path to the input video file (.mp4 or .mov)")
    vid_parser.add_argument("--n_colors", type=int, default=20, help="Number of colors to use (default: 20)")
    vid_parser.add_argument("--saveas", default="compressed_video", help="Output filename without extension (default: compressed_video)")

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "image":
        compress_image(args.input_file, n_colors=args.n_colors, quality=args.quality, saveas=args.saveas)
        print(f"Compressed image saved as {args.saveas}.jpeg")

    elif args.command == "video":
        compress_video(args.input_file, n_colors=args.n_colors, saveas=args.saveas)
        print(f"Compressed video saved as {args.saveas}.mp4")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
