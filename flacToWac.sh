#!/bin/bash
# usage:. ./flacToWac.sh /fastdata/ac1zy/data/libri/LibriSpeech
function flacToWav(){
  echo $1
  ext=${1##*.}
  echo $ext
  if [ $ext = 'flac' ]
  then
    #echo "True"
    filename=$(basename $1 .flac)
    name=${1%.*}
    echo $filename
    ffmpeg -i $1 ${name}.wav
    
  fi
}

function travFolder(){
  echo $1
  flist=`ls $1`
  cd $1
  #echo $flist
  for f in $flist
  do
    if test -d $f
    then
      travFolder $f
    else
      flacToWav $f
    fi
  done
  cd ../
}
travFolder $1
