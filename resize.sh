for f in apriltag-imgs/tag16h5/*.png; do
  convert ./"$f" -scale 2000% ./"${f%}"
done