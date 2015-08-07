#!/bin/bash
# You need imagemagick installed

convert $1 -flatten $2 && rm $1
