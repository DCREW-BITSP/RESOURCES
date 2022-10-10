#!/bin/bash

while [ 1 ]
do
    file=$(pwd)
    passw=$(echo $file | sed 's:.*/::')
    echo $passw
    unzip -P $passw *.zip
    echo $(ls -d */|head -n 1)
    cd $(ls -d */|head -n 1)
    file=$(pwd)
    echo $file
done
