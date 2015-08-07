#!/bin/bash

for FILE in *.doc; do
    soffice --convert-to pdf "${FILE}" --headless
done

for FILE in *.doc*; do
    gs -o "${FILE}-new.pdf" -sDEVICE=pdfwrite -dPDFFitPage -r300x300 -g5000x5000 "${FILE}"
done

for FILE in *.pdf; do
    pdfcrop "${FILE}"
done

for FILE in *-crop.pdf; do
    convert "${FILE}" -flatten "${FILE}".png
done
