#!/bin/bash
# Resize all images in raw/ to a fixed height.
# Requires ImageMagick.

for x in raw/*; do
  y=$(basename $x)
  z=${y%.*}.jpg
  echo $x '-->' $z
  w=$(identify -format "%w" $x)
  h=$(identify -format "%h" $x)
  if (( $w < $h )); then
    convert $x -resize 100 -crop 100x100+0+0 -fill white -opaque none $z
  else
    convert $x -resize x100 -crop 100x100+0+0 -fill white -opaque none $z
  fi
done
