import argparse
from PIL import Image
import os
import json

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

    # Create JSON file
    sprite_filename = os.path.basename(output_path)
    json_data = {
        "sprite_sheet": output_path,
        "x": 0,
        "y": 0,
        "visible": False,
        "can_move": False,
        "frames": len(frames)
    }
    json_output_path = os.path.join("./ducks", f"{os.path.splitext(sprite_filename)[0]}.json")
    with open(json_output_path, 'w') as json_file:
        json.dump(json_data, json_file)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract frames from a GIF and save them into a big image.')
    parser.add_argument('-i', '--input', required=True, help='Input GIF file')
    parser.add_argument('-o', '--output', required=False, help='Output image file')

    args = parser.parse_args()
    base_name = os.path.splitext(args.input)[0]
    
    if args.output is None:
        args.output = f"./assets/sprites/{base_name}-frames.png"
    else:
        args.output = f"./assets/sprites/{args.output}.png"
    
    extract_frames(args.input, args.output)