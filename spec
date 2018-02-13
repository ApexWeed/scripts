#!/bin/bash

mkdir spec
for file in *.flac
do
    outfile="${file%.*}.png"
    sox "$file" -n spectrogram -t "$file" -o "spec/$outfile"
    echo "<img src=\"${outfile}\">" >> spec/index.html
done
