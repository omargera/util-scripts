#!/bin/bash
for full_path in /home/omar/Downloads/temp/x/upload/*.csv; do
	echo "full path is: $full_path"
	file_name="${full_path##*/}"
	echo "file_name is $file_name"
	new_name="${file_name:20}"
	echo "new name: $new_name"
	echo "new path: /home/omar/Downloads/temp/x/upload/$new_name"
	# mv "$full_path" /home/omar/Downloads/temp/x/upload/"$new_name"
    # cp "$full_path" /home/omar/Downloads/temp/x/upload/"${filename:20}"
    # cp /home/omar/Downloads/temp/x/procssed/"$filename" /home/omar/Downloads/temp/x/upload/'cut -c 5- "$filename"'
done
