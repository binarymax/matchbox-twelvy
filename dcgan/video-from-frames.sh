#!/bin/bash
cd /home/max/apps/matchbox-twelvy/frames/
ffmpeg -r 24 \
 -f image2 \
 -s 256x256 \
 -i epoch_%04d.png \
 -vcodec libx264 \
 -crf 25  \
 -pix_fmt yuv420p \
 twelvy_training_128x128x7000_24fps.mp4