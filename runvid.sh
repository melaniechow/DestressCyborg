#!/bin/bash -       
#title           :runvideo.sh
#description     :This script detects objects in a video sand saves the labels.
#author		 :Royce Yang
#date            :20190131
#version         :0.1
#usage		 :sbatch runvideo.sh video_file.mp4 [-s]
#notes           :Use the -s opt to save visual output;Output folder is called video_file_processed_DATE
#==============================================================================

#SBATCH --account=pi-cjbryan
#SBATCH --job-name=vision     # name of job
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=47:00:00

# load desired python version (check availability with 'module avail')
module load python/booth/3.6/3.6.3

#ffmpeg -i vid5_cut.mp4 -qscale:v 2 vid5/%06d.jpg
#ffmpeg -i vid5/%06d_blur.png -pix_fmt yuv420p -qscale:v 2 vid5_blurred.mp4
python3 blur_section.py
