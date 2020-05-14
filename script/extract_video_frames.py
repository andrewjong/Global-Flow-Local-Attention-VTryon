import cv2
import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--video_path", type=str, help="Folder where videos are")
parser.add_argument("--frame_root", type=str, help="Root folder where to output the frames")
args = parser.parse_args()

frame_root = args.frame_root
videos = sorted(glob.glob(os.path.join(args.video_path, "*.mp4")))
for video in videos:
    print(video)
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    count = 0
    video_path = os.path.basename(video).replace(".mp4", "")
    frame_path = os.path.join(frame_root, video_path)
    os.makedirs(frame_path, exist_ok=True)
    while success:
        name = os.path.join(frame_path, str(count).zfill(5) + ".png")
        print(name)
        image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
        cv2.imwrite(name, image)
        success, image = vidcap.read()
        count += 1
