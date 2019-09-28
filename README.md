# Matchbox Twelvy

Uses a DCGAN to make fake matchbox car designs

## Prerequisites

A \*nix machine with:
- A CUDA capable NVidia card (metrics below used a GTX 1080Ti)
- CUDA toolkit
- bash
- python3
- scrapy
- pytorch
- torchvision

## Steps
1. Get the data:
```bash
cd acquisition
scrapy crawl acquisition
```

2. Reshape the images as 128x128
```bash
cd shape
.'/resize.sh'
```

3. Train the model
(I trained for 72 hours nonstop to get the results in the demo)
```bash
cd dcgan
.'/train-jpg-images.sh'
```
STARTED Mon 13:52


4. Sort & resize?
polachok/py-phash/tree/python3

## Credits
All images credit https://matchbox.fandom.com/ (CC-BA-SA)
