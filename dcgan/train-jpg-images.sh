#!/bin/bash
python main.py \
 --dataset folder \
 --dataroot ~/apps/matchbox-twelvy/jpg-images/ \
 --imageSize 128 \
 --batchSize 16 \
 --cuda \
 --niter 8000 \
 --ngf 128 \
 --ndf 32 \
 --outf ~/apps/matchbox-twelvy/output/ \
 --checkFreq 25 \
 --manualSeed 505 \
 >> ~/apps/matchbox-twelvy/output/training-log.txt

# --netG /media/max/9045a012-fc84-441c-b847-3f9461cfd86c/roco6x6/output_128_100/netG_epoch_99.pth \
# --netD /media/max/9045a012-fc84-441c-b847-3f9461cfd86c/roco6x6/output_128_100/netD_epoch_99.pth \
