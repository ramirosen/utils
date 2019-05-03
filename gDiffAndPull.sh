#!/bin/sh

master_branch='master'
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
#echo "current_branch=" $current_branch
RED='\e[1;31m'
NC='\e[0m' # No Color



if [ $master_branch = $current_branch ]  
then
	echo -e "${RED} master${NC}"
else
	echo -e "${RED} Not master branch!! ${NC}" && exit
fi

diffStr=`git diff`

if [ -z "${diffStr}" ]; then
    echo "diffStr is empty, calling git pull"
    git pull
else
    echo "diffStr is not empty"
fi
            
