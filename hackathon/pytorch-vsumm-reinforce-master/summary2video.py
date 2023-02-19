import h5py
import cv2
import os
import os.path as osp
import numpy as np
import argparse
import shutil
import moviepy.editor
import glob
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, required=True, help="path to h5 result file")
parser.add_argument('-d', '--frm-dir', type=str, required=True, help="path to frame directory")
parser.add_argument('-i', '--idx', type=int, default=0, help="which key to choose")
parser.add_argument('--fps', type=int, default=30, help="frames per second")
parser.add_argument('--width', type=int, default=640, help="frame width")
parser.add_argument('--height', type=int, default=480, help="frame height")
parser.add_argument('--save-dir', type=str, default='log', help="directory to save")
parser.add_argument('--save-name', type=str, default='summary.mp4', help="video name to save (ends with .mp4)")
args = parser.parse_args()

def video2frm(path):
  
    # Path to video file
    vidObj = cv2.VideoCapture(path)
  
    # Used as counter variable
    count = 0
  
    # checks whether frames were extracted
    success = 1

    os_current_path = os.path

    if os.path.exists("frames"):
        shutil.rmtree("frames")
    os.mkdir("frames")
    os.chdir("frames")
  
    while success:
  
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
  
        # Saves the frames with frame-count
        if success:
            count += 1
            cv2.imwrite("%.6d.jpg" % count, image)

    os.chdir('..')    
  

def frm2video(frm_dir, summary, vid_writer):
    img_array = []
    for idx, val in enumerate(summary):
        if val == 1:
            # here frame name starts with '000001.jpg'
             # change according to your need
                frm_name = str(idx+1).zfill(6) + '.jpg'
                frm_path = osp.join(frm_dir, frm_name)
                for filename in glob.glob(frm_path):
                    img = cv2.imread(filename)
                
                height, width, layers = img.shape
                size = (width,height)
                img_array.append(img)
    #             frm = cv2.imread(frm_path)
    #             frm = cv2.resize(frm, (args.width, args.height))
    #             vid_writer.write(frm)
    #         except Exception as e:
    #             print(str(e))
    out = cv2.VideoWriter('my_pngs.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()   


    
if __name__ == '__main__':
    
    video2frm(args.frm_dir)
    if not osp.exists(args.save_dir):
        os.mkdir(args.save_dir)
    vid_writer = cv2.VideoWriter(
        osp.join(args.save_dir, args.save_name),
        cv2.VideoWriter_fourcc(*'MP4V'),
        args.fps,
        (args.width, args.height),
    )
    h5_res = h5py.File(args.path, 'r')
    key = list(h5_res.keys())[args.idx]
    summary = h5_res[key]['machine_summary'][...]
    h5_res.close()
    frm2video("frames", summary, vid_writer)
    video = moviepy.editor.VideoFileClip(args.frm_dir)
    video_duration = int(video.duration)
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
    ffmpeg_extract_subclip("my_pngs.avi", 0,(video_duration/3)+10, targetname="temp.avi")

    # vid_writer.release()
    cv2.destroyAllWindows()
    
    

# Converts into more readable format
