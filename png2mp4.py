import glob
from natsort import natsorted
from moviepy.editor import *
from os import listdir
from os.path import isfile,join
import os

rootdir="/home/coder/workspace/iLIDS-VID/i-LIDS-VID/sequences"
cam_list = os.listdir(rootdir)
#print(cam_list)
for cam_id in cam_list:
    if os.path.isdir(cam_id):
        person_list = os.listdir(cam_id)
        person_list = sorted(person_list)
        print ("person_list:",person_list) 
        for person_id in person_list:
            base_dir = os.path.join(rootdir,cam_id)
            base_dir = os.path.join(base_dir,person_id)

            print ("base_dir",base_dir)
            gif_name='pic'
            fps=25
            final_path = base_dir+'/*.png'
            #print ("final_path:",final_path)
            file_list = glob.glob(final_path)  # Get all the pngs in the current directory
            #print ("file_list:",file_list)
            file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images
            clips = [ImageClip(m).set_duration(0.04)
                    for m in file_list_sorted]

            concat_clip = concatenate_videoclips(clips, method="compose")
            concat_clip.write_videofile(base_dir+"/"+person_id+".mp4", fps=fps)
