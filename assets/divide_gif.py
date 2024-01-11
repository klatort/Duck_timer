import argparse
from PIL import Image
import os

def extract_frames(gif_path, output_path):
    im = Image.open(gif_path)
    i = 0
    frames = []
    try:
        while True:
            im.seek(i)
            frames.append(im.copy())
            i += 1
    except EOFError:
        pass

    # Determine the size of the output image
    width, height = frames[0].size
    total_width = width * len(frames)
    total_height = height

    # Create a new image of the correct size
    new_im = Image.new('RGBA', (total_width, total_height))

    print(f"The number of frames in the gif is {len(frames)} frames")
    # Paste each frame into the output image
    for i, frame in enumerate(frames):
        new_im.paste(frame, (i * width, 0))

    # Save the output image
    new_im.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract frames from a GIF and save them into a big image.')
    parser.add_argument('-i', '--input', required=True, help='Input GIF file')
    parser.add_argument('-o', '--output', required=False, help='Output image file')

    args = parser.parse_args()
    base_name = os.path.splitext(args.input)[0]
    
    if args.output is None:
        args.output = f"{base_name}-frames.png"
    else:
        args.output = f"{args.output}/{os.path.basename(base_name)}-frames.png"
    
    extract_frames(args.input, args.output)