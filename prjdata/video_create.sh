#!/bin/sh

set -e
#set -x

# we use this instead of docker cp because cp is not guaranteed to be atomic,
# and as a bonus we can keep track of the transfer with kill -USR1

# args:
#  $1: image file name (required to get the extension, to tell ffmpeg)
#  $2: path to save the video file

ext="${1##*.}"

# verify extension
LC_ALL=C echo "$ext" | grep -E '^[a-zA-Z0-9]+$' || exit 10

tmpin="$(mktemp -p /tmp).${ext}"
tmpout="$(mktemp -p /tmp).mp4"

dd if=/dev/fd/0 of="${tmpin}" bs=1M

ft="$(file -i "${tmpin}" | awk '{split($2, type, "/"); print type[1]}')"

if [ "$ft" = "image" ]
then
    ffmpeg -loop 1 -i "${tmpin}" -vb 1024k -an -s 640x480 -pix_fmt nv12 -r 25 -t 10 "${tmpout}"
elif [ "$ft" = "video" ]
then
    ffmpeg -i "${tmpin}" -vb 1024k -an -s 640x480 -pix_fmt nv12 -r 25 "${tmpout}"
fi

mv "${tmpout}" "${2}"
rm "${tmpin}"
