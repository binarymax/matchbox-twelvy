#!/bin/bash
python main.py \
 --cuda \
 --ngf 128 \
 --ndf 32 \
 --outf ~/apps/matchbox-twelvy/twelvys/ \
 --netG ~/apps/matchbox-twelvy/dcgan/models/netG_epoch_45.pth