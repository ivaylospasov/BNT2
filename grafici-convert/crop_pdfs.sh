#!/bin/bash
# You need pdfcrop installed. It is a part from texlive-extra-utils package in Ubuntu.


pdfcrop $1 $2 && rm $1
