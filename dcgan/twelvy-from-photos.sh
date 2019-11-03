#!/bin/bash
python twelvy.py \
 --dataroot ~/apps/matchbox-twelvy/photos/ \
 --ngf 128 \
 --ndf 32 \
 --outf ~/apps/matchbox-twelvy/twelvys/ \
 --netG ~/apps/matchbox-twelvy/dcgan/models/netG_epoch_50.pth \
 --netD ~/apps/matchbox-twelvy/dcgan/models/netD_epoch_50.pth