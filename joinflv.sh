#!/bin/bash

current_dir=`pwd`

now=$(date +"_%Y%m%d")

output_file=$1$now.flv

all_files=$current_dir/*.flv

my_list=$current_dir/mylist.txt

for f in $current_dir/*.flv; do echo "file '$f'" >> $my_list; done

ffmpeg -f concat -safe 0 -i $my_list -c copy $output_file

rm $my_list
