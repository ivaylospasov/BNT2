#!/bin/bash
# GhostScript should be installed y default in Ubuntu.

gs -o $2 -sDEVICE=pdfwrite -dPDFFitPage -r300x300 -g5000x5000 $1 && rm $1
