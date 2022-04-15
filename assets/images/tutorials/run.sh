#!/bin/bash
# Resize all images in raw/ to a fixed height.
# Requires ImageMagick.

for x in raw/*; do
  y=$(basename $x)
  z=${y%.*}.jpg
  echo $x '-->' $z
  convert $x -resize x100 -fill white -opaque none $z
done
